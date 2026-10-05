from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
def fonk1(b2):
    try:
        b1 = urlopen(b2)
        if b1.getcode() == 200:
            return b1.read()
        else:
            return None
    except Exception as e:
        print("Error fetching URL:", e)
        return None
def fonk2():
    b2 = 'http:
    b3 = fonk1(b2)
    if b3:
        b4 = soup(b3, "html.parser")
        b5 = b4.findAll("div", {"class": "movie"})
        b6 = "todayHomepage.csv"
        with open(b6, "w", b7 = "utf-8") as save_file:
            b8 = "Title, Description, Category, Views, Movie URL\n"
            save_file.write(b8)
            for movie in b5:
                b9 = movie.findAll("div", {"class": "boxcontentFilm"})
                b10 = b9[0].h2.text.strip()
                b11 = b9[0].p.text.strip()
                b12 = movie.findAll("span", {"class": "b13"})
                b13 = b12[0].text.strip()
                b14 = movie.findAll("span", {"class": "views"})
                b15 = b14[0].text.strip()
                b16 = movie.a["href"]
                print("Title:", b10)
                print("Description:", b11)
                print("Category:", b13)
                print("Views:", b15)
                print("Movie URL:", b16)
                save_file.write(f"{b10.replace(',', ' ')}, {b11.replace(',', ' ')}, {b13.replace(',', ' ')}, {b15.replace(',', ' ')}, {b16.replace(',', ' ')}\n")
        print("Data saved to", b6)
    else:
        print("Failed to fetch the webpage.")
if b17 = = "__main__":
    fonk2()