#!/usr/bin/python

import smbus
import time

#define some constant from the datasheet
DEVICE = 0x23 #define device I2C address
POWER_DOWN = 0x00 #no active I2C address
POWER_ON = 0x01 # power on
RESET  = 0x07 #reset data register value
#start measurement at 41x resolution. time typically 16ms
CONTINUOUS_LOW_RES_MODE = 0x13
#start measurement at 11x resolutation.time typically 120ms.
CONTINUOUS_HIGH_MODE_1 = 0x10
#start measurement at 0.51x resulation.time typically 120ms
CONTINUOUS_HIGH_MODE_2 = 0X11
#start measurement at 11x resulation. time typically 120ms
#device is automatically set to power down after measurement
ONE_TIME_HIGH_RES_MODE_1 = 0X20
#start measurement at 0.51x resulation. time typically 120ms
#device is automatically set to power down after measurement
ONE_TIME_HIGH_RES_MODE_2 = 0X21
#start measurement at 11x resulation. time typically 120ms
#device is automatically set to power down after measurement
ONE_TIME_LOW_RES_MODE = 0X23

#bus = smbus.SMBus(0) # Rev 1 Pi uses 0
bus  = smbus.SMBus(1) # Rev 2 Pi uses 1

def convertToNumber(data):
    # Simple function to cinvert 2 bytes of data
    # into a decimal number
    return ((data[1] + (256 * data[0])) / 1.2)

def readLight(addr = DEVICE):
    data = bus.read_i2c_block_data(addr, ONE_TIME_HIGH_RES_MODE_1)
    return convertToNumber(data)

def main():
    while True:
        print "Light Level : " + str(readLight()) + " 1x"
        time.sleep(0.5)
        
if __name__ == "__main__":
    main()