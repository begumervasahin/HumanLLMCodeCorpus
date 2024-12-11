import urllib.b4
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random
class class1:
    def fonk1(self):
        self.b1 = UserAgent()
        self.b2 = []
    def fonk2(self):
        b3 = 'https:
        b4 = urllib.b4.Request(b3, headers={'User-Agent': self.b1.random})
        b5 = urllib.b4.urlopen(b4)
        b6 = BeautifulSoup(b5, 'html.parser')
        b7 = b6.find(id='proxylisttable')
        for row in b7.tbody.find_all('tr'):
            b8 = row.find_all('td')[0].string
            b9 = row.find_all('td')[1].string
            self.b2.append({'b8': b8, 'b9': b9})
    def fonk3(self):
        return random.choice(self.b2)
def fonk4():
    b10 = class1()
    b10.fonk2()
    for request_number in range(1, 100):
        b11 = b10.fonk3()
        b12 = urllib.b4.Request('https:
        b12.set_proxy(b11['b8'] + ':' + b11['b9'], 'http')
        try:
            with urllib.b4.urlopen(b12) as b5:
                b13 = b5.read().decode('utf8')
                print('My IP:', b13)
        except urllib.error.URLError:
            b10.b2.remove(b11)
            print(f'Proxy {b11["b8"]}:{b11["b9"]} deleted.')
if b14 = = '__main__':
    fonk4()