from random import choice
import requests
import urllib.request
from bs4 import BeautifulSoup
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
    b5 = b4.findAll("div",{"class":"deal"})
    b6 = len(b5)
    b7 = []
    b8 = []
    b9 = []
    b10 = []
    b11 = []
    b12 = []
    for content in b5:
        b13 = content.find("img")
        b11.append(b13['src'].replace(",",""))
        b14 = content.find("div",{"class":"dealName"})
        b7.append(b14.text.replace(",",""))
        b15 = content.find("p")
        b8.append(b15.text.replace(",",""))
        b16 = content.find("a")
        b12.append(b16['href'].replace(",",""))
    b17 = "easemytrip_offers.csv"
    b18 = open(b17,"a")
    b1 = "Offer Name,Link,Description,Image Link,Validity \n"
    b18.write(b1)
    for i in range(0,b6):
        b18.write(b7[i] + "," + b12[0] + "," + b8[i] + "," + b11[i] + "\n")
    b18.close()