from ctypes import *
from datetime import datetime
def run(**args):
    user32 = windll.user32
    kernel32 = windll.kernel32
    psapi = windll.psapi
    def get_current_process():
        # get a handle to the foreground window
        hwnd = user32.GetForegroundWindow()
        # find the process ID
        pid = c_ulong(0)
        user32.GetWindowThreadProcessId(hwnd, byref(pid))
        # store the current process ID
        process_id = "%d" % pid.value
        # grab the executable
        executable = create_string_buffer("\x00" * 512)
        h_process = kernel32.OpenProcess(0x400 | 0x10, False, pid)
        psapi.GetModuleBaseNameA(h_process,None,byref(executable),512)
        # now read its title
        window_title = create_string_buffer("\x00" * 512)
        length = user32.GetWindowTextA(hwnd, byref(window_title),512)
        # print out the header if we're in the right process and close handle
        kernel32.CloseHandle(hwnd)
        kernel32.CloseHandle(h_process)
        return [process_id, executable.value, window_title.value]
    process_list = []
    counter = 0
    while (counter < 10):
        currentproc = get_current_process()
        process_data = ()
        process_start = str(datetime.now())
        process_end = None
        while(get_current_process() == currentproc):
            pass
        counter = counter +1
        process_end = str(datetime.now())
        process_data = (process_start,process_end,currentproc)
        process_list.append(process_data)
    return str(process_list)
