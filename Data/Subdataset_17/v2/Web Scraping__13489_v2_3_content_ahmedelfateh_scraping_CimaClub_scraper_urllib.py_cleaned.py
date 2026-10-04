import requests
from bs4 import BeautifulSoup
import csv
url = 'http:
response = requests.get(url)
page_soup = BeautifulSoup(response.content, "html.parser")
movies = page_soup.findAll("div", {"class": "movie"})
output_file = "todayHomepage.csv"
with open(output_file, "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    headers = ["Title", "Description", "Category", "View", "Movie URL"]
    writer.writerow(headers)
    for movie in movies:
        title_container = movie.find("div", {"class": "boxcontentFilm"})
        title = title_container.h2.text if title_container and title_container.h2 else "No Title"
        description = title_container.p.text if title_container and title_container.p else "No Description"
        category_container = movie.find("span", {"class": "category"})
        category = category_container.text if category_container else "No Category"
        views_container = movie.find("span", {"class": "views"})
        view = views_container.text if views_container else "No Views"
        movie_url = movie.a["href"] if movie.a else "No URL"
        print(f"Title: {title}")
        print(f"Description: {description}")
        print(f"Category: {category}")
        print(f"Views: {view}")
        print(f"Movie URL: {movie_url}")
        writer.writerow([
            title.replace(",", " "),
            description.replace(",", " "),
            category.replace(",", " "),
            view.replace(",", " "),
            movie_url.replace(",", " ")
        ])