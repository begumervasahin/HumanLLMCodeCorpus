import requests
from bs4 import BeautifulSoup
import csv
b1 = 'http:
b2 = requests.get(b1)
b3 = BeautifulSoup(b2.content, "html.parser")
b4 = b3.findAll("div", {"class": "movie"})
b5 = "todayHomepage.csv"
with open(b5, "w", b6 = '', encoding='utf-8') as file:
    b7 = csv.b7(file)
    b8 = ["Title", "Description", "Category", "View", "Movie URL"]
    b7.writerow(b8)
    for movie in b4:
        b9 = movie.find("div", {"class": "boxcontentFilm"})
        b10 = b9.h2.text if b9 and b9.h2 else "No Title"
        b11 = b9.p.text if b9 and b9.p else "No Description"
        b12 = movie.find("span", {"class": "b13"})
        b13 = b12.text if b12 else "No Category"
        b14 = movie.find("span", {"class": "views"})
        b15 = b14.text if b14 else "No Views"
        b16 = movie.a["href"] if movie.a else "No URL"
        print(f"Title: {b10}")
        print(f"Description: {b11}")
        print(f"Category: {b13}")
        print(f"Views: {b15}")
        print(f"Movie URL: {b16}")
        b7.writerow([
            b10.replace(",", " "),
            b11.replace(",", " "),
            b13.replace(",", " "),
            b15.replace(",", " "),
            b16.replace(",", " ")
        ])