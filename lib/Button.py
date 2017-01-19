# coding: utf-8
from Sensor import Sensor
from threading import Lock
import sys


class Button(Sensor):
    __state = None
    __lock = None

    def __init__(self, channel):
        Sensor.__init__(self, channel)
        self.__lock = Lock()

    # notify all of observers if state change
    def notify(self, args):
        sys.stdout.write(str(args))
        if args == 1:
            self.__lock.acquire()
            if self.__state == 0:
                self.__state = 1
            else:
                self.__state = 0

            for observer in self._observers:
                observer.update(self.__state)

            self.__lock.release()

    # return current state
    def get_state(self):
        self.__lock.acquire()
        state = self.__state
        self.__lock.release()
        return state
