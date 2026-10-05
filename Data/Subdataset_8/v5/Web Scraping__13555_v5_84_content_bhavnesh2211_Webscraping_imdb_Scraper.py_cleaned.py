import requests
from bs4 import BeautifulSoup
def scrape_top_list():
    url = "https:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    movies = []
    for row in soup.find("tbody", class_="lister-list").find_all("tr"):
        title_column = row.find("td", class_="titleColumn").getText().strip().split("\n")
        name = title_column[1].strip()
        position = float(title_column[0])
        year = int(title_column[2][1:5])
        rating = row.find("strong").getText().strip()
        url = "https:
        movie_details = {
            "name": name,
            "year": year,
            "position": position,
            "Ratings": rating,
            "url": url
        }
        movies.append(movie_details)
    return movies
def group_by_year(movies):
    group_by_year = {}
    for movie in movies:
        year = movie["year"]
        group_by_year.setdefault(year, []).append(movie)
    return group_by_year
def decade_by_year(movies):
    decade_by_year = {}
    for movie in movies:
        decade = movie["year"] - (movie["year"] % 10)
        decade_by_year.setdefault(decade, []).append(movie)
    return decade_by_year
def scrape_movie_cast(movie_cast_url):
def scrape_movie_details(movie_url):
def get_movie_list_details(movies_list):
def analyse_movies_language(movies_list):
def analyse_movies_Director(movies_list):
def analyse_language_and_directors(movies_list):
def analyse_movies_genre(movies_list):
def analyse_co_actors(movies_list):
def analyse_actors(movies_list):
top_movies = scrape_top_list()
movies_list = top_movies[:]
pprint(analyse_language_and_directors(movies_list))