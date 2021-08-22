import socket
import sys
import sims4.commands
import sims4.callback_utils
import config
import re

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER = "irc.chat.twitch.tv"
CHANNEL = ""

def connect(_context):
    config.reload();
    TOKEN = str(config.config["IRC"]["token"])
    NICK = str(config.config["IRC"]["nick"])
    CHANNEL = str(config.config["IRC"]["channel"])
    
    output = sims4.commands.CheatOutput(_context)
    output("Connecting to IRC (" + CHANNEL + ")")
    try:
        ircsock.connect((SERVER, 6667))
        # authenticate with token provided in config
        ircsock.send(bytes("PASS oauth:" + TOKEN + "\n", "UTF-8"))
        # provide nick from config
        ircsock.send(bytes("NICK " + NICK + "\n", "UTF-8"))
        # join channel
        ircsock.send(bytes("JOIN " + CHANNEL + "\n", "UTF-8"))
        # require capability for user tags
        ircsock.send(bytes("CAP REQ :twitch.tv/tags\n", "UTF-8"))
        # send startup message to chat
        ircsock.send(bytes("PRIVMSG " + CHANNEL + " :Sims 4 connected to chat." + "\n", "UTF-8"))
        while 1:
            ircmsg = ircsock.recv(2048).decode("UTF-8")
            ircmsg = ircmsg.strip('\r\n')
            if(bool(re.match(r'^PING :.*$', ircmsg))):
                ircsock.send(bytes("PONG :tmi.twitch.tv\n", "UTF-8"))

            parseMessage(ircmsg, _context)
    except:
        output(str(sys.exc_info()))

def parseMessage(data, _context):
    output = sims4.commands.CheatOutput(_context)
    # [FULLMATCH, TAGS, USERNAME, MESSAGE]
    messageMatch = re.match(r'^@(\S+)\s:(\S+)!\S+\sPRIVMSG\s'+ CHANNEL +'\s:(.*)$', data);
    if not bool(messageMatch):
        return
    tags = parseTags(messageMatch.group(1))
    username = messageMatch.group(2)
    message = messageMatch.group(3)

    if tags["mod"] == "1" and message.startswith("!cheat"):
        sims4.commands.execute(message.replace("!cheat ", ""), _context)
    output(username + ": " + message)

def parseTags(tagMessage):
    tagDir = {}
    tags = tagMessage.split(";")
    for tag in tags:
        keyValue = tag.split("=")
        tagDir[keyValue[0]] = keyValue[1]
    return tagDir
