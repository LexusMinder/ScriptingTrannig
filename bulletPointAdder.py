#! python3
# bulletPointAdder.py - Adds classroom bullet points to start
# of each line of text on the clipboard

import pyperclip
text = pyperclip.paste()

#Separate lines and add starts.
lines = text.split("\r\n")
for i in range(len(lines)): #loop through all indexes for "lines" list
    lines[i] = "* " + lines[i]

text = "\r\n".join(lines)
pyperclip.copy(text)
    

