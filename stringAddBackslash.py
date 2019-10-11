import pyperclip

string = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

stringList = []

for i in range(len(string)):
    stringList.append("|\\" + string[i])
    print(string[i])

for i in range(len(stringList)):
    print(stringList[i])
    string2 = "".join(stringList)

pyperclip.copy(string2)
