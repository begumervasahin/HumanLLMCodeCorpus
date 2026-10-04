from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
def fonk1(b8):
    with uReq(b8) as uClient:
        return uClient.read()
def fonk2(html):
    return soup(html, "html.parser")
def fonk3(movie):
    b1 = movie.find("div", {"class": "boxcontentFilm"}).h2.text
    b2 = movie.find("div", {"class": "boxcontentFilm"}).p.text
    b3 = movie.find("span", {"class": "b3"}).text
    b4 = movie.find("span", {"class": "views"}).text
    b5 = movie.a["href"]
    return {
        "b1": b1,
        "b2": b2,
        "b3": b3,
        "b4": b4,
        "b5": b5
    }
def fonk4(b11, filename):
    with open(filename, "w") as file:
        b6 = "b1,b2,b3,b4,b5\n"
        file.write(b6)
        for movie in b11:
            b7 = fonk3(movie)
            file.write(f"{b7['b1'].replace(',', ' ')},"
                       f"{b7['b2'].replace(',', ' ')},"
                       f"{b7['b3'].replace(',', ' ')},"
                       f"{b7['b4'].replace(',', ' ')},"
                       f"{b7['b5'].replace(',', ' ')}\n")
def fonk5():
    b8 = 'http:
    b9 = fonk1(b8)
    b10 = fonk2(b9)
    b11 = b10.findAll("div", {"class": "movie"})
    fonk4(b11, "todayHomepage.csv")
if b12 = = "__main__":
    fonk5()