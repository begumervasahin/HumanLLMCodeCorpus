import urllib.request
from bs4 import BeautifulSoup
import ssl
b1 = ssl.create_default_context()
b1.b2 = False
b1.b3 = ssl.CERT_NONE
def fonk1(b6, b4):
    return urllib.request.urlopen(b6, b4 = b4).read()
def fonk2(b10, b8):
    b5 = b10('a')
    if len(b5) >= b8:
        return b5[b8 - 1].get('href', None)
    else:
        print(f"No link found at b8 {b8}")
        return None
def fonk3():
    b6 = input('Enter URL: ')
    b7 = int(input('Enter b7: '))
    b8 = int(input('Enter b8: '))
    for i in range(b7 + 1):
        print('Retrieving:', b6)
        b9 = fonk1(b6, b1)
        b10 = BeautifulSoup(b9, 'b9.parser')
        b11 = fonk2(b10, b8)
        if b11:
            b6 = b11
        else:
            break
if b12 = = "__main__":
    fonk3()