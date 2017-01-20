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
        args = (args*100)/self.__max
        if args >= self.__threshold:
            args = -1
        else:
            # percent of hue use needs
            args = 100 - ((args*100)/self.__threshold)

        for observer in self._observers:
            observer.update(args)
