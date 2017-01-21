# coding: utf-8
from Sensor import Sensor
import sys


class Button(Sensor):
    __value = None

    def __init__(self, channel, value):
        Sensor.__init__(self, channel)
        self.__value = value

    # notify all of observers if state change
    def notify(self, args):
        sys.stdout.write(str(self.__value))
        for observer in self._observers:
            observer.update(self.__value)
