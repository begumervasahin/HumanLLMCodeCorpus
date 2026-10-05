import requests
from bs4 import BeautifulSoup
url = 'http:
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
movies = soup.find_all("div", {"class": "movie"})
file_name = "todayHomepage.csv"
with open(file_name, "w", encoding='utf-8') as file:
    file.write("title, description, category, view, movieUrl\n")
    for movie in movies:
        title = movie.find("div", {"class": "boxcontentFilm"}).h2.text.strip()
        description = movie.find("div", {"class": "boxcontentFilm"}).p.text.strip()
        category = movie.find("span", {"class": "category"}).text.strip()
        view = movie.find("span", {"class": "views"}).text.strip()
        movieUrl = movie.a["href"]
        print("Title:", title)
        print("Description:", description)
        print("Category:", category)
        print("Views:", view)
        print("Movie URL:", movieUrl)
        file.write(f"{title.replace(',', ' ')}, {description.replace(',', ' ')}, "
                   f"{category.replace(',', ' ')}, {view.replace(',', ' ')}, {movieUrl.replace(',', ' ')}\n")
print("Data has been scraped and saved to", file_name)