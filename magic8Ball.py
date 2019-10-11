import random

def getAnswer(answer):
    if answer == 1:
        return "It's certain"
    elif answer == 2:
        return "It's decidedly so"
    elif answer == 3:
        return "Yes"
    elif answer == 4:
        return "Reply hazy try again"
    elif answer == 5:
        return "Ask me again later"
    elif answer == 6:
        return "Concetrate and ask again"
    elif answer == 7:
        return "Me reply is no"
    elif answer == 8:
        return "Outlook not so good"
    elif answer == 9:
        return "Very doubtful"

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)
