#!/usr/bin/python
# -*- conding = UTF-8 -*-

from Tkinter import *
import sys
import RPi.GPIO as GPIO
import Adafruit_DHT

def getSensorData():
    RH, T = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 23)
    #return dict
    return (str(RH), str(T))


root = Tk()

var = StringVar()
label = Label(root, textvariable=var, relief=RAISED)
label.config(font=("Courier", 20))

RH, T = getSensorData()
var.set("Hey!? How are you doing?"+str(RH)+"%"+str(T)+"c")
label.pack()

root.mainloop()
