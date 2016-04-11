def run(**args):
    script_text=""\
    "//install python\n"\
    "LOCK\n"\
    "lock\n"\
    "LWIN\n"\
    "SLEEP 0.2\n"\
    "TYPE powershell\n"\
    "SLEEP 0.9\n"\
    "APPS\n"\
    "SLEEP 0.9\n"\
    "DOWN\n"\
    "SLEEP 0.9\n"\
    "ENTER\n"\
    "SLEEP 0.9\n"\
    "END"
    fo = open("script.txt","w+")
    fo.write(script_text)
    fo.close()
