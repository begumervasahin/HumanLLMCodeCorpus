import requests
import json
import os
from bs4 import BeautifulSoup
def top_scrape_list():
    if os.path.isfile("cache_file_for_task_1.json"):
        with open("cache_file_for_task_1.json", "r") as data_file:
            return json.load(data_file)
    else:
        endpoint = 'https:
        req = requests.get(endpoint)
        result = req.text
        soup = BeautifulSoup(result, 'html.parser')
        main = soup.find('div', class_='article')
        sub_main = main.find('div', class_='lister')
        tbody = sub_main.find('tbody', class_='lister-list')
        trs = tbody.find_all('tr')
        movies_list = []
        for rank, tr in enumerate(trs, start=1):
            td = tr.find('td', class_='titleColumn')
            title = td.find('a').text
            year = int(td.find('span').text[1:5])
            link = "https:
            rating = tr.find('td', class_='ratingColumn imdbRating').text.strip()
            movie_data = {'Title': title, 'Rank': rank, 'Year': year, 'URL': link, 'Rating': rating}
            movies_list.append(movie_data)
        with open("cache_file_for_task_1.json", "w") as data_file:
            json.dump(movies_list, data_file, indent=4)
        return movies_list
movies = top_scrape_list()
print("Top-rated Indian movies data has been scraped and stored.")