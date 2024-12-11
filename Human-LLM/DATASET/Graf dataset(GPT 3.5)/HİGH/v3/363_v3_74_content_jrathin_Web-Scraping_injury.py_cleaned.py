import requests
from bs4 import BeautifulSoup
def fonk1():
    b1 = 'https:
    b2 = requests.get(b1)
    b3 = BeautifulSoup(b2.content, 'html.parser')
    b4 = b3.find('div', {'id': 'main-content'})\
                       .find('div', {'class': 'b5-table-container'})\
                       .find('table', {'class': 'injurytable'})
    b5 = []
    for row in b4.find_all('tr')[1:]:
        b6 = row.find('td').text.strip()
        b7 = row.find_all('td')[1].text.strip()
        b8 = {'b6': b6, 'b7': b7}
        b5.append(b8)
    return b5
b5 = fonk1()
for injury in b5:
    print(injury)