# coding: utf-8
import RPi.GPIO as GPIO
from Observable import Observable


class Sensor(Observable):
    __channel = None

    def __init__(self, channel):
        Observable.__init__(self)
        self.__channel = channel
        GPIO.setup(channel, GPIO.IN)

    # callback observer
    def update(self, value):
        self.notify(GPIO.input(value))

    # add an event for listen GPIO
    def add_event(self):
        GPIO.add_event_detect(self.__channel, GPIO.BOTH, callback=self.update, bouncetime=200)

    # remove event of listen GPIO
    def remove_event(self):
        GPIO.remove_event_detect(self.__channel)

    def __del__(self):
        GPIO.cleanup(self.__channel)
