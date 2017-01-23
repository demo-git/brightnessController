# coding: utf-8
import RPi.GPIO as GPIO
import logging
from lib.HueFactory import HueFactory
from optparse import OptionParser
from lib.Button import Button
import time
import sys


# argument
parser = OptionParser()
parser.add_option("-l", "--btnl", dest="btnl", help="Channel button less", type=int)
parser.add_option("-m", "--btnm", dest="btnm", help="Channel button more", type=int)
parser.add_option("-p", "--percent", dest="percent", help="Percent", type=int)
(options, args) = parser.parse_args()

# init var
percent = options.percent

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# init object
buttonL = Button(options.btnl, percent * -1)
buttonM = Button(options.btnm, percent)

factory = HueFactory()
status = factory.get_connect()
if status != 'error':
    status = factory.get_user()
    if status != 0:
        status = factory.get_lights()
        if status != 0:
            hues = factory.generate()
            buttonM.add_observers(hues)
            buttonL.add_observers(hues)
            buttonM.add_event(0)
            buttonL.add_event(0)

            sys.stdout.write("\nPush a keyboard key for quit...")

            try:
                raw_input()
            except KeyboardInterrupt:
                pass

        else:
            logging.log(logging.ERROR, 'impossible de générer les hues')
    else:
        logging.log(logging.ERROR, 'pas de user trouvé')
else:
    logging.log(logging.ERROR, 'pas de bridge trouvé')
