from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
b1 = 'http:
with uReq(b1) as uClient:
    b2 = uClient.read()
b3 = soup(b2, "html.parser")
b4 = b3.findAll("div", {"class": "movie"})
b5 = "todayHomepage.csv"
with open(b5, "w") as saveFile:
    b6 = "b7,b8,b9,b10,b11\n"
    saveFile.write(b6)
    for movie in b4:
        b7 = movie.find("div", {"class": "boxcontentFilm"}).h2.text
        b8 = movie.find("div", {"class": "boxcontentFilm"}).p.text
        b9 = movie.find("span", {"class": "b9"}).text
        b10 = movie.find("span", {"class": "views"}).text
        b11 = movie.a["href"]
        print(f"b7: {b7}")
        print(f"b8: {b8}")
        print(f"b9: {b9}")
        print(f"views: {b10}")
        print(f"b11: {b11}")
        saveFile.write(f"{b7.replace(',', ' ')},{b8.replace(',', ' ')},{b9.replace(',', ' ')},{b10.replace(',', ' ')},{b11.replace(',', ' ')}\n")