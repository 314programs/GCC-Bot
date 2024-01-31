import pyautogui
import keyboard
import time
import Quartz.CoreGraphics as CG


pyautogui.PAUSE = 0  # No delay after each PyAutoGUI call
def click(x, y):
    pyautogui.moveTo(x, y, duration=0.0)  # Move instantly
    pyautogui.mouseDown()
    pyautogui.mouseUp()

def get_pixel_color(x, y):
    region = CG.CGRectMake(x, y, 1, 1)
    context = CG.CGWindowListCreateImage(region, CG.kCGWindowListOptionOnScreenOnly, CG.kCGNullWindowID, CG.kCGWindowImageDefault)
    pixel_data = CG.CGDataProviderCopyData(CG.CGImageGetDataProvider(context))
    data = bytearray(pixel_data)
    
    # Pixels are stored as BGRA (Blue, Green, Red, Alpha)
    blue = data[0]
    green = data[1]
    red = data[2]
    alpha = data[3]  # You might not need alpha

    return (red, green, blue, alpha)

while not keyboard.is_pressed('q'):
    if get_pixel_color(400, 400)[0] == 0:
        click(400, 400)
    if get_pixel_color(500, 400)[0] == 0:
        click(500, 400)
    if get_pixel_color(600, 400)[0] == 0:
        click(600, 400)
    if get_pixel_color(690, 400)[0] == 0:
        click(690, 400)

