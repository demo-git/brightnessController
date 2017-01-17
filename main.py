# coding: utf-8
import RPi.GPIO as GPIO
import time
import logging
from lib.BrightnessSensor import BrightnessSensor
from lib.HueFactory import HueFactory
from lib.Button import Button
from lib.Led import Led

# init var
channel_brightness = 1
channel_button = 2
channel_led = 3
percent = 70
maxi = 1024
state = 0

# set warnings to false in production
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BOARD)

# init object
sensor = BrightnessSensor(channel_brightness, percent, maxi)
factory = HueFactory()
status = factory.get_connect()
if status != 'error':
    status = factory.get_user()
    if status != 0:
        status = factory.get_lights()
        if status != 0:
            sensor.add_observers(factory.generate())
        else:
            logging.log(logging.ERROR, 'impossible de générer les hues')
    else:
        logging.log(logging.ERROR, 'pas de user trouvé')
else:
    logging.log(logging.ERROR, 'pas de bridge trouvé')
button = Button(channel_button)
led = Led(channel_led)

# works
while True:
    if button.get_state() == 1:
        if state == 0:
            state = 1
            sensor.add_event()
    else:
        if state == 1:
            state = 0
            sensor.remove_event()

    # sleep for optimize performance
    time.sleep(0.2)
