# coding: utf-8
from Sensor import Sensor


class Button(Sensor):
    __value = None

    def __init__(self, channel, value):
        Sensor.__init__(self, channel)
        self.__value = value

    # notify all of observers if state change
    def notify(self, args):
        if args == 1:
            for observer in self._observers:
                observer.update(self.__value)
