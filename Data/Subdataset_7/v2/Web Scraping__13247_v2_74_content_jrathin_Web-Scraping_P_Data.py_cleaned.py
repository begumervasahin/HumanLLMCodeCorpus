import requests
from bs4 import BeautifulSoup
from selenium import webdriver
def fonk1():
    b1 = webdriver.Chrome('chromedriver.exe')
    b2 = 'http:
    b3 = 'gerbun.htm'
    b1.get(b2 + b3)
    b4 = b1.page_source
    b5 = BeautifulSoup(b4, "html.parser")
    b6 = b5.find_all("div", {"id": "main"})
    b7 = b6[0].find_all('h5')
    b8 = []
    for team_heading in b7:
        b9 = team_heading.text
        b10 = b2 + team_heading.find("a").get("href")
        b1.get(b10)
        b11 = b1.page_source
        b12 = BeautifulSoup(b11, "html.parser")
        b13 = b12.find_all("div", {"id": "main"})
        b14 = b13[0].find_all('table')
        b15 = b14[0].find('tbody').find_all('tr')
        for player_row in b15[1:]:
            b16 = []
            b17 = player_row.find_all('td')
            try:
                if b17[1].text:
                    b16.append(b17[1].text)
                    b16.append(b17[2].text)
                    b16.append(b17[3].text)
                    b16.append(b9)
                    b8.append(b16)
            except:
                break
    b1.quit()
    return b8
b8 = fonk1()
for b16 in b8:
    print(b16)