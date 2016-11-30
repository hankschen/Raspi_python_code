#!/usr/bin/python
# -*- coding = UTF-8 -*-
import sys
import urllib
import RPi.GPIO as GPIO
from time import sleep
import Adafruit_DHT
import urllib2
import spidev
import smbus
import time
import os
import MFRC522
import signal
uid = [0,0,0,0]

PIR_PIN = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIR_PIN, GPIO.IN)

# define some constant from the datasheet
DEVICE = 0x23  # define device I2C address
POWER_DOWN = 0x00  # no active I2C address
POWER_ON = 0x01  # power on
RESET = 0x07  # reset data register value
CONTINUOUS_LOW_RES_MODE = 0x13  # start measurement at 41x resolution. time typically 16ms
CONTINUOUS_HIGH_MODE_1 = 0x10  # start measurement at 11x resolutation.time typically 120ms
CONTINUOUS_HIGH_MODE_2 = 0X11  # start measurement at 0.51x resulation.time typically 120ms
# start measurement at 11x resulation. time typically 120ms
# device is automatically set to power down after measurement
ONE_TIME_HIGH_RES_MODE_1 = 0X20
# start measurement at 0.51x resulation. time typically 120ms
# device is automatically set to power down after measurement
ONE_TIME_HIGH_RES_MODE_2 = 0X21
# start measurement at 11x resulation. time typically 120ms
# device is automatically set to power down after measurement
ONE_TIME_LOW_RES_MODE = 0X23
# bus = smbus.SMBus(0) # Rev 1 Pi uses 0
bus = smbus.SMBus(1)  # Rev 2 Pi uses 1

######### RFID ###############################################
# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()
# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)
# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()
######### RFID ###############################################

def convertToNumber(data):
    # Simple function to cinvert 2 bytes of data
    # into a decimal number
    return ((data[1] + (256 * data[0])) / 1.2)

def readLight(addr=DEVICE):
    data = bus.read_i2c_block_data(addr, ONE_TIME_HIGH_RES_MODE_1)
    return convertToNumber(data)

spi = spidev.SpiDev()
spi.open(0, 0)

def readadc(adcnum):
    if adcnum > 7 or adcnum < 0:
        print "Wrong port num"
        return -1
    r = spi.xfer2([1, 8 + adcnum << 4, 0])
    adcount = ((r[1] & 3) << 8) + r[2]
    return adcount

def getSensorData():
    RH, T = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 23)
    # return dict
    return (str(RH), str(T))

def main():
    #use sys.argv if needed
    if len(sys.argv) < 2:
        print('Usage:python tstest.py PRIVATE_KEY')
        exit(0)
    print 'starting....'
    baseURL = "https://api.thingspeak.com/update?api_key=%s" % sys.argv[1]
    print baseURL

    while True:
        try:
            ######### RFID ###############
            # Scan for cards
            (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
            # If a card is found
            if status == MIFAREReader.MI_OK:
                print "Card detected"
            # Get the UID of the card
            (status, uid) = MIFAREReader.MFRC522_Anticoll()
            # If we have the UID, continue
            if status == MIFAREReader.MI_OK:
                # Print UID
                print "Card read UID: " + str(uid[0]) + "," + str(uid[1]) + "," + str(uid[2]) + "," + str(uid[3])
            else:
                uid[0,0,0,1]
            ######### RFID ###############

            RH, T = getSensorData()
            print RH
            print T

            gas = int(round(readadc(3) / 1.024))  # MQ2 in port:3
            print gas

            light = "%.1f" % (readLight())
            print light

            pir = str(GPIO.input(PIR_PIN))
            print pir

            f = urllib2.urlopen(baseURL +
                                "&field1=%s&field2=%s&field3=%s&field5=%s&field6=%s" % (RH, T, gas, light, pir))
            print f.read()
            f.close()
            sleep(10)
        except:
            print "exiting."
            break  # call main

if __name__ == '__main__':
    main()
