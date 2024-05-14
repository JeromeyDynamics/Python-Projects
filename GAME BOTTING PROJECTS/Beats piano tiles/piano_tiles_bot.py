#use fullscreen on https://www.agame.com/game/magic-piano-tilesq    
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#Tile 1 Position: X:  969 Y:  964 RGB: (158, 162, 233)
#Tile 2 Position: X: 1174 Y: 1009 RGB: (221, 149, 128)
#Tile 3 Position: X: 1379 Y: 1045 RGB: (113, 117, 169)
#Tile 4 Position: X: 1579 Y: 1061 RGB: (  0,   0,   0)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1) #This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    
    if pyautogui.pixel(969, 1009)[0] == 0:
        click(969, 1009)
    if pyautogui.pixel(1174, 1009)[0] == 0:
        click(1174, 1009)
    if pyautogui.pixel(1379, 1009)[0] == 0:
        click(1379, 1009)
    if pyautogui.pixel(1579, 1009)[0] == 0:
        click(1579, 1009)
