import sys

def getNumber():
    print("Enter a number: ")
    try:
        number = int(input())
        return number
    except ValueError:
        print("You must be enter only numbers")
        sys.exit()
def collatz(number):
    while number != 1:
        if (number % 2) == 0:
            number = number // 2
            print(number)
        elif (number % 2) == 1:
            number = 3 * number + 1
            print(number)
        else:
            print("Error")
    return number

collatz(getNumber())
