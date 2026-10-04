from bs4 import BeautifulSoup as soup
from workfiles.getUrlData import simple_get
def fonk1(b11):
    b1 = simple_get(b11)
    b2 = soup(b1, "html.parser")
    b3 = b2.findAll("div", {"class": "movie"})
    b4 = []
    for movie in b3:
        b5 = movie.find("div", {"class": "boxcontentFilm"}).h2.text
        b6 = movie.find("div", {"class": "boxcontentFilm"}).p.text
        b7 = movie.find("span", {"class": "b7"}).text
        b8 = movie.find("span", {"class": "views"}).text
        b9 = movie.a["href"]
        b4.append({
            "b5": b5.replace(",", " "),
            "b6": b6.replace(",", " "),
            "b7": b7.replace(",", " "),
            "b8": b8.replace(",", " "),
            "movieUrl": b9.replace(",", " ")
        })
        print(f"b5: {b5}")
        print(f"b6: {b6}")
        print(f"b7: {b7}")
        print(f"views: {b8}")
        print(f"movieUrl: {b9}")
    return b4
def fonk2(b13, b12, data):
    with open(b13, "w") as file:
        file.write(b12)
        for entry in data:
            b10 = f"{entry['b5']}, {entry['b6']}, {entry['b7']}, {entry['b8']}, {entry['movieUrl']}\n"
            file.write(b10)
def fonk3():
    b11 = 'http:
    b12 = "b5, b6, b7, b8, movieUrl\n"
    b13 = "todayHomepage.csv"
    b4 = fonk1(b11)
    fonk2(b13, b12, b4)
if b14 = = "__main__":
    fonk3()