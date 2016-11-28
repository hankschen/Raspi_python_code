#!/usr/bin/python
# -*- coding = UTF-8 -*-

import sys
import urllib
import RPi.GPIO as GPIO
from time import sleep
import Adafruit_DHT
import urllib2
import spidev

spi = spidev.SpiDev()
spi.open(0, 0)

def readadc(adcnum):
        if adcnum > 7 or adcnum < 0:
                print "Wrong port num"
                return -1
        r = spi.xfer2([1, 8+adcnum << 4, 0])
        adcount = ((r[1] & 3) << 8) + r[2]
        return adcount

def getSensorData():
	      RH, T = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 23)
	      # return dict
	      return (str(RH), str(T))

# main() function
def main():
	      if len(sys.argv) < 2:
		          print('Usage:python tstest.py PRIVATE_KEY')
		          exit(0)
	      print 'starting....'
	      baseURL = "https://api.thingspeak.com/update?api_key=%s" % sys.argv[1]
	      print baseURL

	      while True:
     		 try:
	      		RH, T = getSensorData()
	     	        print RH
	      		print T
	                gas = int(round(readadc(3)/1.024))
	                print gas
	                f = urllib2.urlopen(baseURL + "&field1=%s&field2=%s" % (RH, T)+"&field3="+str(gas))
	                print f.read()
	                sleep(10)
     	         except:
	                print "exiting."
	                break
# call main
if __name__=='__main__':
	main()

