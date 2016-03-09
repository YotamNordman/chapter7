import os,time
def run(**args):
    files = os.listdir(".")
    time.sleep(25)
    return str(files)
run()
