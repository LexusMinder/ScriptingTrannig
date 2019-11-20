#! python3

import requests, sys, os, bs4

print("Introduce the URL: ", end="")

url = input()

res = requests.get(url)

res.raise_for_status()

webpage = bs4.BeautifulSoup(res.text, features="html.parser")

elemns = webpage.select("a")

links = []

cont = 0

lnf = 0

for elemn in elemns:
    var = dict(elemn.attrs)
    if "href" in var.keys():
        links += [var["href"]]
    else:
        continue
        
#print(str(cont) + " of " + str(len(elemns)))
for link in links:
    a = url.rstrip("/")
    if os.path.isabs(link):
        r = requests.get(a + link)
        print(a+link+ " : " + str(r.status_code))
        res.raise_for_status()
        if int(r.status_code) == 404:
            lnf = lnf + 1
            print("NOT FOUND [404]")
            print(a+link)
        elif int(r.status_code) == 403:
            continue
    elif "#" in link:
        continue
    else:
        r = requests.get(link)
        print(link+ " : " + str(r.status_code))
        res.raise_for_status()
        if int(r.status_code) == 404:
            lnf = lnf + 1
            print("NOT FOUND [404]")
            print(link)
        elif int(r.status_code) == 403:
            continue

if lnf > 0:
    print("Found dead links: " + str(lnf))
else:
    print("It doesnt found dead links")
