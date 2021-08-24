import sims4.commands
import irc
import threading

@sims4.commands.Command('tds', command_type=sims4.commands.CommandType.Live)
def init(_connection=None):
    output = sims4.commands.CheatOutput(_connection)
    output('Welcome to Twitch decides Sims 4!')
    output('developed by CodeRoria')
    output('https://github.com/coderoria')
    ircThread = threading.Thread(target=irc.connect, args=(_connection,))
    ircThread.start();

@sims4.commands.Command('tds.patch', command_type=sims4.commands.CommandType.Live)
def patch(_connection=None):
    sims4.commands.output = sims4.commands.cheat_output

    sims4.commands.output("If you can see this, Sims4 has been successfully patched!", _connection)