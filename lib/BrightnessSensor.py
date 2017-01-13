# coding: utf-8
import Sensor


class BrightnessSensor(Sensor):
    __threshold = None
    __max = None

    def __init__(self, channel, threshold, max):
        Sensor.Sensor.__init__(self, channel)
        self.__threshold = threshold
        self.__max = max

    def notify(self, args):
        # percent of luminosity
        args = (args/100)*self.__max
        if args >= self.__threshold:
            args = -1
        else:
            # percent of hue use needs
            args = (args/100)*self.__threshold

        for observer in self.__observers:
            observer.update(args)
