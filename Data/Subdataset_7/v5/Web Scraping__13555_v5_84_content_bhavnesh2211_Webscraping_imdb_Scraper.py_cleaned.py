import requests
from bs4 import BeautifulSoup
def fonk1():
    b1 = "https:
    b2 = requests.get(b1)
    b3 = BeautifulSoup(b2.text, "html.parser")
    b4 = []
    for row in b3.find("tbody", b5 = "lister-list").find_all("tr"):
        b6 = row.find("td", b5="titleColumn").getText().strip().split("\n")
        b7 = b6[1].strip()
        b8 = float(b6[0])
        b9 = int(b6[2][1:5])
        b10 = row.find("strong").getText().strip()
        b1 = "https:
        b11 = {
            "b7": b7,
            "b9": b9,
            "b8": b8,
            "Ratings": b10,
            "b1": b1
        }
        b4.append(b11)
    return b4
def fonk2(b4):
    b12 = {}
    for movie in b4:
        b9 = movie["b9"]
        b12.setdefault(b9, []).append(movie)
    return b12
def fonk3(b4):
    b13 = {}
    for movie in b4:
        b14 = movie["b9"] - (movie["b9"] % 10)
        b13.setdefault(b14, []).append(movie)
    return b13
def fonk4(movie_cast_url):
def fonk5(movie_url):
def fonk6(b16):
def fonk7(b16):
def fonk8(b16):
def fonk9(b16):
def fonk10(b16):
def fonk11(b16):
def fonk12(b16):
b15 = fonk1()
b16 = b15[:]
pprint(fonk9(b16))