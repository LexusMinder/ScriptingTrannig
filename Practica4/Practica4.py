#! python3
# Practica4 - Analiza un archivo con hashes y luego comprueba cuales son malignos

import sys, requests, time

#Variables Globales
APIKEY = "911e79223df6364c1f676f0cdfd68cc2ae0832cbf77d413af039754fcefe2ab4"

#Funcion que hace llamada a otras funciones
def main():
    filename = getInput("Introduzca la ruta del archivo: ")
    hashes = sanitizeHashes(openFile(filename))
    mh = checkHashes(hashes)
    printHashes[mh]
    
    sys.exit()

#Funcion openFile
def openFile(filename):
    try:
        file = open(filename, "r") #Abre el archivo
        content = file.readlines()
        file.close()

        return content
    except FileNotFoundError:
        print("No se encontro el archivo")
        sys.exit()

#Funcion getInput
def getInput(msg):
    try:
        var = input(msg) #Lee lo que introduzca el usuario

        return var
    except KeyboardInterrupt:
        print("Se ha detenido el programa")
        sys.exit()

#Funcion que verifica los hashes en la pagina de virustotal
def checkHashes(hashes):
    maliciousHashes = [] #Lista para guardar los hashes malignos
    
    print("Cheking hashes...\n")
    try:
        for hashe in hashes:
            url = 'https://www.virustotal.com/vtapi/v2/file/report'
            params = {'apikey': APIKEY, 'resource': hashe}
            response = requests.get(url, params=params)
            print("[+] Hash: " + hashe + " : ", end="")
            if len(response.text) > 160:
                #hash maligno encontrado
                print("MALICIOUS")
                maliciousHashes = maliciousHashes + [hashe] #Añade el hash malicioso a una lista
            else:
                #hash limpio encotrado
                print("Clean")

            #print(len(response.text))
            time.sleep(15)

        return maliciousHashes
    except KeyboardInterrupt:
        print("Se ha detenido la ejecucion del programa")
    except Exception as exc:
        print("Ah ocurrido un error de tipo: " + str(exc))

#Funcion que limpia los hashes de carcateres no esperados
def sanitizeHashes(hashes):
    try:
        for i in range(len(hashes)):
            hashes[i] = hashes[i].strip("\n")
            
        return hashes
    except Exception as exc:
        print("Ah ocurrido un error de tipo: " + str(exc))
        sys.exit()

#Funcion que imprime hashes
def printHashes(hashes):
    try:
        for i in range(len(hashes)):
            print("[Malicious Hashes]")
            print("Found: " + str(len(hashes)))
            print("[" + str(i) + "] " + hashes[i])
    except Exception as exc:
        print("Ha ocurrido un excepcion de tipo: " + str(exc))

if __name__ == "__main__":
    main()
