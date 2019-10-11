#! python3
#Author: lexus
#Name: dirMachineCreator.py

import pyperclip, os, sys

#Verify if the path exists
def checkExist(path):
    if os.path.exists(path):
        return True
    else:
        return False
    
def makeDir(path, name):
    rootPath = path[0]
    newDir = rootPath + "\\Pentesting\\" + name
    try:
        os.makedirs(newDir)
        return newDir
    
    except FileExistsError:
        print("\n[+] El directorio ya fue creado")
        return newDir
    
    except KeyboardInterrupt:
        print("Se ha interrumpido la ejecucion del script")
        sys.exit()


def getInput(ins):
    try:
        name = input(ins)
        return name
    
    except KeyboardInterrupt:
        print("Se ha interrumpido la ejecucion del script")
        sys.exit()

print("DirMachineCreator.py\n")

name = getInput("Introduce el nombre la maquina activa: ")

cwd = os.getcwd()

dirParts = cwd.split(os.path.sep) # The current directory parts

newDir = makeDir(dirParts, name)

print("\n" + "Feed")
print("El nombre de la maquina es: " + name.ljust(30))
print("Directorio Actual:          " + cwd.ljust(30))
print("Directorio Maquina:         " + newDir.ljust(30))
