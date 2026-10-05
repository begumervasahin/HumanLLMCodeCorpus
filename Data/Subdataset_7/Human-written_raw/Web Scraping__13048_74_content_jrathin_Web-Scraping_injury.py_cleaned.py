import requests
from bs4 import BeautifulSoup
from selenium import webdriver
def fonk1():
    b1 = 'https:
    b2 = webdriver.Chrome('chromedriver.exe')
    b2.get(b1)
    b3 = b2.page_source
    b4 = BeautifulSoup(b3, 'b3.parser')
    b5 = b4.find_all('div', {'id': 'main-content', 'class': 'col-md-9'})[0].find('div', {'class': 'injuries-table-container'}).find_all('h3')
    b6 = b4.find_all('div', {'id': 'main-content', 'class': 'col-md-9'})[0].find('div', {'class': 'injuries-table-container'}).find_all('table', {'class': 'injurytable'})
    b7 = []
    a1 = 0
    for eachTable in b6:
        b8 = eachTable.find('tbody').find_all('tr')
        b9 = {}
        b10 = []
        for eachTr in range(1, len(b8)):
            b11 = {}
            b12 = []
            b13 = b8[eachTr].find_all('td')
            b12.append(b13[0].get('class')[0])
            b12.append(b13[1].text)
            b7.append(b12)
    return(b7)
    '''for i in b7:
        print(i)
        print('\n----------------------------------------------\n')
fonk1()
'''