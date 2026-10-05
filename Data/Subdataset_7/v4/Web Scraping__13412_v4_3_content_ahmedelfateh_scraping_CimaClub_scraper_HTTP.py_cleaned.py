
from bs4 import BeautifulSoup as soup
from workfiles.getUrlData import simple_get
b1 = 'http:
b2 = simple_get(b1)
b3 = soup(b2, "html.parser")
b4 = b3.findAll("div", {"class": "movie"})
b5 = "todayHomepage.csv"
b6 = open(b5, "w")
b7 = "b9, b10, b12, b14, b15\n"
b6.write(b7)
for movie in b4:
    b8 = movie.findAll("div", {"class": "boxcontentFilm"})
    b9 = b8[0].h2.text
    b10 = b8[0].p.text
    b11 = movie.findAll("span", {"class": "b12"})
    b12 = b11[0].text
    b13 = movie.findAll("span", {"class": "views"})
    b14 = b13[0].text
    b15 = movie.a["href"]
    print("b9: " + b9)
    print("b10: " + b10)
    print("b12: " + b12)
    print("views: " + b14)
    print("b15: " + b15)
    b6.write(b9.replace(",", " ") + ", " + b10.replace(",", " ") + ", " +
                   b12.replace(",", " ") + ", " + b14.replace(",", " ") + ", " + b15.replace(",", " ") + "\n")
b6.close()