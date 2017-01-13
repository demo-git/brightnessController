# coding: utf-8
import RPi.GPIO as GPIO
from lib import BrightnessSensor

# init var
channel = 1

# GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
sensor = BrightnessSensor.BrightnessSensor(channel, 70, 1024)
