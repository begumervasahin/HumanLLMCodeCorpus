from bs4 import BeautifulSoup as soup
from workfiles.getUrlData import simple_get
def fonk1(element):
    return element.text.strip() if element else ""
b1 = 'http:
b2 = simple_get(b1)
b3 = soup(b2, "html.parser")
b4 = b3.find_all("div", class_="movie")
b5 = "todayHomepage.csv"
b6 = "b8, b10, b12, b14, movieUrl\n"
with open(b5, "w") as csv_file:
    csv_file.write(b6)
    for movie in b4:
        b7 = movie.find("div", class_="boxcontentFilm").h2
        b8 = fonk1(b7)
        b9 = movie.find("div", class_="boxcontentFilm").p
        b10 = fonk1(b9)
        b11 = movie.find("span", class_="b12")
        b12 = fonk1(b11)
        b13 = movie.find("span", class_="views")
        b14 = fonk1(b13)
        b15 = movie.a["href"]
        print("Title:", b8)
        print("Description:", b10)
        print("Category:", b12)
        print("Views:", b14)
        print("Movie URL:", b15)
        csv_file.write(f"{b8.replace(',', ' ')}, {b10.replace(',', ' ')}, "
                       f"{b12.replace(',', ' ')}, {b14.replace(',', ' ')}, {b15.replace(',', ' ')}\n")
print("Data extraction completed.")