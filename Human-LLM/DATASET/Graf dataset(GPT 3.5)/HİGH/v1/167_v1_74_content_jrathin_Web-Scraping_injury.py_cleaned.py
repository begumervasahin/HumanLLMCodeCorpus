import requests
from bs4 import BeautifulSoup
from selenium import webdriver
def fonk1():
    b1 = 'https:
    b2 = requests.get(b1)
    b3 = BeautifulSoup(b2.content, 'html.parser')
    b4 = b3.find('div', {'id': 'main-content'}).find('div', {'class': 'b9-table-container'}).find('table', {'class': 'injurytable'})
    b5 = []
    for row in b4.find_all('tr')[1:]:
        b6 = row.find_all('td')
        b7 = b6[0].text.strip()
        b8 = b6[1].text.strip()
        b5.append({'b7': b7, 'b8': b8})
    return b5
b9 = fonk1()
for injury in b9:
    print(injury)