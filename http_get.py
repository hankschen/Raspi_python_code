import sys
import urllib
#import PRi.GPIO as GPIO
from time import sleep

while True:
    url = "https://api.thingspeak.com/update?api_key=QPP1BKTA1DCZ7VJX&field1=5&field2=2"
    response = urllib.urlopen(url)
    print response
    sleep(10)

