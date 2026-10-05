import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from time import sleep
from random import randint
titles = []
years = []
time = []
imdb_ratings = []
metascores = []
votes = []
us_gross = []
headers = {"Accept-Language": "en-US, en;q=0.5"}
pages = np.arange(1, 1001, 50)
for page in pages:
    url = f"https:
    response = requests.get(url, headers=headers)
    sleep(randint(2, 10))
    soup = BeautifulSoup(response.text, 'html.parser')
    movie_div = soup.find_all('div', class_='lister-item mode-advanced')
    for container in movie_div:
        titles.append(container.h3.a.text)
        years.append(container.h3.find('span', class_='lister-item-year').text)
        time.append(container.find('span', class_='runtime').text if container.p.find('span', class_='runtime') else '_')
        imdb_ratings.append(float(container.strong.text))
        metascores.append(container.find('span', class_='metascore').text if container.find('span', class_='metascore') else '-')
        nv = container.find_all('span', attrs={'name': 'nv'})
        votes.append(nv[0].text)
        us_gross.append(nv[1].text if len(nv) > 1 else '-')
movies = pd.DataFrame({
    'movie': titles,
    'year': years,
    'timeMin': time,
    'imdb': imdb_ratings,
    'metascore': metascores,
    'votes': votes,
    'us_grossMillions': us_gross
})
movies['year'] = movies['year'].str.extract('(\d+)').astype(int)
movies['timeMin'] = movies['timeMin'].str.extract('(\d+)').astype(int)
movies['votes'] = movies['votes'].str.replace(',', '').astype(int)
movies['metascore'] = movies['metascore'].str.extract('(\d+)')
movies['metascore'] = pd.to_numeric(movies['metascore'], errors='coerce')
movies['us_grossMillions'] = movies['us_grossMillions'].str.replace('M', '').str.replace('$', '').astype(float)
movies.to_csv('movie.csv', index=False)
print(movies.to_string())
print(movies.dtypes)