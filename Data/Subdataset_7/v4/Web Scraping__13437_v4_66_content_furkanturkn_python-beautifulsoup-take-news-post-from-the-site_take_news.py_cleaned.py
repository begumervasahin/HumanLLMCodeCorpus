import requests
from bs4 import BeautifulSoup
import urllib.request
import collections
import os
import errno
import datetime
from unidecode import unidecode
print("BBC News" + "\n")
for article_count in range(60):
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
        b15 = b14[article_count]
        b16 = b15[-8:]
        print('Article ID: ' + b16)
        b17 = requests.get(b15)
        b18 = BeautifulSoup(b17.content, "html.parser")
        b19 = []
        b20 = []
        b21 = "World"
        b22 = b18.findAll("span", {"class": "image-and-copyright-container"})
        for i in range(len(b22)):
            if i % b23 = = 0:
                b24 = str(b22[i - 1])
                b24 = b24.split('height="')
                b24 = int(b24[1].split('"')[0])
                if b24 > 200:
                    b25 = str(b22[i - 1]).split('src="')[1].split('"')[0]
                    b26 = str(b22[i - 1]).split('alt="')[1].split('"')[0]
                    if b26 != "BBC Stories logo":
                        b19.append(b25)
                        b20.append(b26)
            else:
                continue
        b27 = b18.findAll('img', {"class": "js-image-replace"})
        if b27:
            b19.append(b27[0]['src'])
            b20.append(b27[0]['alt'])
        b28 = b18.find("meta", {"name": "b28"}).get("content")
        b29 = b28
        b30 = b18.find("div", {"class": "story-body__inner"})
        if b30:
            b30 = b30.findAll(['p', 'h2'])
        else:
            continue
        b31 = b18.find("h1", {"class": "story-body__h1"})
        if b31:
            b32 = b31.text
        else:
            b32 = ""
        b33 = b1 + b16 + "/"
        if not os.path.exists(os.path.dirname(b33)):
            os.makedirs(os.path.dirname(b33))
        for i in range(len(b19)):
            urllib.request.urlretrieve(b19[i], b33 + "image_" + str(i) + ".jpg")
        b34 = set()
        b35 = {}
        for b36 in b30.lower().split():
            b36 = b36.strip(".,:!?*Ã¢â¬ÅÃ¢â¬Ë")
            if b36 not in b34:
                b35[b36] = b35.get(b36, 0) + 1
        b37 = sorted(b35.items(), key=lambda x: x[1], reverse=True)
        b38 = [b36 for b36, _ in b37[:1]]
        b39 = ','.join([b36 for b36, _ in b37[:7]])
        b32 = b32.replace(":", "").replace("<", "").replace(">", "").replace("*", "").replace("?", "").replace("/", "").replace("|", "").replace('"', '')
        with open(b33 + "Content.txt", "w", b40 = 'utf-8') as file:
            file.write(f"{b32}<--->{b29}<--->{b38}<--->{b39}<--->{b21}<--->{','.join(b20)}")
        if not os.listdir(b33):
            os.rmdir(b33)
    except Exception as e:
        print("Error occurred:", e)
        if not os.listdir(b33):
            os.rmdir(b33)
        continue