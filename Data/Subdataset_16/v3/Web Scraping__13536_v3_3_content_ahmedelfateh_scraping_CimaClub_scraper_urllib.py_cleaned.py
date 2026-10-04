import requests
from bs4 import BeautifulSoup
import csv
def fonk1(b14):
    b1 = requests.get(b14)
    return b1.content
def fonk2(b17):
    b2 = BeautifulSoup(b17, "html.parser")
    return b2.findAll("div", {"class": "movie"})
def fonk3(movie):
    b3 = movie.find("div", {"class": "boxcontentFilm"})
    b4 = b3.h2.text if b3 and b3.h2 else "No Title"
    b5 = b3.p.text if b3 and b3.p else "No Description"
    b6 = movie.find("span", {"class": "b7"})
    b7 = b6.text if b6 else "No Category"
    b8 = movie.find("span", {"class": "views"})
    b9 = b8.text if b8 else "No Views"
    b10 = movie.a["href"] if movie.a else "No URL"
    return b4, b5, b7, b9, b10
def fonk4(file_name, b16, b18):
    with open(file_name, "w", b11 = '', encoding='utf-8') as file:
        b12 = csv.b12(file)
        b12.writerow(b16)
        for movie in b18:
            b13 = fonk3(movie)
            b12.writerow([detail.replace(",", " ") for detail in b13])
def fonk5():
    b14 = 'http:
    b15 = "todayHomepage.csv"
    b16 = ["Title", "Description", "Category", "View", "Movie URL"]
    b17 = fonk1(b14)
    b18 = fonk2(b17)
    fonk4(b15, b16, b18)
    print(f"Data has been written to {b15}")
if b19 = = "__main__":
    fonk5()