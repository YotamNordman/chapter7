import os,time
def run(**args):
    time.sleep(25)
    files = os.listdir(".")

    return str(files)
run()
