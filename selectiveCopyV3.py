#! python3
# selectiveCopyV3.py - Copia archivos de un tipo de extension a un nuevo folder,
# en la ruta especificada por el usuario


import sys, os, shutil, re

def main():
    folder = getInput("Introduce la ruta con los archivos: ") # Solicita un input
    path = checkPath(folder) # Verifica la ruta valida
    allFiles = walkthrough(path) # Entra en el folder y captura todos los archivos
    specificFiles = checkExtension(allFiles)# Busca en al arraglo anterior todos los archivos
    newFolder = getInput("Introduce la ruta de guardado: ") # Solicita la ruta de guardado
    savePath = checkPath(newFolder, True)
    copyAllFiles(specificFiles, path, savePath) #Copia todos los archivos en un folder nuevo

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

#Funcion que verifica que sea un ruta valida
def checkPath(path, act = False):
    try:
        path = path.strip()
        regex = re.compile(r"^[a-zA-Z]:\\[\\\S|*\S]?.*$")
        mo = regex.search(path)
        
        if not type(mo) == type(None):
            #Verifica si la ruta existe
            if not os.path.exists(path):
                if act == True:
                    os.makedirs(path)
                    print("[+] Se ha creado un nuevo folder en: " + path)
                    return path
                print("[+] Ruta no encontrada")
                sys.exit()
            else:
                #Verifica que sea un directorio
                if not os.path.isdir(path):
                    print("[+] La ruta no es un directorio. Introduzca un folder")
                    sys.exit()
                else:
                    print("[+] Ruta proporcianda: " + path)
                    return path
        else:
            print("[+] Ruta no valida")
            sys.exit()
    except Exception as exc:
        print("Ha ocurrido un error: " +  str(exc))
        sys.exit()

def copyAllFiles(filenames, path, savePath):
    try:
        for filename in filenames:
            if os.path.exists(savePath + "\\"+ os.path.basename(filename)):
                print("[+] El archivo ya ha sido copiado a este directiorio: " + filename)
            else:
                copyFile(filename, savePath)

        print("Se han copiado todo los archivos. Cerrando script.")
    except Exception as exc:
        print("Ha ocurrido un error: " + str(exc))
        sys.exit()

def copyFile(sourFile, destPath):
    try:
        shutil.copy(sourFile, destPath)
    except Exception as exc:
        print("Ha ocurrido un error " + str(exc))
        sys.exit()
        
if __name__ == "__main__":
    main()
