from github3 import login
import json,os
import base64
def connect_to_github():#log into github
    gh = login(username="haxxx42",password="yotam1709")#details for login
    repo = gh.repository("haxxx42","chapter7")#name of repository
    branch = repo.branch("master")#branch
    return gh,repo,branch#retrun the login info
def download_report(trojan_id):
    #connect to github and find a file in github
    if not os.path.exists(r'C:\Report\data\%s' % trojan_id):
        os.makedirs(r'C:\Report\data\%s' % trojan_id)
    #path = "data/%s/" % trojan_id
    gh,repo,branch = connect_to_github()#get the details and connect to github
    tree = branch.commit.commit.tree.recurse()#github command to get filename list
    for filename in tree.tree:#search for filename in files
        print filename.path
        if trojan_id in filename.path and "data" in filename.path and "data/%s" %trojan_id != filename.path :
            print "[*] Found file %s" % filename.path#notify me
            blob = repo.blob(filename._json_data['sha'])#download it
            path = (filename.path).replace("/",'\\')
            path = path[:len(path) - 5]
            path += ".txt"
            fo = open(r"C:\Report\%s" % path, "wb")
            file_content = blob.content
            #file_content = base64.b64decode(str(blob.content))
            fo.write(file_content.decode('base64').decode('base64'))
            fo.close()
        #now get the content decoded in base 64 and write it into a file
        #also remember to add /data directory
connect_to_github()
download_report("abc")
