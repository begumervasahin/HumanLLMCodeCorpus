import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from time import sleep
from random import randint
titles, years, times, imdb_ratings, metascores, votes, us_gross = ([] for _ in range(7))
headers = {"Accept-Language": "en-US, en;q=0.5"}
pages = np.arange(1, 1001, 50)
for page in pages:
    response = requests.get(f"https:
    soup = BeautifulSoup(response.text, 'html.parser')
    movie_containers = soup.find_all('div', class_='lister-item mode-advanced')
    sleep(randint(2, 10))
    for container in movie_containers:
        title = container.h3.a.text
        titles.append(title)
        year = container.h3.find('span', class_='lister-item-year').text
        years.append(year)
        runtime = container.find('span', class_='runtime')
        time = runtime.text if runtime else '_'
        times.append(time)
        imdb_rating = float(container.strong.text)
        imdb_ratings.append(imdb_rating)
        metascore = container.find('span', class_='metascore')
        metascore = metascore.text.strip() if metascore else '-'
        metascores.append(metascore)
        nv = container.find_all('span', attrs={'name': 'nv'})
        vote = nv[0].text
        votes.append(vote)
        us_gross_value = nv[1].text if len(nv) > 1 else '-'
        us_gross.append(us_gross_value)
movies_df = pd.DataFrame({
    'movie': titles,
    'year': years,
    'timeMin': times,
    'imdb': imdb_ratings,
    'metascore': metascores,
    'votes': votes,
    'us_grossMillions': us_gross,
})
movies_df['year'] = movies_df['year'].str.extract('(\d+)').astype(int)
movies_df['timeMin'] = movies_df['timeMin'].str.extract('(\d+)').astype(int)
movies_df['votes'] = movies_df['votes'].str.replace(',', '').astype(int)
movies_df['metascore'] = pd.to_numeric(movies_df['metascore'].str.extract('(\d+)')[0], errors='coerce')
movies_df['us_grossMillions'] = pd.to_numeric(movies_df['us_grossMillions'].str.replace('$', '').str.replace('M', ''), errors='coerce')
movies_df.to_csv('movie.csv', index=False)
print(movies_df.to_string())
print(movies_df.dtypes)