# 
# BunSearch: Bunny intel Searching.
#      https://github.com/L3pu5/BunSearch
#      By L3pu5, L3pu5_Hare, Lepus Hare.

#IMPORTS

import sys
import webbrowser
import urllib.request
import base64
from os.path import exists

from tkinter import *

#DEFINITIONS
##SIZES
DEFAULT_BUTTON_WIDTH = 100
DEFAULT_BUTTON_HEIGHT = 50
DEFAULT_BUTTON_PADX = 10
DEFAULT_BUTTON_PADY = 10

##COLOURS (DARK, LIGHT)
DEFAULT_COLOUR_BACKGROUND   = ("#121212", "#FFFFFF")
DEFAULT_COLOUR_LEVEL1       = ("#212121", "#FFFFFF")

#(500, 500)
DEFAULT_COLOUR_DEFAULT_WIDGET       = ("#88f082", "#88f082")
DEFAULT_COLOUR_TARGETED_WIDGET      = ("#66bb6a", "#7986cb")
DEFAULT_COLOUR_ALTERNATE_WIDGET     = ("#673ab7", "#88f082")

DARK_MODE = 0
LIGHT_MODE = 1
GREEN_THEME = 0
#

#DEFAULTS
colourMode = DARK_MODE
colourTheme = GREEN_THEME

#Setup
_browser = webbrowser.get()

def open_in_browser(url):
    _browser.open(url, new=0, autoraise=False)

#ELEMENTS
root = Tk()
root.title("BunSearch GUI")
root.configure(background=DEFAULT_COLOUR_BACKGROUND[colourMode])
root.geometry("400x800")

#InputFrame
inputFrame = Frame(root, height=50)
inputFrame.configure(background=DEFAULT_COLOUR_LEVEL1[colourMode])
inputFrame.pack(fill='x')

#Label Widget
userInput = Entry(inputFrame, justif=CENTER, font=('Consolas', 20))
userInput.pack( pady=10, padx=20, fill='x')

#Frame
IPButtonFrame = Frame(root, width= (DEFAULT_BUTTON_WIDTH + 2*DEFAULT_BUTTON_PADX))
IPButtonFrame.configure(background=DEFAULT_COLOUR_LEVEL1[colourMode])
IPButtonFrame.pack(padx=10, pady=10, fill="both", expand=True, side=LEFT)

HashButtonFrame = Frame(root, width= (DEFAULT_BUTTON_WIDTH + 2*DEFAULT_BUTTON_PADX))
HashButtonFrame.configure(background=DEFAULT_COLOUR_LEVEL1[colourMode])
HashButtonFrame.pack(padx=10, pady=10, fill="both", expand=True)

#Buttons
IPButtons = []
HashButtons = []

#BUTTON LOGIC
def PlaceButtons(buttons):
    for i in range(len(buttons)):
        xLocation = DEFAULT_BUTTON_PADX
        yLocation = (DEFAULT_BUTTON_PADY) * (i+1) + ((i)* DEFAULT_BUTTON_HEIGHT)
        buttons[i].place(x=xLocation, y=yLocation, width=DEFAULT_BUTTON_WIDTH, height=DEFAULT_BUTTON_HEIGHT)

def contextHash():
    hashString = ""
    escapeHashString = ""
    if ":" in userInput.get():
        hashString = userInput.get().split(':')[1]
        escapeHashString = userInput.get().replace(':', '%3A')
    else:
        hashString = userInput.get()
        escapeHashString = userInput.get()
    return (hashString, escapeHashString)

#Buttons - IP/Link
#ANNON
urlScanButton = Button(IPButtonFrame, text="Url Scan")
urlScanButton.configure(bg=DEFAULT_COLOUR_DEFAULT_WIDGET[colourTheme])
urlScanButton.configure(command=lambda: open_in_browser("https://urlscan.io"))
IPButtons.append(urlScanButton)

#DIRECTED
ciscoTalosButton = Button(IPButtonFrame, text="Cisco Talos")
ciscoTalosButton.configure(bg=DEFAULT_COLOUR_ALTERNATE_WIDGET[colourTheme])
ciscoTalosButton.configure(command=lambda: open_in_browser("https://www.talosintelligence.com/reputation_center/lookup?search=" + userInput.get()))
IPButtons.append(ciscoTalosButton)

