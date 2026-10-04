import urllib.request
import ssl
from bs4 import BeautifulSoup
b1 = ssl.create_default_context()
b1.b2 = False
b1.b3 = ssl.CERT_NONE
def fonk1(b7, b9):
    b4 = urllib.request.urlopen(b7, context=b1).read()
    b5 = BeautifulSoup(b4, 'b4.parser')
    b6 = b5('a')
    return b6[b9 - 1].get('href', None)
def fonk2():
    b7 = input('Enter URL: ')
    b8 = int(input('Enter b8: '))
    b9 = int(input('Enter b9: '))
    for _ in range(b8 + 1):
        print('Retrieving:', b7)
        b7 = fonk1(b7, b9)
        if b7 is None:
            print("No URL found at the specified b9.")
            break
if b10 = = "__main__":
    fonk2()