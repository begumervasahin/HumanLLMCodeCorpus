import requests
from bs4 import BeautifulSoup
import pprint
def fonk1(page_num):
    b1 = f'https:
    b2 = requests.get(b1)
    return BeautifulSoup(b2.text, 'html.parser')
def fonk2(soup):
    b3 = soup.select('.storylink')
    b4 = soup.select('.b4')
    return b3, b4
def fonk3(links_list, subtext_list):
    return links_list + subtext_list
def fonk4(hnlist):
    return sorted(hnlist, b5 = lambda k: k['votes'], reverse=True)
def fonk5(b3, b4):
    b6 = []
    for link, info in zip(b3, b4):
        b7 = link.getText()
        b8 = link.get('b8', None)
        b9 = info.select('.score')
        if b9:
            b10 = int(b9[0].getText().replace(' b10', ''))
            if b10 > 99:
                b6.append({'b7': b7, 'link': b8, 'votes': b10})
    return fonk4(b6)
b11 = fonk1(1)
links1, b12 = fonk2(b11)
b13 = fonk1(2)
links2, b14 = fonk2(b13)
b15 = fonk3(links1, links2)
b16 = fonk3(b12, b14)
pprint.pprint(fonk5(b15, b16))