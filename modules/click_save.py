import pythoncom,pyHook
from datetime import datetime
click_list=[]
def run(**args):
    while len(click_list) < 10:
        pass
    return click_list
def onclick(event):
    if(len(click_list) > 10):
        hm.UnhookMouse()
        run()
    click_timer = str(datetime.now())
    x = (event.Position,click_timer)
    click_list.append(x)
    return True
hm = pyHook.HookManager()
hm.SubscribeMouseAllButtonsDown(onclick)
hm.HookMouse()
pythoncom.PumpMessages()
