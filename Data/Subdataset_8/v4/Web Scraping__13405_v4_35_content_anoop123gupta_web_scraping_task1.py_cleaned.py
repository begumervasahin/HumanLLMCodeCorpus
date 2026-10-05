import requests
import json
import os
from bs4 import BeautifulSoup
def top_scrape_list():
    if os.path.isfile("cache_file_for_task_1.json"):
        with open("cache_file_for_task_1.json", "r+") as data_file:
            data = json.load(data_file)
            return data
    else:
        endpoint = 'https:
        req = requests.get(endpoint)
        result = req.text
        soup = BeautifulSoup(result, 'html.parser')
        main = soup.find('div', class_='article')
        sub_main = main.find('div', class_='lister')
        tbody = sub_main.find('tbody', class_='lister-list')
        trs = tbody.find_all('tr')
        movie_list = []
        rank = 0
        unique_years = []
        for tr in trs:
            rank += 1
            td = tr.find('td', class_='titleColumn')
            title = td.find('a').text
            year = int(td.find('span').text[1:5])
            if year not in unique_years:
                unique_years.append(year)
            movie_url = "https:
            rating = tr.find('td', class_='ratingColumn imdbRating').text.strip()
            movie_details = {'Title': title, 'Rank': rank, 'Year': year, 'URL': movie_url, 'Rating': rating}
            movie_list.append(movie_details)
        with open("cache_file_for_task_1.json", "w") as cache_file:
            json.dump(movie_list, cache_file)
        return movie_list
movies = top_scrape_list()