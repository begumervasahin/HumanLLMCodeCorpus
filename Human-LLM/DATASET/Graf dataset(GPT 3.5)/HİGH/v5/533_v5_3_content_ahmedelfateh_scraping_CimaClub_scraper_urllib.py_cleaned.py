import urllib.request
from bs4 import BeautifulSoup
b1 = 'http:
with urllib.request.urlopen(b1) as response:
    b2 = response.read()
b3 = BeautifulSoup(b2, "html.parser")
b4 = b3.find_all("div", class_="movie")
b5 = "todayHomepage.csv"
with open(b5, "w") as file:
    b6 = "b7, b8, b9, b10, movieUrl\n"
    file.write(b6)
    for movie in b4:
        b7 = movie.find("div", class_="boxcontentFilm").h2.text
        b8 = movie.find("div", class_="boxcontentFilm").p.text
        b9 = movie.find("span", class_="b9").text
        b10 = movie.find("span", class_="views").text
        b11 = movie.a["href"]
        print("Title:", b7)
        print("Description:", b8)
        print("Category:", b9)
        print("Views:", b10)
        print("Movie URL:", b11)
        file.write(f"{b7.replace(',', ' ')}, {b8.replace(',', ' ')}, "
                   f"{b9.replace(',', ' ')}, {b10.replace(',', ' ')}, {b11.replace(',', ' ')}\n")
print("Data has been successfully written to", b5)