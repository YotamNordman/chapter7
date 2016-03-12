import win32gui
import win32ui
import win32api
import win32con
import time
import os
import ImageGrab
def run(**args):
    image = ImageGrab.grab()
    return str(image)
