#!/usr/bin/python
# -*- conding = UTF-8 -*-

from Tkinter import *
import sys
import RPi.GPIO as GPIO
import Adafruit_DHT
import Tkinter

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(38, GPIO.OUT)

def helloCallBack_0():
    #tkMessageBox.showinfo("Hello Python", "Hello World")
    GPIO.output(38, False)
    print "high"

def helloCallBack_1():
    GPIO.output(38, False)
    print "low"

def getSensorData():
    RH, T = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 23)
    #return dict
    return (str(RH), str(T))

root = Tkinter.Tk()

var = StringVar()
label = Label(root, textvariable=var, relief=RAISED)
label.config(font=("Courier", 20))

RH, T = getSensorData()
var.set("Hey!? How are you doing?"+str(RH)+"%"+str(T)+"c")

B_0 = Tkinter.Button(root, text = "ON", command = helloCallBack_0())
B_1 = Tkinter.Button(root, text = "OFF", command = helloCallBack_1())

B_0.pack()
B_1.pack()
label.pack()

root.mainloop()