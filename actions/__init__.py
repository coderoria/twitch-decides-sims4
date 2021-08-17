from threading import Timer

class Action():
    requiredPack = None

class OneTimeAction(Action):
    def run(self):
        pass

class TimedAction(Action):
    def run(self, time):
        Timer(time, self.stop).start()
        pass

    def stop(self):
        pass