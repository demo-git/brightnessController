# coding: utf-8
import RPi.GPIO as GPIO
from Observer import Observer


class Led(Observer):
    __channel = None

    def __init__(self, channel):
        self.__channel = channel
        GPIO.setup(channel, GPIO.OUT)

    # callback observer
    def update(self, state):
        GPIO.output(self.__channel, state)

    def __del__(self):
        GPIO.cleanup(self.__channel)
