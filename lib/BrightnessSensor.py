# coding: utf-8
from Sensor import Sensor


class BrightnessSensor(Sensor):
    __threshold = None
    __max = None

    def __init__(self, channel, threshold, maxi):
        Sensor.__init__(self, channel)
        self.__threshold = threshold
        self.__max = maxi

    # notify all observers with the new intensity
    def notify(self, args):
        # percent of luminosity
        args = (args*self.__max)/100
        if args >= self.__threshold:
            args = -1
        else:
            # percent of hue use needs
            args = (args*self.__threshold)/100

        for observer in self.__observers:
            observer.update(args)
