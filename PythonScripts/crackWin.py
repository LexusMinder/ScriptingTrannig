#! python3

import string, hashlib

"""
Reglas de passwords:
1) Segundo nombre del Empleado con la primera letra en mayuscula0
2) Primer apellido del empleado con la primera letra en mayuscula
3) Tres numeros
4) Un caracter especial
"""


def makePassword(first, second):
    fst = first.title()
    snd = second.title()

    for a in string.digits:
        for b in string.digits:
            for c in string.digits:
                for d in string.punctuation:
                    password = str(fst + snd + a + b + c + d)
                    file = open("passwordlist.txt", "a")
                    file.write(password + "\n")
                    file.close()

#A traves de un nombre completo genera una password list

fullName = input("Ingrese el nombre COMPLETO del usuario: ")

fullName = fullName.strip()

parts = fullName.split()

if len(parts) == 4:
    firstPart = parts[1] #Obtiene el segundo nombre
    secondPart = parts[2] #Obtiene el primer apellido
elif len(fullNameArr) == 3:
    firstPart = parts[0] #Obtiene el primer nombre dado que no tiene dos
    secondPart = parts[1] #Obtiene el primer apellido
else:
    print("Nombre no valido")

makePassword(firstPart, secondPart)
