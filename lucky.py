#! python3
# lucky.py - Open several Google search results

import requests, sys, webbrowser, bs4

print("Googling...") #display text while downloading the Google page
res = requests.get("https://google.com/search?q=" + " ".join(sys.argv[1:]))
print(res.text)
res.raise_for_status()

#Retrive top search result links
soup = bs4.BeautifulSoup(res.text, features="html.parser")



#Open a browser tab for each result
linkElems = soup.select(".r a")
print(len(linkElems))
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    print("Work!")
    webbrowser.open("http://google.com" + linkElems[i].get("href"))
