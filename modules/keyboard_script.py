import pythoncom, pyHook ,ctypes,win32clipboard,win32api,win32con
import time,threading,os,stat,sys
def PressKey(hexKeyCode):
        extra = ctypes.c_ulong(0)
        ii_ = Input_I()
        ii_.ki = KeyBdInput( hexKeyCode, 0x48, 0, 0, ctypes.pointer(extra) )
        x = Input( ctypes.c_ulong(1), ii_ )
        SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
        extra = ctypes.c_ulong(0)
        ii_ = Input_I()
        ii_.ki = KeyBdInput( hexKeyCode, 0x48, 0x0002, 0, ctypes.pointer(extra) )
        x = Input( ctypes.c_ulong(1), ii_ )
        SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
def ClickLeftMouse(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
def ClickRightMouse(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)
def Lock_KeyBoard():
    def uMad(event):
        if write_status != os.stat(str(sys.argv[0]))[0]:
            return True
        else:
            return False
    hm = pyHook.HookManager()
    hm.KeyAll = uMad
    hm.HookKeyboard()
    pythoncom.PumpMessages()
def Change_To_Lock_Mode():
    t = threading.Thread(target=Lock_KeyBoard)
    t.start()
    Script_Line = fi.readline()
    while Script_Line.upper() != "END":
        if Script_Line[:2] == "//":
            pass
        elif Script_Line[:4].upper() == "TYPE":
            for c in Script_Line[5:len(Script_Line)-1]:
                os.chmod(str(sys.argv[0]), stat.S_IREAD)
                PressKey(Key_Dictionary[c])
                ReleaseKey(Key_Dictionary[c])
                os.chmod(str(sys.argv[0]), stat.S_IWRITE)
        elif Script_Line[:4].upper() == "LOCK":
            os.chmod(str(sys.argv[0]), stat.S_IREAD)
            return 0
        elif Script_Line[:5].upper() == "SLEEP":
            time.sleep(float(Script_Line[6:len(Script_Line)-1]))
        else:
            Script_Line = Script_Line.replace(" ", '')
            Script_Line = Script_Line[:len(Script_Line)-1]
            if '+' in Script_Line:
                parts = Script_Line.split("+")
            else:
                parts = [Script_Line]
            os.chmod(str(sys.argv[0]), stat.S_IREAD)
            for key in parts:
                PressKey(Key_Dictionary[key.upper()])
            for key in parts:
                ReleaseKey(Key_Dictionary[key.upper()])
            os.chmod(str(sys.argv[0]), stat.S_IWRITE)    
        Script_Line = fi.readline()
    fi.close()
    os.chmod(str(sys.argv[0]), stat.S_IREAD)
    os.remove("script.txt")
    return 1
def run(**args):
    global SendInput
    SendInput = ctypes.windll.user32.SendInput
    global PUL
    PUL = ctypes.POINTER(ctypes.c_ulong)
    global KeyBdInput
    class KeyBdInput(ctypes.Structure):
            _fields_ = [("wVk", ctypes.c_ushort),
            ("wScan", ctypes.c_ushort),
            ("dwFlags", ctypes.c_ulong),
            ("time", ctypes.c_ulong),
            ("dwExtraInfo", PUL)]
    global HardwareInput
    class HardwareInput(ctypes.Structure):
        _fields_ = [("uMsg", ctypes.c_ulong),
            ("wParamL", ctypes.c_short),
            ("wParamH", ctypes.c_ushort)]
    global MouseInput
    class MouseInput(ctypes.Structure):
        _fields_ = [("dx", ctypes.c_long),
            ("dy", ctypes.c_long),
            ("mouseData", ctypes.c_ulong),
            ("dwFlags", ctypes.c_ulong),
            ("time",ctypes.c_ulong),
            ("dwExtraInfo", PUL)]
    global Input_I
    class Input_I(ctypes.Union):
        _fields_ = [("ki", KeyBdInput),
            ("mi", MouseInput),
            ("hi", HardwareInput)]
    global Input
    class Input(ctypes.Structure):
        _fields_ = [("type", ctypes.c_ulong),
            ("ii", Input_I)]
    global Key_Dictionary
    Key_Dictionary ={
    "ESCAPE":27,"F1":112,
    "F2":113,"F3":114,"F4":115,"F5":116,
    "F6":117,"F7":118,"F8":119,"F9":120,
    "F10":121,"F11":122,"F12":123,"DELETE":46,
    "MEDIA_PLAY_PAUSE":179,"VOLUME_MUTE":173,"VOLUME_DOWN":174,"VOLUME_UP":175,
    "PRTSCN":44,"HOME":36,"END":35,"PAGEUP":33,
    "PAGEDOWN":34,"INSERT":45,"`":192,"~":192,
    "-":189,"_":189,"+":187,"=":187,"BACKSPACE":8,"TAB":9,
    "{":219,"[":219,"}":221,"]":221,
    "|":220,r"\\":220,"CAPS":20,";":186,
    ":":186,"'":222,r'"':222,"RETURN":13,"ENTER":13,
    "LSHIFT":160,",":188,"<":188,".":190,
    ">":190,"/":191,"?":191,"RSHIFT":161,"CONTROL":162,
    "LCONTROL":162,"RCONTROL":163,"LWIN":91,"RWIN":92,
    "ALT":18,"SPACE":32," ":32,"APPS":93,
    "LEFT":37,"UP":38,"RIGHT":39,"DOWN":40,
    "0":48,"1":49,"2":50,"3":51,"4":52,"5":53,"6":54,"7":55,"8":56,"9":57,
    "A":65,"B":66,"C":67,"D":68,"E":69,"F":70,"G":71,"H":72,"I":73,"J":74,
    "K":75,"L":76,"M":77,"N":78,"O":79,"P":80,"Q":81,"R":82,"S":83,"T":84,
    "U":85,"V":86,"W":87,"X":88,"Y":89,"Z":90,
    "a":65,"b":66,"c":67,"d":68,"e":69,"f":70,"g":71,"h":72,"i":73,"j":74,
    "k":75,"l":76,"m":77,"n":78,"o":79,"p":80,"q":81,"r":82,"s":83,"t":84,
    "u":85,"v":86,"w":87,"x":88,"y":89,"z":90,"/n":13
    
    }
    global Lock_Key_To_Press
    Lock_Key_To_Press = ""
    os.chmod(str(sys.argv[0]), stat.S_IWRITE)
    global write_status
    write_status = os.stat(str(sys.argv[0]))[0]
    try:
        global fi
        fi = open("script.txt", "r+")
    except:
        return "No Script File"
    global Script_Line
    Script_Line = fi.readline()
    while Script_Line != "END":
        if Script_Line[:2] == "//":
            pass 
        elif Script_Line[:4].upper() == "TYPE":
            for c in Script_Line[5:len(Script_Line)-1]:
                PressKey(Key_Dictionary[c])
                ReleaseKey(Key_Dictionary[c])
        elif Script_Line[:4].upper() == "LOCK":
            print "[*]Change To Lock Mode"
            is_done =Change_To_Lock_Mode()
            if(is_done):
                return "Script executed"
        elif Script_Line[:5].upper() == "SLEEP":
            time.sleep(float(Script_Line[6:len(Script_Line)-1]))
        else:
            Script_Line = Script_Line.replace(" ", '')
            Script_Line = Script_Line[:len(Script_Line)-1]
            if '+' in Script_Line:
                parts = Script_Line.split("+")
            else:
                parts = [Script_Line]
            for key in parts:
                PressKey(Key_Dictionary[key.upper()])
            for key in parts:
                ReleaseKey(Key_Dictionary[key.upper()])
        Script_Line = fi.readline()
    fi.close()
    os.remove("script.txt")
    return
run()
