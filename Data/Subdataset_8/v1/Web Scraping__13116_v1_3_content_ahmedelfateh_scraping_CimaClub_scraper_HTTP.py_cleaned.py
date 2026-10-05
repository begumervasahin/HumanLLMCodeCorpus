from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
def simple_get(url):
    try:
        response = urlopen(url)
        if response.getcode() == 200:
            return response.read()
        else:
            return None
    except Exception as e:
        print("Error fetching URL:", e)
        return None
myUrl = 'http:
uClient = simple_get(myUrl)
if uClient:
    pageSoup = soup(uClient, "html.parser")
    movies = pageSoup.findAll("div", {"class": "movie"})
    file = "todayHomepage.csv"
    with open(file, "w", encoding="utf-8") as saveFile:
        headers = "title, description, category, view, movieUrl\n"
        saveFile.write(headers)
        for movie in movies:
            titleList = movie.findAll("div", {"class": "boxcontentFilm"})
            title = titleList[0].h2.text.strip()
            description = titleList[0].p.text.strip()
            categoryList = movie.findAll("span", {"class": "category"})
            category = categoryList[0].text.strip()
            viewsList = movie.findAll("span", {"class": "views"})
            view = viewsList[0].text.strip()
            movieUrl = movie.a["href"]
            print("Title: " + title)
            print("Description: " + description)
            print("Category: " + category)
            print("Views: " + view)
            print("Movie URL: " + movieUrl)
            saveFile.write(f"{title.replace(',', ' ')}, {description.replace(',', ' ')}, {category.replace(',', ' ')}, {view.replace(',', ' ')}, {movieUrl.replace(',', ' ')}\n")
    print("Data saved to", file)
else:
    print("Failed to fetch the webpage.")