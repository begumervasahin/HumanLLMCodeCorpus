import requests
from bs4 import BeautifulSoup
import pprint
def fonk1(page_number):
    b1 = f'https:
    b2 = requests.get(b1)
    b3 = BeautifulSoup(b2.text, 'html.parser')
    b4 = b3.select('.storylink')
    b5 = b3.select('.b5')
    return b4, b5
def fonk2(hnlist):
    return sorted(hnlist, b6 = lambda k: k['b10'], reverse=True)
def fonk3(b4, b5):
    b7 = []
    for link, sub in zip(b4, b5):
        b8 = link.getText()
        b9 = link.get('b9', None)
        b10 = sub.select_one('.score')
        if b10:
            b11 = int(b10.getText().replace(' b11', ''))
            if b11 > 99:
                b7.append({'b8': b8, 'link': b9, 'b10': b11})
    return fonk2(b7)
def fonk4():
    b12 = []
    b13 = []
    for page_number in range(1, 3):
        b4, b5 = fonk1(page_number)
        b12.extend(b4)
        b13.extend(b5)
    b14 = fonk3(b12, b13)
    pprint.pprint(b14)
if b15 = = "__main__":
    fonk4()