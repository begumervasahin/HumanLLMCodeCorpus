import requests
from bs4 import BeautifulSoup
import urllib.request
import os
import datetime
from unidecode import unidecode
def fonk1():
    b1 = "http:
    b2 = "http:
    b3 = "http:
    b4 = requests.get(b1)
    b5 = requests.get(b2)
    b6 = requests.get(b3)
    b7 = BeautifulSoup(b4.content, "xml")
    b8 = BeautifulSoup(b5.content, "xml")
    b9 = BeautifulSoup(b6.content, "xml")
    b10 = b7.findAll('item')
    b11 = b8.findAll('item')
    b12 = b9.findAll('item')
    b13 = []
    for i in range(20):
        b13.append(b10[i].contents[5].text)
        b13.append(b12[i].contents[5].text)
        b13.append(b11[i].contents[5].text)
    return b13
def fonk2(b26, b22, b27):
    for i, img_url in enumerate(b26):
        b14 = os.path.join(b27, f"{i}_{b22}.jpg")
        urllib.request.urlretrieve(img_url, b14)
def fonk3(b24):
    b15 = b24.find("h1", {"class": "story-body__h1"})
    b16 = b15.text if b15 else ''
    b17 = b24.find("meta", {"b20": "b17"}).get("content")
    b18 = b17
    b19 = ""
    for paragraph in b24.find("div", {"class": "story-body__inner"}).findAll(['p', 'h2']):
        if paragraph.b20 = = "h2":
            b19 += f"<h2>{paragraph.text}</h2><br><br>"
        else:
            b19 += f"{paragraph.text}<br><br>"
    return b16, b18, b19
def fonk4(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
def fonk5(news_url):
    try:
        b21 = "C:/Users/Administrator/Desktop/Haberler/BBC_News/"
        b22 = news_url[-8:]
        print('Haber ID:', b22)
        b23 = requests.get(news_url)
        b24 = BeautifulSoup(b23.content, "html.parser")
        b25 = b24.findAll("span", {"class": "image-and-copyright-container"})
        b26 = [img.split('src="')[1].split('"')[0] for img in b25 if "BBC Stories logo" not in img]
        b27 = os.path.join(b21, b22)
        fonk4(b27)
        fonk2(b26, b22, b27)
        b16, b18, b19 = fonk3(b24)
        with open(os.path.join(b27, "Content.html"), "w", b28 = 'utf-8') as file:
            file.write(b19)
    except Exception as e:
        print(f"Error processing article {news_url}: {e}")
def fonk6():
    print("BBC News\n")
    b13 = fonk1()
    for yazisayi in range(60):
        if yazisayi < len(b13):
            fonk5(b13[yazisayi])
if b29 = = "__main__":
    fonk6()