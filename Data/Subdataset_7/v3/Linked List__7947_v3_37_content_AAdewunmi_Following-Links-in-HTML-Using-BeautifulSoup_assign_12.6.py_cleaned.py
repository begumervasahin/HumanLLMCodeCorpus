import urllib.request
from bs4 import BeautifulSoup
import ssl
def fonk1():
    b1 = input('Enter URL: ')
    b2 = int(input('Enter b2: '))
    b3 = int(input('Enter b3: '))
    return b1, b2, b3
def fonk2():
    b4 = ssl.create_default_context()
    b4.b5 = False
    b4.b6 = ssl.CERT_NONE
    return b4
def fonk3(b1, b3, b4):
    b7 = urllib.request.urlopen(b1, context=b4).read()
    b8 = BeautifulSoup(b7, 'b7.parser')
    b9 = b8.find_all('a')
    b10 = b9[b3 - 1].get('href', None)
    return b10
def fonk4():
    b1, b2, b3 = fonk1()
    b4 = fonk2()
    for _ in range(b2):
        print('Retrieving:', b1)
        b1 = fonk3(b1, b3, b4)
if b11 = = '__main__':
    fonk4()