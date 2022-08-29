# 
# BunSearch: Bunny intel Searching.
#      https://github.com/L3pu5/BunSearch
#      By L3pu5, L3pu5_Hare, Lepus Hare.

import sys
import webbrowser
import urllib.request
import base64
from os.path import exists

_browser = webbrowser.get()
_pagesIP = ["https://www.talosintelligence.com/reputation_center/lookup?search=",
          "https://mxtoolbox.com/SuperTool.aspx?action=blacklist:",
          "https://www.virustotal.com/gui/search/",
          "https://www.abuseipdb.com/check/",
          "https://opentip.kaspersky.com/",
          "https://otx.alienvault.com/browse/global/indicators?include_inactive=0&sort=-modified&page=1&limit=10&q="
          ]

_pagesHash = [ "https://bazaar.abuse.ch/browse.php?search=",
"https://www.virustotal.com/gui/search/",
"https://otx.alienvault.com/indicator/file/",]
#Context defines the information being searched.
# 0 - IP
# 1 - HASH 
context = 0 

#Context Functions
def contextIP():
    for page in _pagesIP:
        _browser.open(page + sys.argv[1], new=1)
    
    #special pages
    _browser.open("https://metadefender.opswat.com/results/ip/" + (base64.b64encode(bytearray(sys.argv[1], 'utf-8'))).decode('utf-8') + "/overview", new=1)

    if exists("urlHaus.txt"):
        urlHausFile = open("./urlHaus.txt")
        lines = urlHausFile.readlines()
        clean_haus = False
        for line in lines:
            if sys.argv[1] in line:
                print("[!]: URL in URLHAUS LIST\n")
                print(line)
                print("\n")
                clean_haus = True
                break

        if not clean_haus:
            print("[+]: URL NOT IN URLHAUS\n")
    else:
        print("No URLHaus. Use UPDATE to download.")



def contextHash():
    hashString = ""
    escapeHashString = ""
    if ":" in sys.argv[2]:
        hashString = sys.argv[2].split(':')[1]
        escapeHashString = sys.argv[2].replace(':', '%3A')
    else:
        hashString = sys.argv[2]
        escapeHashString = sys.argv[2]
    
    for page in _pagesHash:
        _browser.open(page + escapeHashString, new=1)
    _browser.open("https://metadefender.opswat.com/results/file/" + hashString + "/hash/overview", new=1)
    _browser.open("https://hash.cymru.com/", new=1)
    _browser.open("https://www.talosintelligence.com/talos_file_reputation", new=1)

    
def update():
    urlHaus = urllib.request.urlopen("https://urlhaus.abuse.ch/downloads/text/")
    urlHausFile = open("./urlHaus.txt", "w")
    urlHausFile.write(urlHaus.read().decode(urlHaus.headers.get_content_charset('utf-8')))
    urlHausFile.flush()
    urlHausFile.close()
    print("Updated!\n")



if __name__ == "__main__":
    if sys.argv[1].lower() == "update":
        update()
        exit()
    else:
        print("Have you updated your urlHaus today?\n")
    
    if sys.argv[1].lower() == "help" or sys.argv[1].lower() == "-help" or sys.argv[1].lower() == "--help" or sys.argv[1].lower() == "-h":
        print("Usage: bunsearch.py <IP>\n")
        print("       bunsearch.py UPDATE\n")
        exit()
    
    if sys.argv[1].lower() == "hash" or sys.argv[1].lower() == "-hash":
        context = 1


    if context == 0:
        contextIP()
    elif context == 1:
        contextHash()