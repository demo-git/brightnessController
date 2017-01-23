# coding: utf-8
import RPi.GPIO as GPIO
from Observable import Observable


class Sensor(Observable):
    __channel = None

    def __init__(self, channel):
        Observable.__init__(self)
        self.__channel = channel
        GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    # callback observer
    def update(self, chan):
        self.notify(chan)

    # add an event for listen GPIO
    def add_event(self, value):
        if value == 1:
            GPIO.add_event_detect(self.__channel, GPIO.RISING, callback=self.update, bouncetime=500)
        elif value == 0:
            GPIO.add_event_detect(self.__channel, GPIO.FALLING, callback=self.update, bouncetime=500)
        else:
            GPIO.add_event_detect(self.__channel, GPIO.BOTH, callback=self.update, bouncetime=500)

    # remove event of listen GPIO
    def remove_event(self):
        GPIO.remove_event_detect(self.__channel)

    def __del__(self):
        GPIO.cleanup(self.__channel)
