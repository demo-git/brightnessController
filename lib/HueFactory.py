# coding: utf-8
import httplib
import logging
import json
from Hue import Hue
import time
import sys


class HueFactory:
    __connect = None
    __user = None
    __nbhue = None

    # construct object and detect hue bridge
    def __init__(self):
        request = httplib.HTTPSConnection("www.meethue.com")
        request.request("GET", "/api/nupnp")
        response = request.getresponse()
        data = json.loads(response.read())

        if response.status == 200 and 'internalipaddress' in data[0]:
            logging.log(logging.INFO, 'POST upnp 200')
            self.__connect = data[0]['internalipaddress']
        else:
            logging.log(logging.INFO, 'POST upnp ' + str(response.status))
            self.__connect = "error"

        request.close()

    # generate hue objects
    def generate(self):
        observers = []
        i = 1
        while i <= self.__nbhue:
            hue = Hue(self.__connect, i, self.__user)
            observers.append(hue)
            i += 1

        return observers

    # get user for use api of hue bridge
    def get_user(self):
        status = 0
        x = 0
        while status != 1 and x < 5:
            request = httplib.HTTPConnection(self.__connect)
            request.request("POST", "/api", '{"devicetype":"rasp_brightness_sensor"}')
            response = request.getresponse()
            data = json.loads(response.read())
            if 'success' in data[0] and response.status == 200:
                logging.log(logging.INFO, 'POST get_user 200')
                self.__user = data[0]['success']['username']
                status = 1
            else:
                logging.log(logging.INFO, 'POST get_user ' + str(response.status))
                sys.stdout.write(data[0]['error']['description'])
                time.sleep(2)

            x += 1
            request.close()

        return status

    # get number of hue light on this bridge
    def get_lights(self):
        request = httplib.HTTPConnection(self.__connect)
        request.request("GET", "/api/" + self.__user + "/lights")
        response = request.getresponse()
        status = 0
        data = json.loads(response.read())

        if response.status == 200 and 'error' not in data:
            logging.log(logging.INFO, 'GET get_lights 200')
            self.__nbhue = len(data)
            status = 1
        else:
            logging.log(logging.INFO, 'GET get_lights ' + str(response.status))

        request.close()
        return status

    # get current connect string
    # return "error" if connection is impossible
    def get_connect(self):
        return self.__connect
