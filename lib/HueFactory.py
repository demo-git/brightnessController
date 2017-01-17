# coding: utf-8
import httplib
import logging
import json
from Hue import Hue


class HueFactory:
    __connect = None
    __user = None
    __nbhue = None

    def __init__(self):
        request = httplib.HTTPSConnection(self.__connect)
        request.request("GET", "https://www.meethue.com/api/nupnp")
        response = request.getresponse()

        if response.status == 200:
            logging.log(logging.INFO, 'POST upnp 200')
            data = json.dumps(response.read())
            self.__connect = data['internalipaddress']
        else:
            logging.log(logging.INFO, 'POST upnp ' + response.status)
            self.__connect = "error"

        request.close()

    def generate(self):
        observers = []
        i = 1
        while i <= self.__nbhue:
            hue = Hue(self.__connect, i, self.__user)
            observers.append(hue)
            i += 1

        return observers

    def get_user(self):
        status = 0
        x = 0
        while status != 1 and x < 5:
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

            x += 1
            request.close()

    def get_lights(self):
        request = httplib.HTTPSConnection(self.__connect)
        string = "http://" + self.__connect + "/api/" + self.__user + "/lights"
        request.request("GET", string)
        response = request.getresponse()
        status = 0

        if response.status == 200:
            logging.log(logging.INFO, 'GET get_lights 200')
            data = json.dumps(response.read())
            self.__nbhue = data.count()
            status = 1
        else:
            logging.log(logging.INFO, 'GET get_lights ' + response.status)

        request.close()
        return status

    def get_connect(self):
        return self.__connect
