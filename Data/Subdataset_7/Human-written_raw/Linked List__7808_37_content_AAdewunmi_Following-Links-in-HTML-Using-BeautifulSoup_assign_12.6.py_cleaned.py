import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
b1 = ssl.create_default_context()
b1.b2 = False
b1.b3 = ssl.CERT_NONE
b4 = input('Enter URL: ')
b5 = int(input('Enter b5: '))
b6 = int(input('Enter b6: '))
for i in range(b5 + 1):
    print ('Retrieving:', b4)
    b7 = urllib.request.urlopen(b4, context=b1).read()
    b8 = BeautifulSoup(b7, 'b7.parser')
    b9 = b8('a')
    b4 = b9[b6 - 1].get('href', None)