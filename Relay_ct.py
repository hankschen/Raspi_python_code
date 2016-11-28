#!/usr/bin/python
# -*- conding = UTF-8 -*-
import sys
import urllib
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(38, GPIO.OUT)

while True:
    try:
        GPIO.output(38, True)
        print "high"
        sleep(1)
        GPIO.output(38, False)
        print "low"
        sleep(1)
    except:
        GPIO.cleanup()