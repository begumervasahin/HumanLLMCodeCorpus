import requests
from bs4 import BeautifulSoup
from selenium import webdriver
def fonk1():
    b1 = webdriver.Chrome('chromedriver.exe')
    b2 = 'http:
    b3 = 'gerbun.htm'
    b1.get(b2+b3)
    b4 = b1.page_source
    b5 = BeautifulSoup(b4, "b4.parser")
    b6 = b5.find_all("div", {"id": "main"})
    b7 = b6[0].find_all('h5')
    b8 = []
    for i in b7:
        b9 = i.text
        b1.get(b2+i.find("a").get("href"))
        b4 = b1.page_source
        b5 = BeautifulSoup(b4, "b4.parser")
        b6 = b5.find_all("div", {"id": "main"})
        b10 = b6[0].find_all('table')
        b11 = b10[0].find('tbody').find_all('tr')
        for i in range(1,len(b11)):
            b12 = []
            b13 = b11[i].find_all('td')
            try:
                if b13[1].text:
                    b12.append(b13[1].text)
                    b12.append(b13[2].text)
                    b12.append(b13[3].text)
                    b12.append(b9)
                    b8.append(b12)
            except:
                break
        '''for i in range(len(b8)):
            print(b8[i])
        '''
    return(b8)