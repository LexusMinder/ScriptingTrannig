#This program says hello and asks for my name

print("Hello world")
print("What is your name?")
myName = input() #Ask for my name
print("It's a good to meet you, " + myName)
print("The length of your name is: ")
print(len(myName))
print("What is your age?") #Ask for their age
myAge = input()
print("You will be " + str(int(myAge) + 1) + " in a year.")
