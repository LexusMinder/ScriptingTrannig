#! python3
# runes.py - Script que a traves de la utilidad Ejecutar verifica las runas o el rango de un invocador

import pyperclip, webbrowser, sys

#Variables Globales
champList = []

#Llamadas a funciones
def main():
    if len(sys.argv) > 1:
        global champList
        option = sys.argv[1]
        champList = sanitaze(openFile())
        print(champList)
        #verifyOption(option)
    else:
        print("Usage rS [nombre de invocador|nombre de campeon]")
        sys.exit()

#Funcion que guarda el contenido de un archivo en una variable       
def openFile():
    try:
        file = open("list.txt","r") #Abre el archivo con la lista de campeones
        content = file.readlines()
        file.close

        return content
    except FileNotFoundError:
        print("No se ha encontrado el archivo")
    
#Funcion que abre el navegador dependiendo si es campeon o invocador
def verifyOption(name):
    try:
        name = name[0].upper() + name[1:]
        act = True
        for champ in champList:
            if name in champ:
                act = False
                webbrowser.open("https://lan.op.gg/champion/" + name)
                break
        if act == True:
            webbrowser.open("https://lan.op.gg/summoner/userName=" + name)
    except Exception as exc:
        print("Ha ocurrido un excepcion de tipo: " + str(exc))

def sanitaze(array):
    try: 
        for i in range(len(array)):
            array[i] = array[i].strip("\n")
        
        return array
    except Exception as exc:
        print("Ha ocurrido un error de tipo: " + str(exc))

if __name__ == "__main__":
    main()
