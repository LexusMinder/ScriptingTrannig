#! python3
# regexSearch - Search a regex in a text and return all matches

#import modules
import sys, re

#Main function
def main():
    filename = getInput("Introduce the text file > ") # get the file
    text = openFile(filename) # open the file
    regex = getInput("Introduce the regular expression > ")#get the regex expression
    macthes = matchRegex(text,regex) #Return all the matches
    printMatches(macthes) #Print matches

    sys.exit()


#Get the user input a return the input
def getInput(banner):
    try:
        var = input(banner)
        return var
    except KeyboardInterrupt:
        print("Script stopped")
        sys.exit()

#Read the text file and return the content
def openFile(filename):
    try:    
        file = open(filename,"r")
        fileread = file.read()
        file.close()

        return fileread
    except FileNotFoundError:
        print("File dont found.")
        sys.exit()

#Return all matches in a text
def matchRegex(content, regex):
    try:
        textRegex = re.compile(regex)
        matches = textRegex.findall(content)

        return matches
    except Exception as err:
        print("An error has occurred " + str(err))
    
#Print alll macthes with the regex introduced
def printMatches(matches):
    try:
        for i in range(len(matches)):
            print("Match " + str(1 + i) + " : " + " " + matches[i].rjust(5))
    except Exception as err:
        print("An error has courred " + str(err))

if __name__ == "__main__":
    main()
