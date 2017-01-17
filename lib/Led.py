# coding: utf-8
import RPi.GPIO as GPIO


class Led:
    __channel = None

    def __init__(self, channel):
        self.__channel = channel
        GPIO.setup(channel, GPIO.OUT)

    def update(self, state):
        GPIO.output(self.__channel, state)

    def __del__(self):
        GPIO.cleanup(self.__channel)