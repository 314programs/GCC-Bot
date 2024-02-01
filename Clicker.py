import pyautogui
import keyboard
import time
import Quartz.CoreGraphics as CG


pyautogui.PAUSE = 0  # No delay after each PyAutoGUI call
def click(x, y):
    pyautogui.moveTo(x, y, duration=0.0)  # Move instantly
    pyautogui.mouseDown()
    pyautogui.mouseUp()

while not keyboard.is_pressed('q'):
    screenshot = pyautogui.screenshot()
    for i in range(0, 1512*2, 5):
        for j in range(0, 982*2, 5):
            if screenshot.getpixel((i, j))[0] >= 224 and screenshot.getpixel((i, j))[0] <= 230:
                if screenshot.getpixel((i, j))[1] >= 208 and screenshot.getpixel((i, j))[1] <= 214:
                    if screenshot.getpixel((i, j))[2] >= 138 and screenshot.getpixel((i, j))[2] <= 142:
                        i += 10
                        click(i/2, j/2)


    
