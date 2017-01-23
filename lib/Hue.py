# coding: utf-8
import httplib
import logging
from threading import Lock
from Observer import Observer
import sys


class Hue(Observer):
    __connect = None
    __string = None
    __intensity = None
    __lock = None

    def __init__(self, connect, number, user):
        Observer.__init__(self)
        self.__connect = connect
        self.__string = "/api/" + user + "/lights/" + str(number) + "/state"
        self.__lock = Lock()
        self.__intensity = 0
        self.change_state(0)

    # change the state of hue light and its intensity
    def change_state(self, on, intensity=None):
        request = httplib.HTTPConnection(self.__connect)

        if on == 1:
            intensity = int(round((intensity * 254) / 100))
            request.request("PUT", self.__string, '{"on":true, "bri":' + str(intensity) + '}')
        else:
            request.request("PUT", self.__string, '{"on":false}')

        response = request.getresponse()
        if response.status == 200:
            logging.log(logging.INFO, 'PUT on/off 200')
        else:
            logging.log(logging.INFO, 'PUT on/off ' + str(response.status))

        request.close()

    # callback observer
    def update(self, value):
        sys.stdout.write(str(value))
        self.__lock.acquire()
        tmp = -1
        if (self.__intensity > 0 and value < 0) or (self.__intensity < 100 and value > 0):
            self.__intensity += value
            tmp = self.__intensity

        self.__lock.release()
        if tmp != -1:
            if tmp > 0:
                self.change_state(1, tmp)
            else:
                self.change_state(0)
