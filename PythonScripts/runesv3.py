#! python3
#runesv2.py

import pyperclip, webbrowser, sys

champList = []

#Main function
def main():
    if len(sys.argv) > 1:
        option = sys.argv[1]
        openFile()
        verifyOption(option)
    else:
        sys.exit()
        
def openFile():
    global champList
    file = open("list.txt","r")
    champList = file.readlines()
    file.close
    
def verifyOption(name):
    name = name[0].upper() + name[1:]

    act = True
    
    for champ in champList:
        if name in champ:
            act = False
            webbrowser.open("https://lan.op.gg/champion/" + name)
            break
    if act == True:
        webbrowser.open("https://lan.op.gg/summoner/userName=" + name)

if __name__ == "__main__":
    main()
