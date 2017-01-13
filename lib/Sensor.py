# coding: utf-8
import RPi.GPIO as GPIO
import Observable


class Sensor(Observable):
    __channel = None

    def __init__(self, channel):
        Observable.Observable.__init__(self)
        self.__channel = channel
        GPIO.setup(channel, GPIO.IN)
        GPIO.add_event_callback(channel, GPIO.FALLING, callback=self.update(), bouncetime=200)

    def update(self):
        self.notify(GPIO.input(self.__channel))

    def __del__(self):
        GPIO.remove_event_detect(self.__channel)
        GPIO.cleanup(self.__channel)
