import requests
from bs4 import BeautifulSoup
import urllib.request
import os
import datetime
from unidecode import unidecode
print("BBC News" + "\n")
for yazisayi in range(60):
    try:
        b1 = "C:/Users/Administrator/Desktop/Haberler/BBC_News/"
        b2 = "http:
        b3 = "http:
        b4 = "http:
        b5 = requests.get(b2)
        b6 = requests.get(b3)
        b7 = requests.get(b4)
        b8 = BeautifulSoup(b5.content, "xml")
        b9 = BeautifulSoup(b6.content, "xml")
        b10 = BeautifulSoup(b7.content, "xml")
        b11 = b8.findAll('item')
        b12 = b9.findAll('item')
        b13 = b10.findAll('item')
        b14 = []
        for i in range(20):
            b14.append(b11[i].contents[5].text)
            b14.append(b13[i].contents[5].text)
            b14.append(b12[i].contents[5].text)
        b15 = b14[yazisayi]
        b16 = b15[-8:]
        print('Haber ID: ' + b16)
        b17 = requests.get(b15)
        b18 = BeautifulSoup(b17.content, "html.parser")
        b19 = b18.findAll("span", {"class": "image-and-copyright-container"})
        b20 = []
        b21 = []
        for i in range(len(b19)):
            b22 = b19[i - 1].split('src="')[1].split('"')[0]
            b23 = b19[i - 1].split('alt="')[1].split('"')[0]
            if b23 != "BBC Stories logo":
                b20.append(b22)
                b21.append(b23)
        b24 = b18.find("meta", {"b31": "b24"}).get("content")
        b25 = b24
        b26 = b18.find("h1", {"class": "story-body__h1"})
        if b26 is not None:
            b27 = b26.text
        else:
            b27 = ''
        b28 = b1 + b16 + "/"
        if not os.path.exists(b28):
            os.makedirs(b28)
        for i in range(len(b20)):
            b29 = os.path.join(b28, f"{i}_{b16}.jpg")
            urllib.request.urlretrieve(b20[i], b29)
        b30 = ""
        for paragraph in b18.find("div", {"class": "story-body__inner"}).findAll(['p', 'h2']):
            if paragraph.b31 = = "h2":
                b30 += f"<h2>{paragraph.text}</h2><br><br>"
            else:
                b30 += f"{paragraph.text}<br><br>"
        with open(os.path.join(b28, "Content.html"), "w", b32 = 'utf-8') as file:
            file.write(b30)
    except Exception as e:
        print("An error occurred:", e)
        continue