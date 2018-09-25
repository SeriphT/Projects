#imports
from tkinter import *
from tkinter import ttk
from tkinter import font
import time
import calendar
import datetime
import os
import winsound

#defining clock counting
def Clock():

    seconds = calendar.timegm(time.gmtime())
    current_second = seconds % 60
    minutes = seconds // 60
    current_minute = minutes % 60
    hours = minutes // 60
    current_hour = hours % 24

    #set time zone
    current_hour = current_hour - 6
    #define AM and PM tags
    if current_hour >= 12:
        tag = "PM"
    else:
        tag = "AM"

    #format output
    timex = str(current_hour)+":"+str(current_minute)+":"+str(current_second)+(tag)
    #return output
    return timex

def quit(*args):
    root.destroy()
def showTime():
    time = Clock()
    #show time
    txt.set(time)
    #trigger tick after 1000ms
    root.after(1000, showTime)

#use tkinter lib for showing the clock
root = Tk()
root.attributes("-fullscreen",False)
root.configure(background = "Black")
root.bind("x", quit)
root.after(1000, showTime)

fnt = font.Font(family ='Helvetica', size=60, weight = "bold")
txt = StringVar()
lbl = ttk.Label(root, textvariable = txt, font = fnt, foreground = "White", background = "Black")
lbl.place(relx = 0.5, rely =0.5, anchor = CENTER)
    
root.mainloop()


