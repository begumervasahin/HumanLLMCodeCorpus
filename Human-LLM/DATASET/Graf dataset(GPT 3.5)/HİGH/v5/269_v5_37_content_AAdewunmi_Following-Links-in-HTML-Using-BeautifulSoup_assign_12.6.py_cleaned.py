import urllib.request
from bs4 import BeautifulSoup
import ssl
def fonk1(b7, b9, b10):
    b1 = ssl.create_default_context()
    b1.b2 = False
    b1.b3 = ssl.CERT_NONE
    for _ in range(b9):
        print('Retrieving:', b7)
        try:
            b4 = urllib.request.urlopen(b7, context=b1).read()
            b5 = BeautifulSoup(b4, 'b4.parser')
            b6 = b5.find_all('a')
            b7 = b6[b10 - 1].get('href', None)
        except Exception as e:
            print('Error:', e)
            break
if b8 = = "__main__":
    b7 = input('Enter URL: ')
    b9 = int(input('Enter b9: '))
    b10 = int(input('Enter b10: '))
    fonk1(b7, b9, b10)