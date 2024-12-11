import requests
from bs4 import BeautifulSoup
from selenium import webdriver
def fonk1():
    b1 = 'https:
    b2 = webdriver.Chrome('chromedriver.exe')
    b2.get(b1)
    b3 = b2.page_source
    b4 = BeautifulSoup(b3, 'b3.parser')
    b5 = b4.find('div', {'class': 'b8-table-container'})
    b6 = b5.find_all('h3')
    b7 = b5.find_all('table', {'class': 'injurytable'})
    b8 = []
    for table in b7:
        b9 = table.find('tbody').find_all('tr')
        for row in b9[1:]:
            b10 = row.find_all('td')
            b11 = b10[0].get('class')[0]
            b12 = b10[1].text
            b8.append({'b11': b11, 'b12': b12})
    b2.quit()
    return b8
b13 = fonk1()
for injury in b13:
    print(injury)
    print('----------------------------------------------')