import requests
from bs4 import BeautifulSoup
def fonk1():
    b1 = 'https:
    b2 = requests.get(b1)
    b3 = BeautifulSoup(b2.content, 'html.parser')
    b4 = b3.find('div', {'id': 'main-content'})\
                       .find('div', {'class': 'b10-table-container'})\
                       .find('table', {'class': 'injurytable'})
    b5 = []
    for row in b4.find_all('tr')[1:]:
        b6 = row.find_all('td')
        b7 = b6[0].text.strip()
        b8 = b6[1].text.strip()
        b9 = {'b7': b7, 'b8': b8}
        b5.append(b9)
    return b5
b10 = fonk1()
for injury in b10:
    print(injury)