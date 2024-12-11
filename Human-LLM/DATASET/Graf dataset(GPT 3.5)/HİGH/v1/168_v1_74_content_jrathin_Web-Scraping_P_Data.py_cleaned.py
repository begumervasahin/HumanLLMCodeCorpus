import requests
from bs4 import BeautifulSoup
from selenium import webdriver
def fonk1():
    b1 = webdriver.Chrome('chromedriver.exe')
    b2 = 'http:
    b3 = 'gerbun.htm'
    b1.get(b2 + b3)
    b4 = b1.page_source
    b5 = BeautifulSoup(b4, "b4.parser")
    b6 = b5.find_all("div", {"id": "main"})
    b7 = b6[0].find_all('h5')
    b8 = []
    for i in b7:
        b9 = i.text
        b10 = b2 + i.find("a").get("href")
        b1.get(b10)
        b4 = b1.page_source
        b5 = BeautifulSoup(b4, "b4.parser")
        b6 = b5.find_all("div", {"id": "main"})
        b11 = b6[0].find_all('table')
        b12 = b11[0].find('tbody').find_all('tr')
        for j in range(1, len(b12)):
            b13 = []
            b14 = b12[j].find_all('td')
            try:
                if b14[1].text:
                    b13.append(b14[1].text)
                    b13.append(b14[2].text)
                    b13.append(b14[3].text)
                    b13.append(b9)
                    b8.append(b13)
            except:
                break
    b1.quit()
    return b8
b15 = fonk1()
for player_info in b15:
    print(player_info)