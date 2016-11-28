#!/usr/bin/python
# -*- conding = UTF-8 -*-

import sys
import urllib
import RPi.GPIO as GPIO
import time
from time import sleep
import Tkinter
import tkMessageBox

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(38, GPIO.OUT)

top = Tkinter.Tk()

def helloCallBack_0():
    #tkMessageBox.showinfo("Hello Python", "Hello World")
    GPIO.output(38, False)
    print "high"

def helloCallBack_1():
    GPIO.output(38, False)
    print "low"

B_0 = Tkinter.Button(top, text = "ON", command = helloCallBack_0())
B_1 = Tkinter.Button(top, text = "OFF", command = helloCallBack_1())

B_0.pack()
B_1.pack()
top.mainloop()