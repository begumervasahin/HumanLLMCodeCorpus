from bs4 import BeautifulSoup as soup
from workfiles.getUrlData import simple_get
def fonk1(b12):
    b1 = simple_get(b12)
    b2 = soup(b1, "html.parser")
    b3 = b2.find_all("div", {"class": "movie"})
    b4 = []
    for movie in b3:
        b5 = movie.find("div", {"class": "boxcontentFilm"}).h2.text.strip()
        b6 = movie.find("div", {"class": "boxcontentFilm"}).p.text.strip()
        b7 = movie.find("span", {"class": "b7"}).text.strip()
        b8 = movie.find("span", {"class": "views"}).text.strip()
        b9 = movie.a["href"].strip()
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
def fonk2(b14, b13, data):
    with open(b14, "w", b10 = 'utf-8') as file:
        file.write(b13)
        for entry in data:
            b11 = f"{entry['b5']}, {entry['b6']}, {entry['b7']}, {entry['b8']}, {entry['movieUrl']}\n"
            file.write(b11)
def fonk3():
    b12 = 'http:
    b13 = "b5, b6, b7, b8, movieUrl\n"
    b14 = "todayHomepage.csv"
    b4 = fonk1(b12)
    fonk2(b14, b13, b4)
if b15 = = "__main__":
    fonk3()