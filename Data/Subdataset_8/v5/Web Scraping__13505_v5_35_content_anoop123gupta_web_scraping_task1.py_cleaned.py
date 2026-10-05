import requests
import json
import os
from bs4 import BeautifulSoup
def top_scrape_list():
    cache_file_path = "cache_file_for_task_1.json"
    if os.path.isfile(cache_file_path):
        with open(cache_file_path, "r") as cache_file:
            return json.load(cache_file)
    else:
        endpoint = 'https:
        response = requests.get(endpoint)
        soup = BeautifulSoup(response.text, 'html.parser')
        main_content = soup.find('div', class_='article')
        movie_list_container = main_content.find('div', class_='lister')
        movie_rows = movie_list_container.find('tbody', class_='lister-list').find_all('tr')
        movies = []
        unique_years = set()
        for rank, movie_row in enumerate(movie_rows, start=1):
            title_column = movie_row.find('td', class_='titleColumn')
            title = title_column.find('a').text
            year = int(title_column.find('span').text[1:5])
            movie_url = "https:
            rating = movie_row.find('td', class_='ratingColumn imdbRating').text.strip()
            unique_years.add(year)
            movie_details = {'Title': title, 'Rank': rank, 'Year': year, 'URL': movie_url, 'Rating': rating}
            movies.append(movie_details)
        with open(cache_file_path, "w") as cache_file:
            json.dump(movies, cache_file)
        return movies
movies = top_scrape_list()