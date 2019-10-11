def spam():
    print(eggs) # Error
    eggs = "spam local"

eggs = "global"
spam()
