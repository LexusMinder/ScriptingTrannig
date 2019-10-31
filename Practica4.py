#! pyhton3
# Author: lexus
# Practica4.py - El siguiente script lee un archivo con hashes y comprueba si son
# archivos malignos

import sys, os, pyperclip, requests, pprint, hashesDatabase, time

#Global variables
APIKEY = "911e79223df6364c1f676f0cdfd68cc2ae0832cbf77d413af039754fcefe2ab4"
maliciousHashes = []

#Save the typed for the users
def getInput(ban):
    try: 
        var = input(ban)
        return var
    except KeyboardInterrupt:
        print("Se ha detenido la ejecucion del script.")
        sys.exit()

#Open the hashfile
def getHashes(file):   
    try:
        hashes = open(file)
        hashList = hashes.readlines()
        return hashList
    except FileNotFoundError:
        print("Archivo no encontrado, verfique la ruta. ")
        sys.exit()
        
#Print the hashes list and remove the new line space  
def printArray(array):
    try:
        for i in range(len(array)):
            if "\n" in array[i]:
                array[i] = array[i].strip()
        return array
    except IndexError:
        print("Ha ocurrido un error. Cerrando Programa.")
        sys.exit()
        
#Make a GET resquest to the API of the VirusTotal
def fileReport(resource):
    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    params = {"apikey":APIKEY, "resource":resource}
    response = requests.get(url,params)
    return response.json()

#Save the hashes in a python hashesDatabase.py
def saveHashes(hashArray, opt = 0):
    db = []
    if opt == 1: #Made the databases with the current hashes
        fileObj = open("hashesDatabase.py", "w")
        fileObj.write("hashes = " + pprint.pformat(hashArray) + "\nact = True")
        fileObj.close()
        return False

    if (hashesDatabase.act == False):
        for i in range(len(hashArray)):
            element = {"id":i,"hash":hashArray[i],"check":False}
            db.append(element)
        fileObj = open("hashesDatabase.py", "w")
        fileObj.write("hashes = " + pprint.pformat(db) + "\nact = False")
        fileObj.close()
    else:
        db = hashesDatabase.hashes
        return db
    
#Save the output in a file
def saveOutput(result):
    dict1 = result
    if str(dict1["response_code"]) == str(1):
        print(" : FOUND")
        results = open("Results.txt", "a")
        results.write(pprint.pformat(result) + "\n\n")
        results.close()
        file = open("MaliciousHashes.txt","a")
        file.write(dict1["resource"]+"\n")
        file.close()
        return False
    print(" : NOT FOUND")

#made four request every minute
def madeResquests(dbHash):
    try:
        cont = 0
        for i in range(len(dbHash)):
            if dbHash[i]["check"] == False:
                print("[+] Request " + str(cont +1) + " : " + dbHash[i]["hash"], end="")
                saveOutput(fileReport(dbHash[i]["hash"]))
                dbHash[i]["check"] = True
                cont += 1
                time.sleep(15)
            else:
                continue
        saveHashes(dbHash,1)
    except KeyboardInterrupt:
        saveHashes(dbHash, 1)
        print("Se ha cerrado el progoma. Los cambios hasta aqui han sido guardados")
        sys.exit()   

#Print current malicious hashes
def printMaliciousHashes():
    try:
        global maliciousHashes
        count = 0
        file = open("MaliciousHashes.txt", "r")
        maliciousHashes = file.readline()
        file.close()
        print("Found Hashes: " + str(len(maliciousHashes)))
        for i in range(len(maliciousHashes)):
            print("[" + str(i + 1) +"] Hash: " + maliciousHashes[i])
            count += 1
        sys.exit()
    except FileNotFoundError:
        print("Archivo no encontrado, verfique la ruta.")
        sys.exit()    
        
#Retrive the path typed by the user
namefile = getInput("Selecione la ruta del archivo a leer > ") 

#Read the file hashes and save in the a variable
hashesList = getHashes(namefile)

#Remove the new lines in a array
clrHashesList = printArray(hashesList)

#Save array of hashes in a database
databaseHashes = saveHashes(clrHashesList, 0)

#Made 4 requests
madeResquests(databaseHashes)

#Print all hashes
printMaliciousHashes()
