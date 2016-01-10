import pythoncom,pyHook
from datetime import datetime
def run(**args):
    click_list=[]
    def onclick(event):
        if(len(click_list) > 100):
            hm.UnhookMouse()
            print click_list
        click_timer = str(datetime.now())
        x = (event.Position,click_timer)
        click_list.append(x)
        return True
    hm = pyHook.HookManager()
    hm.SubscribeMouseAllButtonsDown(onclick)
    hm.HookMouse()
    pythoncom.PumpMessages()
    hm.UnhookMouse()
    return click_list
