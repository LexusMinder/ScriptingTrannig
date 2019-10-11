allGuests = {"Julio":{"mangos":3,"peras":4},
             "Aracely":{"tostadas":20,"tortillas":100},
             "Edgar":{"sandias":2,"peras":5},
             "Hector":{"mangos":5,"naranja":1}}
def totalTraido(guests, item):
    numTraido = 0
    for k, v in guests.items():
        numTraido += v.get(item, 0)

    return numTraido

print("Numero de cosas que fueron traidas: ")
print(" - Peras      " + str(totalTraido(allGuests, "peras")))
print(" - Naranja    " + str(totalTraido(allGuests, "naranja")))
print(" - Tostadas   " + str(totalTraido(allGuests, "tostadas")))
print(" - Mangos     " + str(totalTraido(allGuests, "mangos")))
print(" - Tortillas  " + str(totalTraido(allGuests, "tortillas")))
print(" - Sandias    " + str(totalTraido(allGuests, "sandias")))

