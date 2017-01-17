# coding: utf-8
import RPi.GPIO as GPIO
from Observable import Observable


class Sensor(Observable):
    __channel = None

    def __init__(self, channel):
        Observable.__init__(self)
        self.__channel = channel
        GPIO.setup(channel, GPIO.IN)

    def update(self):
        self.notify(GPIO.input(self.__channel))

    def add_event(self):
        GPIO.add_event_callback(self.__channel, GPIO.FALLING, callback=self.update(), bouncetime=200)

    def remove_event(self):
        GPIO.remove_event_detect(self.__channel)

    def __del__(self):
        GPIO.cleanup(self.__channel)
