import sys

def printFunc(fruts):
    word = ""
    for i in range(len(fruts)):
        term = fruts[-1]
        if term != fruts[i]:
            word += fruts[i]
            word += ", "
        else:
            word = word + "and " + fruts[i]
    return word

def makeArray():
    fruts = []
    counter = 0
    while True:
        frut = str(input("Introduce the frut(" + str(counter + 1)
                         + "). For stop only type enter: "))
        if frut != "":
            fruts.append(frut)
            counter += 1 
        else:
            break
    return fruts

print(printFunc(makeArray()))
