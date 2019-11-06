#! python3
# madLibs.py -

import sys, re

def inputVerify(banner):
    try:
        var = input(banner)
        return var
    except KeyboardInterrupt:
        print("Script stopped")
        sys.exit()
    
def readFile(path):
    try:
        file = open(path,"r")
        text = file.read()
        file.close()
        return text
    except FileNotFoundError:
        print("File not found. Verify the path")
        sys.exit()

def createFile(content):
    contentNo = " ".join(content)
    file = open("bacon2.txt", "w")
    file.write(contentNo)
    file.close

def replaceWord(textNo):
    text = textNo.split()
    var = None
    for i in range(len(text)):
        if "ADJECTIVE" == text[i]:
            var = inputVerify("Enter an adjective: ")
            text[i] = var
        elif "NOUN" == text[i]:
            var = inputVerify("Enter a noun: ")
            text[i] = var
        elif "VERB" == text[i]:
            var = inputVerify("Enter a verb: ")
            
    if var == None:
            print("Dont keywords found")

    return text

text = readFile(inputVerify("Introduce the text filename > "))

newText = replaceWord(text)

createFile(newText)



