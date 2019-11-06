#! python3
# verifyPath.py - Hace validaciones a un ruta dada

import sys, os

#Hace validaciones a una ruta
#Verifica si la ruta principal existe
def verify(path):
    try:
        #Convierte las rutas relativas a abs
        if not os.path.isabs(path):
            path = os.path.abspath(path) # Relative to abs

        #Verifica si la ruta existe
        if not os.path.exists(path):
            print("[+] La ruta no es valida")
            sys.exit()
        else:
            print("[+] La ruta es valida")

        #Verifica que sea un directorio
        if not os.path.isdir(path):
            print("[+] La ruta no es un directorio")
            sys.exit()
        else:
            print("[+] Es un directorio")
            
        return path #Ruta valida
    
    except Exception as exc:
        print("Ha ocurrido un error de tipo : " + str(exc))
