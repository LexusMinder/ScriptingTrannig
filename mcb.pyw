#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard
# Usage; python mcb.pyw save <keyword> - Saves clipboard to keyword
#        python mcb.pyw <keyword> - Loads keyword to clipboard
#        python mbc.pyw list - Loads all keywords to clipboard
#        python mbc.pyw delete <keyword> - Delete a specific keyword
#        python mbc.pyw deletr - Delete all keywords

import shelve, pyperclip, sys

mcbShelf = shelve.open("mcb")

#Save clipboard content.
if len(sys.argv) == 3:
    if sys.argv[1].lower() == "save":
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == "delete":
        del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # List keywords and load content
    if sys.argv[1].lower() == "list":
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    elif sys.argv[1].lower() == "delete":
        mcbShelf.clear()
            
mcbShelf.close()

