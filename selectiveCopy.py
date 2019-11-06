#! pyhton3
# selectiveCopy.py - Copia archivos de un tipo de extension a un nuevo directorio

import os, sys, shutil, verifyPath, re

#Funcion que hace llamada a funciones
def main():
    folder = verifyPath.verify(getInput("Introduzca el directorio con los archivos: ")) #Obtiene la ruta a analizar
    
    validPath = regex(folder) #Guarda un bool si la ruta es valida

    checkPath

    allFiles = walkthrough(folder) #Trae todos los archivos en la ruta especificada

    specificFiles = checkExtension(allFiles) #Trae todos los archivos con una extension en especifico


    newFolder = getInput("Introduzca el nombre del nuevo directorio. Si desea que sea en una ya existente,\nintroduzca su nombre: ")

    newPath = getInput("Introduzca la ruta donde desea guardar el folder")

    path = getInput("Introduzca la ruta del nuevo directorio: ") #Solicita un ruta para guardar los archivos

    path = checkPath(path) #Verifica la ruta de guardado

    copyAllFiles(specificFiles, path) #Copia todos los archivos en un folder nuevo
    
#Funcion que lee lo ingresado por el usuario
def getInput(msg):
    try:
        var = input(msg)
        return var
    except KeyboardInterrupt:
        print("Se ha detenido el programa")

#Funcion que identifica todos los archivos de un directorio
def walkthrough(path):
    try:
        files = []
        
        for folderName, subFolder, filenames in os.walk(path):
            for filename in filenames:
                files += [folderName + "\\" + filename]

        return files
    except Exception as exc:
        print("Ha ocurrido un error: " + str(exc))
        sys.exit()

#Funcion que verifica las extension especifica
def checkExtension(files):
    allFiles = []
    for file in files:
        if file.endswith(".pdf"):
            allFiles += [file]
        else:
            continue
    return allFiles

#Funcion verifica el path
def checkPath(path):
    try:
        if not os.path.isabs(path):
            path = os.path.abspath(path)
            if not os.path.exists(path):
                path = os.makedirs(path)
            else:
                print("El directorio ya existe")
        elif os.path.isabs(path):
            if not os.path.exists(path):
                path = os.makedirs(path)
            else:
                print("El directorio ya existe")
        else:
            print("Introduzca una ruta valida")

        return path
    except Exception as exc:
        print("Ha ocurrido un error de tipo: " + str(exc))
        sys.exit()


def copyAllFiles(filenames, path):
    try:
        for filename in filenames:
            if os.path.exists(path + "\\" + filename):
                print("Hello")
            else:
                print(path + "\\" + filename)
                print("Copiando")
                copyFile(filename, path)

        print("It's OKEY!")
    except Exception as exc:
        print("Ha ocurrido un error: " + str(exc))
        sys.exit()

def copyFile(sourFile, destPath):
    try:
        shutil.copy(sourFile, destPath)
    except Exception as exc:
        print("Ha ocurrido un error " + str(exc))
        sys.exit()

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
