## IMPORTS ##
from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
import time

## Window Setup ##
win = Tk()
win.title("Morse Code by LED")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

## Hardware ##
RPi.GPIO.setmode(RPi.GPIO.BCM)
led1 = LED(17)
led2 = LED(22)
led3 = LED(27)

## Character Limit ##
limit = StringVar()
max_char = 12

def char_limit(*args):
    read = limit.get()
    if len(read)>max_char:
        limit.set(input[:max_char])
limit.trace_variable("w", char_limit)

## User Interface Setup #
ask = Label(win, text = ("Please Enter Word:"))
ask.grid(row=0,column=0)
textInput = Entry(win, bd=6, textvariable=limit)
textInput.grid(row=0,column=1)

## Define Dash and Dot ##
def dot():
    led1.on()
    led2.on()
    time.sleep(0.25)
    led1.off()
    led2.off()
    time.sleep(0.5)

def dash():
    led1.on()
    led3.on()
    time.sleep(1)
    led1.off()
    led3.off()
    time.sleep(0.5)

        ## DATA ENTRY ##
## Define Letters in Morse Code ##
def display(letter):
    if letter == "a":
        dot()
        dash()
    if letter == "b":
        dash()
        dot()
        dot()
        dot()
    if letter == "c":
        dash()
        dot()
        dash()
        dot()
    if letter == "d":
        dash()
        dot()
        dot()
    if letter == "e":
        dot()
    if letter == "f":
        dot()
        dot()
        dash()
        dot()
    if letter == "g":
        dash()
        dash()
        dot()
    if letter == "h":
        dot()
        dot()
        dot()
        dot()
    if letter == "i":
        dot()
        dot()
    if letter == "j":
        dot()
        dash()
        dash()
        dash()
    if letter == "k":
        dash()
        dot()
        dash()
    if letter == "l":
        dot()
        dash()
        dot()
        dot()
    if letter == "m":
        dash()
        dash()
    if letter == "n":
        dash()
        dot()
    if letter == "o":
        dash()
        dash()
        dash()
    if letter == "p":
        dot()
        dash()
        dash()
        dot()
    if letter == "q":
        dash()
        dash()
        dot()
        dash()
    if letter == "r":
        dot()
        dash()
        dot()
    if letter == "s":
        dot()
        dot()
        dot()
    if letter == "t":
        dash()
    if letter == "u":
        dot()
        dot()
        dash()
    if letter == "v":
        dot()
        dot()
        dot()
        dash()
    if letter == "w":
        dot()
        dash()
        dash()
    if letter == "x":
        dash()
        dot()
        dot()
        dash()
    if letter == "y":
        dash()
        dot()
        dash()
        dash()
    if letter == "z":
        dash()
        dash()
        dot()
        dot()

## Define Morse Program ##
def morseCode():
    word = textInput.get()
    for x in word.lower():
        display(x)

def close():
    RPi.GPIO.cleanup()
    win.destroy()

## Buttons for Pressing ##
startButton = Button(win, text = "Send", font = myFont, command = morseCode, bg = 'green', height = 1, width = 10)
startButton.grid(row=1,column=2)
exitButton = Button(win, text = "EXIT", font = myFont, command = close, bg = 'red', height = 1, width = 10)
exitButton.grid(row=3,column=2)

## Exit without Errors ##
win.protocol("WM_DELETE_WINDOW", close) #clean Exit

win.mainloop() #Looper
