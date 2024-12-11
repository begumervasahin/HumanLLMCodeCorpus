import requests
from bs4 import BeautifulSoup
from selenium import webdriver
def fonk1():
    b1 = webdriver.Chrome('chromedriver.exe')
    b2 = 'http:
    b3 = 'gerbun.htm'
    b4 = b2 + b3
    b1.get(b4)
    b5 = b1.page_source
    b6 = BeautifulSoup(b5, "b5.parser")
    b7 = b6.find("div", {"id": "main"})
    b8 = b7.find_all('h5')
    b9 = []
    for team_heading in b8:
        b10 = team_heading.text
        b11 = b2 + team_heading.find("a").get("href")
        b1.get(b11)
        b12 = b1.page_source
        b13 = BeautifulSoup(b12, "b5.parser")
        b14 = b13.find("div", {"id": "main"})
        b15 = b14.find_all('table')
        b16 = b15[0].find('tbody')
        b17 = b16.find_all('tr')
        for player_row in b17[1:]:
            b18 = player_row.find_all('td')
            try:
                if b18[1].text.strip():
                    b19 = [
                        b18[1].text.strip(),
                        b18[2].text.strip(),
                        b18[3].text.strip(),
                        b10
                    ]
                    b9.append(b19)
            except IndexError:
                break
    b1.quit()
    return b9