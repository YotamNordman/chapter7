import os,time
def run(**args):
    files = os.listdir(".")
    time.sleep(35)
    return str(files)
