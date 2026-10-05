import requests
import os
import json
import random
import time
from bs4 import BeautifulSoup
def fonk1():
    b1 = requests.get("https:
    b2 = BeautifulSoup(b1.text, "html.parser")
    b3 = b2.find("tbody", class_="lister-list")
    b4 = b3.find_all("tr")
    b5 = []
    for i in b4:
        b6 = i.find("td", class_="titleColumn").getText().strip()
        b7 = b6.strip()
        b8 = b7.split("\n")
        b9 = b8[1].strip()
        b10 = float(b8[0])
        b11 = int(b8[2][1:5])
        b12 = i.find("strong").getText().strip()
        b13 = i.find("b7")
        b14 = b13.get("href")
        b14 = b14[:17]
        b15 = {
            "name": b9,
            "b17": b11,
            "position": b10,
            "Ratings": b12,
            "b1": "https:
        }
        b5.append(b15)
    return b5
def fonk2(movies):
    b16 = {}
    for movie in movies:
        b17 = movie["b17"]
        if b17 not in b16:
            b16[b17] = []
        b16[b17].append(movie)
    return b16
def fonk3(movies):
    b18 = {}
    for movie in movies:
        b19 = movie["b17"] - (movie["b17"] % 10)
        if b19 not in b18:
            b18[b19] = []
        b18[b19].append(movie)
    return b18
def fonk4(movie_cast_url):
def fonk5(movie_url):
def fonk6(b21):
def fonk7(b21):
def fonk8(b21):
def fonk9(b21):
def fonk10(b21):
def fonk11(b21):
def fonk12(b21):
b20 = fonk1()
b21 = b20[:]
pprint(fonk9(b21))