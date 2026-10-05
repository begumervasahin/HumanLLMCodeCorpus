import requests
from bs4 import BeautifulSoup
import pprint
b1 = requests.get('https:
b2 = BeautifulSoup(b1.text, 'html.parser')
b3 = requests.get('https:
b4 = BeautifulSoup(b3.text, 'html.parser')
b5 = b2.select('.storylink')
b6 = b2.select('.b6')
b7 = b4.select('.storylink')
b8 = b4.select('.b6')
b9 = b5 + b7
b10 = b6 + b8
def fonk1(hnlist):
    return sorted(hnlist, b11 = lambda k: k['votes'], reverse=True)
def fonk2(b5, b6):
    b12 = []
    for idx, item in enumerate(b5):
        b13 = item.getText()
        b14 = item.get('b14', None)
        b15 = b6[idx].select('.score')
        if len(b15):
            b16 = int(b15[0].getText().replace(' b16', ''))
            if b16 > 99:
                b12.append({'b13': b13, 'link': b14, 'votes': b16})
    return fonk1(b12)
pprint.pprint(fonk2(b9, b10))