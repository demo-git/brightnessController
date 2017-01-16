# coding: utf-8
import httplib
import logging
import json
import Hue


class HueFactory:
    __connect = None
    __user = None
    __nbhue = None

    def __init__(self):
        self.__connect = "TODO"
        self.__nbhue = 0

    def generate(self):
        observers = []
        i = 1
        while i <= self.__nbhue:
            hue = Hue.Hue(self.__connect, i, self.__user)
            observers.append(hue)
            i += 1

        return observers

    def get_user(self):
        status = 0
        while status != 1:
            request = httplib.HTTPSConnection(self.__connect)
            string = "http://" + self.__connect + "/api"
            request.request("POST", string, '{"devicetype":"rasp_brightness_sensor"}')
            response = request.getresponse()
            if response.status == 200:
                logging.log(logging.INFO, 'POST get_user 200')
                data = json.dumps(response.read())
                self.__user = data['success']['username']
                status = 1
            else:
                logging.log(logging.INFO, 'POST get_user ' + response.status)
