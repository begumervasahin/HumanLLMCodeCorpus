import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from time import sleep
from random import randint
titles, years, time, imdb_ratings, metascores, votes, us_gross = ([] for _ in range(7))
headers = {"Accept-Language": "en-US, en;q=0.5"}
pages = np.arange(1, 1001, 50)
def extract_text(element, class_name, default='_'):
    return element.find(class_=class_name).get_text() if element.find(class_=class_name) else default
for page in pages:
    url = f"https:
    response = requests.get(url, headers=headers)
    sleep(randint(2, 10))
    soup = BeautifulSoup(response.text, 'html.parser')
    movie_div = soup.find_all('div', class_='lister-item mode-advanced')
    for container in movie_div:
        titles.append(container.h3.a.text)
        years.append(container.h3.find('span', class_='lister-item-year').text)
        time.append(extract_text(container.p, 'runtime'))
        imdb_ratings.append(float(container.strong.text))
        metascores.append(extract_text(container, 'metascore'))
        votes.append(container.find('span', attrs={'name': 'nv'})[0].text)
        us_gross.append(extract_text(container, 'nv', '-'))
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
movies['metascore'] = pd.to_numeric(movies['metascore'], errors='coerce')
movies['us_grossMillions'] = movies['us_grossMillions'].str.replace('M', '').str.replace('$', '').astype(float)
movies.to_csv('movie.csv', index=False)
print(movies.to_string())
print(movies.dtypes)