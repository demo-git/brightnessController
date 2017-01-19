# coding: utf-8
import RPi.GPIO as GPIO
import time
import logging
from lib.BrightnessSensor import BrightnessSensor
from lib.HueFactory import HueFactory
from optparse import OptionParser
from lib.Button import Button
from lib.Led import Led
import sys


# argument
parser = OptionParser()
parser.add_option("-i", "--cbri", dest="cbri", help="Channel brightness", type=int)
parser.add_option("-b", "--cb", dest="cb", help="Channel button", type=int)
parser.add_option("-l", "--cl", dest="cl", help="Channel led", type=int)
parser.add_option("-p", "--percent", dest="percent", help="percent limit for hue off", type=int)
(options, args) = parser.parse_args()

# init var
channel_brightness = options.cbri
channel_button = options.cb
channel_led = options.cl
# default 70
percent = options.percent
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
        sys.stdout.writelines('compter les hues\r')
        if status != 0:
            sensor.add_observers(factory.generate())
            sys.stdout.writelines('générer les hues\r')
        else:
            logging.log(logging.ERROR, 'impossible de générer les hues')
            sys.stdout.writelines('impossible de générer les hues\r')
    else:
        logging.log(logging.ERROR, 'pas de user trouvé')
        sys.stdout.writelines('pas de user trouvé\r')
else:
    logging.log(logging.ERROR, 'pas de bridge trouvé')
    sys.stdout.writelines('pas de bridge trouvé\r')
button = Button(channel_button)
led = Led(channel_led)

# works
while True:
    if button.get_state() == 1:
        if state == 0:
            sys.stdout.writelines('change state to active\r')
            state = 1
            sensor.add_event()
    else:
        if state == 1:
            sys.stdout.writelines('change state to off\r')
            state = 0
            sensor.remove_event()

    # sleep for optimize performance
    time.sleep(0.2)

    # TODO: supprimer après test
    sensor.update()
