import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from time import sleep
from random import randint
def fetch_movie_data():
    titles = []
    years = []
    runtimes = []
    imdb_ratings = []
    metascores = []
    votes = []
    us_gross = []
    headers = {"Accept-Language": "en-US, en;q=0.5"}
    pages = np.arange(1, 1001, 50)
    for page in pages:
        url = f"https:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        movie_divs = soup.find_all('div', class_='lister-item mode-advanced')
        sleep(randint(2, 10))
        for container in movie_divs:
            title = container.h3.a.text
            titles.append(title)
            year = container.h3.find('span', class_='lister-item-year').text
            years.append(year)
            runtime = container.find('span', class_='runtime').text if container.p.find('span', class_='runtime') else '_'
            runtimes.append(runtime)
            imdb_rating = float(container.strong.text)
            imdb_ratings.append(imdb_rating)
            metascore = container.find('span', class_='metascore').text if container.find('span', class_='metascore') else '-'
            metascores.append(metascore)
            nv_elements = container.find_all('span', attrs={'name': 'nv'})
            vote_count = nv_elements[0].text
            votes.append(vote_count)
            gross = nv_elements[1].text if len(nv_elements) > 1 else '-'
            us_gross.append(gross)
    movies_df = pd.DataFrame({
        'movie': titles,
        'year': years,
        'runtime': runtimes,
        'imdb_rating': imdb_ratings,
        'metascore': metascores,
        'votes': votes,
        'us_gross': us_gross,
    })
    movies_df['year'] = movies_df['year'].str.extract('(\d+)').astype(int)
    movies_df['runtime'] = movies_df['runtime'].str.extract('(\d+)').astype(float)
    movies_df['votes'] = movies_df['votes'].str.replace(',', '').astype(int)
    movies_df['metascore'] = pd.to_numeric(movies_df['metascore'].str.extract('(\d+)')[0], errors='coerce')
    movies_df['us_gross'] = pd.to_numeric(movies_df['us_gross'].map(lambda x: x.lstrip('$').rstrip('M')), errors='coerce')
    movies_df.to_csv('movie.csv', index=False)
    print(movies_df.to_string())
    print(movies_df.dtypes)
if __name__ == "__main__":
    fetch_movie_data()