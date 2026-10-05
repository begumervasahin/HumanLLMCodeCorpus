import requests
from bs4 import BeautifulSoup
from selenium import webdriver
def fonk1():
    b1 = 'https:
    b2 = webdriver.Chrome('chromedriver.exe')
    try:
        b2.get(b1)
        b3 = b2.page_source
        b4 = BeautifulSoup(b3, 'b3.parser')
        b5 = b4.find('div', class_='b7-table-container')
        b6 = b5.find_all('table', class_='injurytable')
        b7 = []
        for table in b6:
            b8 = table.find('tbody').find_all('tr')
            for row in b8[1:]:
                b9 = row.find_all('td')
                b10 = b9[0]['class'][0]
                b11 = b9[1].text.strip()
                b7.append({'b10': b10, 'b11': b11})
        return b7
    finally:
        b2.quit()
b12 = fonk1()
for injury in b12:
    print(injury)
    print('----------------------------------------------')