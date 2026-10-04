import requests
from bs4 import BeautifulSoup
import csv
url = 'http:
response = requests.get(url)
page_soup = BeautifulSoup(response.content, "html.parser")
movies = page_soup.findAll("div", {"class": "movie"})
file = "todayHomepage.csv"
with open(file, "w", newline='', encoding='utf-8') as save_file:
    writer = csv.writer(save_file)
    headers = ["title", "description", "category", "view", "movieUrl"]
    writer.writerow(headers)
    for movie in movies:
        title_list = movie.findAll("div", {"class": "boxcontentFilm"})
        title = title_list[0].h2.text if title_list[0].h2 else "No Title"
        description = title_list[0].p.text if title_list[0].p else "No Description"
        category_list = movie.findAll("span", {"class": "category"})
        category = category_list[0].text if category_list else "No Category"
        views_list = movie.findAll("span", {"class": "views"})
        view = views_list[0].text if views_list else "No Views"
        movie_url = movie.a["href"] if movie.a else "No URL"
        print(f"title: {title}")
        print(f"description: {description}")
        print(f"category: {category}")
        print(f"views: {view}")
        print(f"movieUrl: {movie_url}")
        writer.writerow([title.replace(",", " "), description.replace(",", " "),
                         category.replace(",", " "), view.replace(",", " "),
                         movie_url.replace(",", " ")])