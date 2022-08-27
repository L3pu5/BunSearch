# 
# BunSearch: Bunny intel Searching.
#      https://github.com/L3pu5/BunSearch
#      By L3pu5, L3pu5_Hare, Lepus Hare.

import sys
import webbrowser
import urllib.request

_browser = webbrowser.get()
_pages = ["https://www.talosintelligence.com/reputation_center/lookup?search=",
          "https://mxtoolbox.com/SuperTool.aspx?action=blacklist:",
          "https://www.virustotal.com/gui/search/",
          "https://www.abuseipdb.com/check/",
          ]

if __name__ == "__main__":
    if sys.argv[1].lower() == "update":
        urlHaus = urllib.request.urlopen("https://urlhaus.abuse.ch/downloads/text/")
        urlHausFile = open("./urlHaus.txt", "w")
        urlHausFile.write(urlHaus.read().decode(urlHaus.headers.get_content_charset('utf-8')))
        urlHausFile.flush()
        urlHausFile.close()
        print("Updated!\n")
        exit()
    else:
        print("Have you updated your urlHaus today?\n")
    
    if sys.argv[1].lower() == "help" or sys.argv[1].lower() == "-help" or sys.argv[1].lower() == "--help" or sys.argv[1].lower() == "-h":
        print("Usage: bunsearch.py <IP>\n")
        print("       bunsearch.py UPDATE\n")
        exit()

    for page in _pages:
        _browser.open(page + sys.argv[1], new=1)
    
    urlHausFile = open("./urlHaus.txt")
    lines = urlHausFile.readlines()
    clean_haus = False
    for line in lines:
        if sys.argv[1] in line:
            print("[!]: URL in URLHAUS LIST\n")
            print(line)
            print("\n")
            clean_haus = TRUE
            break

    if not clean_haus:
        print("[+]: URL NOT IN URLHAUS\n")