virusTotalButton = Button(IPButtonFrame, text="Virus Total")
virusTotalButton.configure(bg=DEFAULT_COLOUR_ALTERNATE_WIDGET[colourTheme])
virusTotalButton.configure(command=lambda: open_in_browser("https://www.virustotal.com/gui/search/" + userInput.get()))
IPButtons.append(virusTotalButton)

abuseIPButton = Button(IPButtonFrame, text="Abuse IP")
abuseIPButton.configure(bg=DEFAULT_COLOUR_ALTERNATE_WIDGET[colourTheme])
abuseIPButton.configure(command=lambda: open_in_browser("https://www.abuseipdb.com/check/" + userInput.get()))
IPButtons.append(abuseIPButton)

kasperskyButton = Button(IPButtonFrame, text="Kaspersky OpenTip")
kasperskyButton.configure(bg=DEFAULT_COLOUR_ALTERNATE_WIDGET[colourTheme])
kasperskyButton.configure(command=lambda: open_in_browser("https://opentip.kaspersky.com/" + userInput.get()))
IPButtons.append(kasperskyButton)

alientVaultButton = Button(IPButtonFrame, text="OTX AleinVault")
alientVaultButton.configure(bg=DEFAULT_COLOUR_ALTERNATE_WIDGET[colourTheme])
alientVaultButton.configure(command=lambda: open_in_browser("https://otx.alienvault.com/browse/global/indicators?include_inactive=0&sort=-modified&page=1&limit=10&q=" + userInput.get()))
IPButtons.append(alientVaultButton)
#HASH BUTTONS
#ANON
teamCYMRUButton = Button(HashButtonFrame, text="Team CYMRU")
teamCYMRUButton.configure(bg=DEFAULT_COLOUR_DEFAULT_WIDGET[colourTheme])
teamCYMRUButton.configure(command=lambda: open_in_browser("https://hash.cymru.com/"))
HashButtons.append(teamCYMRUButton)

talosHashButton = Button(HashButtonFrame, text="Cisco Talos")
talosHashButton.configure(bg=DEFAULT_COLOUR_DEFAULT_WIDGET[colourTheme])
talosHashButton.configure(command=lambda: open_in_browser("https://www.talosintelligence.com/talos_file_reputation/"))
HashButtons.append(talosHashButton)
#DIRECTED
metaDefenderButton = Button(HashButtonFrame, text="OPSWAT")
metaDefenderButton.configure(bg=DEFAULT_COLOUR_ALTERNATE_WIDGET[colourTheme])
metaDefenderButton.configure(command=lambda: open_in_browser("https://metadefender.opswat.com/results/file/" + contextHash()[0] + "/hash/overview"))
HashButtons.append(metaDefenderButton)

abuseBazaar = Button(HashButtonFrame, text="Abuse Bazaar")
abuseBazaar.configure(bg=DEFAULT_COLOUR_ALTERNATE_WIDGET[colourTheme])
abuseBazaar.configure(command=lambda: open_in_browser("https://bazaar.abuse.ch/browse.php?search=" + userInput.get()))
HashButtons.append(abuseBazaar)

virusTotalHashButton = Button(HashButtonFrame, text="Virus Total")
virusTotalHashButton.configure(bg=DEFAULT_COLOUR_ALTERNATE_WIDGET[colourTheme])
virusTotalHashButton.configure(command=lambda: open_in_browser("https://www.virustotal.com/gui/search/" + userInput.get()))
HashButtons.append(virusTotalHashButton)

alientVaultHashButton = Button(IPButtonFrame, text="OTX AleinVault")
alientVaultHashButton.configure(bg=DEFAULT_COLOUR_ALTERNATE_WIDGET[colourTheme])
alientVaultHashButton.configure(command=lambda: open_in_browser("https://otx.alienvault.com/indicator/file/" + userInput.get()))
HashButtons.append(alientVaultHashButton)

#https://otx.alienvault.com/browse/global/indicators?include_inactive=0&sort=-modified&page=1&limit=10&q=
#ciscoTalosButton.place(x=10, y=10, width=DEFAULT_BUTTON_WIDTH, height=DEFAULT_BUTTON_HEIGHT)
# Build Buttons
PlaceButtons(IPButtons)
PlaceButtons(HashButtons)


#Event Loop.
userInput.focus_set()
root.mainloop()

