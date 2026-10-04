from random import choice
import requests
import urllib.request
from bs4 import BeautifulSoup
import io
b1 = [
    'Mozilla/5.0 (compatible; Googlebot/2.1; +http:
    'Googlebot/2.1 (+http:
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'
    ' Ubuntu Chromium/49.0.2623.108 Chrome/49.0.2623.108 Safari/537.36',
    'Gigabot/3.0 (http:
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; pt-BR) AppleWebKit/533.3 '
    '(KHTML, like Gecko)  QtWeb Internet Browser/3.7 http:
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/41.0.2228.0 Safari/537.36',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, '
    'like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.4pre) '
    'Gecko/20070404 K-Ninja/2.1.3',
    'Mozilla/5.0 (Future Star Technologies Corp.; Star-Blade OS; x86_64; U; '
    'en-US) iNet Browser 4.7',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.13) '
    'Gecko/20080414 Firefox/2.0.0.13 Pogo/2.0.0.13.6866',
    'WorldWideweb (NEXT)'
]
def fonk1():
	return {'User-Agent':choice(b1)}
b2 = "https:
b3 = requests.get(b2, b1=fonk1())
b4 = BeautifulSoup(b3.text, 'b3.parser')
def fonk2():
    b5 = b4.findAll("div",{"class":["deals-cntent-left","deals-cntent-center","deals-cntent-right"]})
    b6 = len(b5)
    b7 = []
    b8 = []
    b9 = []
    b10 = []
    for i in b5:
        b11 = i.find("img")
        b7.append(b11['src'])
        b12 = i.find("div",{"class":"deals-cntent-name"})
        b8.append(b12.text.replace(",",""))
        b13 = i.find("div",{"class":"deals-cntent-disc"})
        b9.append(b13.text.replace(",",""))
        b14 = i.find("div",{"class":"deals-box-ftr-left"})
        b10.append(b14.text)
    b15 = "akbartravels_offers.csv"
    b16 = open(b15,"a")
    b1 = "Offer Name,Image Link,Description,Validity \n"
    b16.write(b1)
    for i in range(0,b6):
        b16.write(b8[i] + "," + b7[i] + "," + b9[i] + "," + b10[i] + "\n")
    b16.close()