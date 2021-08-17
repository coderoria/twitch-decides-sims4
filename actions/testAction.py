from actions import TimedAction
import sims4

class TestAction(TimedAction):
    requiredPack = sims4.common.Pack.EP01

    def run(self):
        return super().run(5.0)

    def stop(self):
        print("test")
