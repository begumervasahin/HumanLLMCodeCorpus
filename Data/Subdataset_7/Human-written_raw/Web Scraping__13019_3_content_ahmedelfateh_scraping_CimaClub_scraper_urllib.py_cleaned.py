from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
b1 = 'http:
b2 = uReq(b1)
b3 = b2.read()
b2.close()
b4 = soup(b3, "html.parser")
b5 = b4.findAll("div", {"class": "movie"})
b6 = "todayHomepage.csv"
b7 = open(b6, "w")
b8 = "b10, b11, b13, b15, b16\n"
b7.write(b8)
for movie in b5:
    b9 = movie.findAll("div", {"class": "boxcontentFilm"})
    b10 = b9[0].h2.text
    b11 = b9[0].p.text
    b12 = movie.findAll("span", {"class": "b13"})
    b13 = b12[0].text
    b14 = movie.findAll("span", {"class": "views"})
    b15 = b14[0].text
    b16 = movie.a["href"]
    print("b10: " + b10)
    print("b11: " + b11)
    print("b13: " + b13)
    print("views: " + b15)
    print("b16: " + b16)
    b7.write(b10.replace(",", " ") + ", " + b11.replace(",", " ") + ", " +
                   b13.replace(",", " ") + ", " + b15.replace(",", " ") + ", " + b16.replace(",", " ") + "\n")
b7.close()