#! pyhton3
# selectiveCopy.py - Copia archivos de un tipo de extension a un nuevo directorio

import os, sys, shutil, verifyPath, re

#Main funcion
def main():
    directory = getInput("Introduzca el directorio con los archivos: ")

    regex(directory)

#Funcion que lee lo ingresado por el usuario
def getInput(msg):
    try:
        var = input(msg)
        return var
    except KeyboardInterrupt:
        print("Se ha detenido el programa")

# Verifica que lo introducido sea una ruta con una regex
def regex(string):
    try:    
        regex = re.compile(r"^[A-Z]:\\(?:[^\\/:*?\"<>|\r\n]+\\)*[^\\/:*?\"<>|\r\n]*$")
        mo = re.search(string)

        if not mo.group() == NoneType:
            return True
        else:
            return False
    except Exception as exc:
        print("Ha ocurrido un error: " +  str(exc))
        sys.exit()

if __name__ == "__main__":
    main()
