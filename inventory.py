# inventory.py
import pprint

stuff = {"rope":1,"torch":34,"gold coin":12,"sword":1,"arrow":34}

def displayInventory(inventory):
    print("Inventory: ")
    itemTotal = 0
    for k, v in inventory.items():
        itemTotal += inventory.get(k, 0)
        print(k + " : " + str(inventory[k]))
    print("Total number of items: " + str(itemTotal))

displayInventory(stuff)
