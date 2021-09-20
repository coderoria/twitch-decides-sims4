import sims4.commands
import sims4.reload
import irc
import threading
import enum
import server_commands

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
    testEnum = sims4.commands.CommandType.DebugOnly
    sims4.commands.CommandType = CommandType
    assert testEnum != sims4.commands.CommandType.DebugOnly
    sims4.commands.is_command_available = lambda command_type: True
    # TODO: check if this really makes a difference (testingcheats/automationcheats)
    sims4.commands.execute("AutomationTestingCheats on", _connection)

    #sims4.reload.reload_module(server_commands)

    sims4.commands.output("If you can see this, Sims4 has been successfully patched!", _connection)
    sims4.commands.output("Native commands enabled: " + str(sims4.commands.__enable_native_commands), _connection)
    sims4.commands.output("Can execute DebugOnly: " + str(sims4.commands.is_command_available(sims4.commands.CommandType.DebugOnly)), _connection)

@sims4.commands.Command('tds.test', command_type=sims4.commands.CommandType.DebugOnly)
def test(_connection=None):
    sims4.commands.output("HELLO THERE", _connection)

class CommandType(enum.Int, export=False):
    DebugOnly = 6
    Automation = 3
    Cheat = 4
    Live = 5