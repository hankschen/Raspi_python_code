#!/usr/bin/env python
#-*- coding=UTF-8 -*-
import urllib2
import json
from time import sleep
import math
import RPi.GPIO as GPIO

READ_API_KEY = "UG1QRHRYGLSZVP8I"
CHANNEL_ID = "178323"

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(38, GPIO.OUT)

def main():
    while True:
        conn = urllib2.urlopen("http://api.thingspeak.com/channels/%s/feed/last.json?api_key=%s" % (CHANNEL_ID, READ_API_KEY))
        response = conn.read()
        print "http status code = %s" % (conn.getcode())
        data = json.loads(response)
        print data['field4']

        if data['field4'] == "1":
            GPIO.output(38, True)
        if data['field4'] == "0":
            GPIO.output(38, False)
        #print data #3
        conn.close()
        sleep(3)

if __name__ == '__main__':
    main()
