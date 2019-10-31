#! python3
# champsLol - Genera un archivo de texto con los campeones actuales de LOL

import requests, bs4


#Funcion principal
def main():
    #print("Hello World!")
    champions = getCurrentChamps()
    sanitazeChamp(champions)
 
def getCurrentChamps():
    champions = []
    
    res = requests.get("https://leagueoflegends.fandom.com/wiki/List_of_champions")
    res.raise_for_status()
    champsSoup = bs4.BeautifulSoup(res.text, features="html.parser")
    currentChamps = champsSoup.select("td > span[data-champion]")


    for i in range(len(currentChamps)):
        champions = champions + [currentChamps[i].getText()]

    return champions

def sanitazeChamp(array):
    sanArray = []
    for i in range(len(array)):
        sanArray += [array[i].split()]
        
        file = open("champs.txt", "a")
        file.write(sanArray[i][0] + "\n")
        file.close()
    
if __name__ == "__main__":
    main()
