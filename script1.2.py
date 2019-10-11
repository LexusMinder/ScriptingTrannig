#!/usr/bin/python3
from pprint import pprint
import requests
import json

data = requests.post("http://35.190.155.168/aed387a36c/login", data = {'username':'admin','password':'admin'})

print(data.status_code)

print(len(data.text))

#print(data.headers['Content-Length'])