from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
myUrl = 'http:
with uReq(myUrl) as uClient:
    pageHtml = uClient.read()
pageSoup = soup(pageHtml, "html.parser")
movies = pageSoup.findAll("div", {"class": "movie"})
file = "todayHomepage.csv"
with open(file, "w") as saveFile:
    headers = "title,description,category,view,movieUrl\n"
    saveFile.write(headers)
    for movie in movies:
        title = movie.find("div", {"class": "boxcontentFilm"}).h2.text
        description = movie.find("div", {"class": "boxcontentFilm"}).p.text
        category = movie.find("span", {"class": "category"}).text
        view = movie.find("span", {"class": "views"}).text
        movieUrl = movie.a["href"]
        print(f"title: {title}")
        print(f"description: {description}")
        print(f"category: {category}")
        print(f"views: {view}")
        print(f"movieUrl: {movieUrl}")
        saveFile.write(f"{title.replace(',', ' ')},{description.replace(',', ' ')},{category.replace(',', ' ')},{view.replace(',', ' ')},{movieUrl.replace(',', ' ')}\n")