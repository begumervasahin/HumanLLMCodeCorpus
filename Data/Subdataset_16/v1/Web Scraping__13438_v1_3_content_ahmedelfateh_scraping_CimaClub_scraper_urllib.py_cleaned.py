import requests
from bs4 import BeautifulSoup
import csv
b1 = 'http:
b2 = requests.get(b1)
b3 = BeautifulSoup(b2.content, "html.parser")
b4 = b3.findAll("div", {"class": "movie"})
b5 = "todayHomepage.csv"
with open(b5, "w", b6 = '', encoding='utf-8') as save_file:
    b7 = csv.b7(save_file)
    b8 = ["b10", "b11", "b13", "b15", "movieUrl"]
    b7.writerow(b8)
    for movie in b4:
        b9 = movie.findAll("div", {"class": "boxcontentFilm"})
        b10 = b9[0].h2.text if b9[0].h2 else "No Title"
        b11 = b9[0].p.text if b9[0].p else "No Description"
        b12 = movie.findAll("span", {"class": "b13"})
        b13 = b12[0].text if b12 else "No Category"
        b14 = movie.findAll("span", {"class": "views"})
        b15 = b14[0].text if b14 else "No Views"
        b16 = movie.a["href"] if movie.a else "No URL"
        print(f"b10: {b10}")
        print(f"b11: {b11}")
        print(f"b13: {b13}")
        print(f"views: {b15}")
        print(f"movieUrl: {b16}")
        b7.writerow([b10.replace(",", " "), b11.replace(",", " "),
                         b13.replace(",", " "), b15.replace(",", " "),
                         b16.replace(",", " ")])