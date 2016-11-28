#!/usr/bin/python
#-*- coding = UTF-8 -*-

import spidev
import time

spi = spidev.SpiDev()
spi.open(0,0)
count = 0

def readdac(adcnum):
    if adcnum > 7 or adcnum < 0:
        print "Wrong port num"
        return -1
    r = spi.xfer2([1, 8+adcnum << 4, 0])
    adcount = ((r[1] & 3) << 8) + r[2]
    return adcount

while True:
    tmp1 = int(round(readdac(0) / 1.024)) #Read MCP3008 CH0(SW) value,look layout
    tmp2 = int(round(readdac(1) / 1.024)) #Read MCP3008 CH1(VRY) value,look layout
    tmp3 = int(round(readdac(2) / 1.024)) #Read MCP3008 CH2(VRX) value,look layout
    tmp4 = int(round(readdac(3) / 1.024)) #Read MCP3008 CH3(A0) value,look layout
    if tmp1 == 0 and tmp2 > 400:
        print "press"
    if tmp2 == 0:
        print "right"
    if tmp2 > 600:
        print "left"
    if tmp3 < 5:
        print "up"
    if tmp3 > 600:
        print "down"
    print "int1:",tmp1
    #print "int2:",tmp2
    #print "int3:",tmp3
    #print "int4:",tmp4
    count = count + 1
    time.sleep(0.5)