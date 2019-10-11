#! python3
# pw.py - An insecure password locker progam
import sys, pyperclip

PASSWORDS = {"email":"password123!",
             "blog":"mypassword",
             "luggage":"imissyou"}

if len(sys.argv) < 2:
    print("Usage: python pw.py [account] - copy account password")
    sys.exit()

account = sys.argv[1] # First command line arg is the account name


if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("Password for " + account + " copied to clipboard")
else:
    print("There is not account named " + account)

