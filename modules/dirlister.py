import os
def run(**args):
    files = os.listdir(".")
    return str(files)
run()
