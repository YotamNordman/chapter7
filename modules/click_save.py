import pythoncom,pyHook
from datetime import datetime
import os
import threading
def run(**args):
    fo = open("output.txt", "w")
    fo.close()
    t = threading.Thread(target=clicks,)
    t.start()
    while (os.stat("output.txt").st_size == 0):
        pass
    fi = open("output.txt", "r+")
    data = fi.read()
    fi.close()
    return data
def clicks(**args):
    click_list = []
    def onclick(event):
        if(len(click_list) == 10):
            hm.UnhookMouse()
            fo = open("output.txt", "w")
            fo.write(str(click_list))
            fo.close()
        click_timer = str(datetime.now())
        x = (event.Position,click_timer)
        click_list.append(x)
        return True
    hm = pyHook.HookManager()
    hm.SubscribeMouseAllButtonsDown(onclick)
    hm.HookMouse()
    pythoncom.PumpMessages()
