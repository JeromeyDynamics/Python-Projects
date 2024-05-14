import pyautogui
import time
import random
import keyboard

#needs to hold it for a bit
while keyboard.is_pressed('q') == False:
    x = random.randint(80, 1000)
    y = random.randint(80, 1720)
    pyautogui.moveTo(x, y, 0.5)
    time.sleep(2)