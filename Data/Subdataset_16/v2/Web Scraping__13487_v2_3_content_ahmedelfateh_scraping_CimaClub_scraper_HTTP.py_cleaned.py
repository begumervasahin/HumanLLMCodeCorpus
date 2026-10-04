import csv
from bs4 import BeautifulSoup
from workfiles.getUrlData import simple_get
def fonk1(url):
    try:
        b1 = simple_get(url)
        if b1 is None:
            print(f"Failed to retrieve data from {url}")
            return None
        return b1
    except Exception as e:
        print(f"An error occurred while fetching data: {e}")
        return None
def fonk2(b11):
    b2 = BeautifulSoup(b11, "html.parser")
    return b2.findAll("div", {"class": "movie"})
def fonk3(movie):
    b3 = movie.find("div", {"class": "boxcontentFilm"}).h2.text
    b4 = movie.find("div", {"class": "boxcontentFilm"}).p.text
    b5 = movie.find("span", {"class": "b5"}).text
    b6 = movie.find("span", {"class": "views"}).text
    b7 = movie.a["href"]
    return b3, b4, b5, b6, b7
def fonk4(file_name, b15, b12):
    with open(file_name, b8 = 'w', newline='', encoding='utf-8') as file:
        b9 = csv.b9(file)
        b9.writerow(b15)
        for movie in b12:
            b9.writerow(movie)
def fonk5():
    b10 = 'http:
    b11 = fonk1(b10)
    if b11 is None:
        print("No data to process. Exiting.")
        return
    b12 = fonk2(b11)
    if not b12:
        print("No b12 found on the page.")
        return
    b13 = []
    for movie in b12:
        try:
            b14 = fonk3(movie)
            b13.append(b14)
        except AttributeError as e:
            print(f"An error occurred while parsing movie b14: {e}")
            continue
    b15 = ["Title", "Description", "Category", "Views", "Movie URL"]
    fonk4("todayHomepage.csv", b15, b13)
    print(f"Data saved to todayHomepage.csv")
if b16 = = "__main__":
    fonk5()