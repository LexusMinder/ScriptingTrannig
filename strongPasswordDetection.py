#! python3
# strongPasswordDetection - Valida si un password es fuerte
import re

password = input("Introduzca un password: ")

especial = re.compile(r"(\s|\!|\"|\#|\$|\%|\&|\'|\(|\)|\*|\+|\,|\-|\.|\/|\:|\;|\<|\=|\>|\?|\@|\[|\\|\]|\^|\_|\`|\{|\||\}|\~)+")

digits = re.compile(r"(\d)+")

lenght = re.compile(r"(\w){8,}")

mo = especial.search(password)

mo1 = digits.search(password)

mo2 = lenght.search(password)


if mo2 == None:
    print("El password debe contener almenos ocho carecteres")
elif mo1 == None:
    print("El password debe contener almenos un numero")
elif mo == None:
    print("El password debe contener almenos un caracter especial")
else:
    print("El password es fuerte" + password)
    printTable()




""" 
if mo == None :
    print("El password debe contener almenos un caracter especial")
else:
    print("El password es " + password)

if mo1 == None :
    print("El password debe contener almenos un numero")
else:
    print("El password es " + password)
"""
