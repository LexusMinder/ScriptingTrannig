def bacon():
    global eggs
    eggs = "spam"

eggs = "global"
bacon()
print(eggs)
