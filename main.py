import sims4.commands
import irc
import threading

sims4.commands.output = lambda s,_connection: sims4.commands.cheatOutput(s, _connection)

@sims4.commands.Command('tds', command_type=sims4.commands.CommandType.Live)
def init(_connection=None):
    output = sims4.commands.CheatOutput(_connection)
    output('Welcome to Twitch decides Sims 4!')
    output('developed by CodeRoria')
    output('https://github.com/coderoria')
    ircThread = threading.Thread(target=irc.connect, args=(_connection,))
    ircThread.start();
