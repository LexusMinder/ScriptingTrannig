#! python3

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    #Get Champion
    champ = sys.argv[1]

else:
    #Get champion  from the pyperclip
    champ = pyperclip.paste()
	
#ie = .get(webbrowser.iexplore)
webbrowser.open("https://lan.op.gg/champion/" + champ.lower())
