# coding: utf-8
import httplib
import logging


class Hue:
    __connect = None
    __number = None
    __user = None

    def __init__(self, connect, number, user):
        self.__connect = connect
        self.__number = number
        self.__user = user

    def change_state(self, on, intensity=None):
        intensity = (intensity*254)/100
        request = httplib.HTTPSConnection(self.__connect)
        string = "http://" + self.__connect + "/api/" + self.__user + "/lights/" + str(self.__number) + "/state"

        if on == 1:
            request.request("PUT", string, '{"on":true, "bri":' + str(intensity) + '}')
        else:
            request.request("PUT", string, '{"on":false}')

        response = request.getresponse()
        if response.status == 200:
            logging.log(logging.INFO, 'PUT on/off 200')
        else:
            logging.log(logging.INFO, 'PUT on/off ' + response.status)

        request.close()

    def update(self, intensity):
        if intensity > 0:
            self.change_state(1, intensity)
        else:
            self.change_state(0)
