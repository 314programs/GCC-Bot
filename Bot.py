from pyautogui import *
import pyautogui
import time
import keyboard
import random
import objc
from Quartz.CoreGraphics import (
    CGEventCreateMouseEvent, 
    kCGEventMouseMoved, 
    kCGEventLeftMouseDown, 
    kCGEventLeftMouseUp, 
    kCGMouseButtonLeft, 
    CGEventPost, 
    kCGHIDEventTap, 
    CGPointMake
)

def move_mouse(x, y):
    mouse_event = CGEventCreateMouseEvent(None, kCGEventMouseMoved, CGPointMake(x, y), kCGMouseButtonLeft)
    CGEventPost(kCGHIDEventTap, mouse_event)

def click(x, y):
    move_mouse(x, y)
    mouse_event_down = CGEventCreateMouseEvent(None, kCGEventLeftMouseDown, CGPointMake(x, y), kCGMouseButtonLeft)
    CGEventPost(kCGHIDEventTap, mouse_event_down)

    time.sleep(0.01)
    
    mouse_event_up = CGEventCreateMouseEvent(None, kCGEventLeftMouseUp, CGPointMake(x, y), kCGMouseButtonLeft)
    CGEventPost(kCGHIDEventTap, mouse_event_up)

while keyboard.is_pressed('q') == False:
    print(pyautogui.pixel(581, 400))
    if pyautogui.pixel(581, 400)[0] == 0:
        click(581, 400)
    if pyautogui.pixel(682, 400)[0] == 0:
        click(682, 400)
    if pyautogui.pixel(770, 400)[0] == 0:
        click(770, 400)
    if pyautogui.pixel(869, 400)[0] == 0:
        click(869, 400)
    time.sleep(5)
