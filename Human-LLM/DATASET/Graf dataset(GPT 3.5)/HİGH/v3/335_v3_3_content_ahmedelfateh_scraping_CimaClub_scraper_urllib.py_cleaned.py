import requests
from bs4 import BeautifulSoup
b1 = 'http:
b2 = requests.get(b1)
b3 = BeautifulSoup(b2.text, 'html.parser')
b4 = b3.find_all("div", class_="movie")
b5 = "todayHomepage.csv"
with open(b5, "w", b6 = 'utf-8') as file:
    file.write("b7, b8, b9, b10, b11\n")
    for movie in b4:
        b7 = movie.find("div", class_="boxcontentFilm").h2.text.strip()
        b8 = movie.find("div", class_="boxcontentFilm").p.text.strip()
        b9 = movie.find("span", class_="b9").text.strip()
        b10 = movie.find("span", class_="views").text.strip()
        b11 = movie.a["href"]
        print("Title:", b7)
        print("Description:", b8)
        print("Category:", b9)
        print("Views:", b10)
        print("Movie URL:", b11)
        file.write(f"{b7.replace(',', ' ')}, {b8.replace(',', ' ')}, "
                   f"{b9.replace(',', ' ')}, {b10.replace(',', ' ')}, {b11.replace(',', ' ')}\n")
print("Data has been scraped and saved to", b5)