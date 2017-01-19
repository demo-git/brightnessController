# coding: utf-8
import RPi.GPIO as GPIO
from Observer import Observer
import sys


class Led(Observer):
    __channel = None

    def __init__(self, channel):
        Observer.__init__(self)
        self.__channel = channel
        GPIO.setup(channel, GPIO.OUT)

    # callback observer
    def update(self, state):
        sys.stdout.write('moove ma gueule\r')
        GPIO.output(self.__channel, state)

    def __del__(self):
        GPIO.cleanup(self.__channel)
