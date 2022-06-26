# 
# BunSearch: Bunny intel Searching.
#      https://github.com/L3pu5/BunSearch
#      By L3pu5, L3pu5_Hare, Lepus Hare.

import sys
import webbrowser
_browser = webbrowser.get()
_pages = ["https://www.talosintelligence.com/reputation_center/lookup?search=",
          "https://mxtoolbox.com/SuperTool.aspx?action=a%3a",
          "https://www.virustotal.com/gui/search/",
          ]

if __name__ == "__main__":
    for page in _pages:
        _browser.open(page + sys.argv[1], new=1)
