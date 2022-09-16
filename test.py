# Import Libraries
import pywhatkit
import pyautogui
from tkinter import *
import time

win = Tk() # Some Tkinter stuff
screen_width = win.winfo_screenwidth() # Gets the resolution (width) of your monitor
screen_height= win.winfo_screenheight() # Gets the resolution (height) of your monitor

print(screen_width, screen_height) # prints your monitor's resolution

pywhatkit.sendwhatmsg("+919693377045", "Happy Birthday 2022", 0, 10) # Sends the message
pyautogui.click() # Clicks the bar
time.sleep(20)
pyautogui.press('enter') # Sends the message