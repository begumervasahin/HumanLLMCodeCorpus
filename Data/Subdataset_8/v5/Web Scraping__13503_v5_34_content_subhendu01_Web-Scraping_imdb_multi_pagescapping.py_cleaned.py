import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from time import sleep
from random import randint
def scrape_imdb_data(url, headers):
    titles = []
    years = []
    time = []
    imdb_ratings = []
    metascores = []
    votes = []
    us_gross = []
    pages = np.arange(1, 1001, 50)
    for page in pages:
        response = requests.get(url.format(page), headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        movie_divs = soup.find_all('div', class_='lister-item mode-advanced')
        for container in movie_divs:
            titles.append(container.h3.a.text)
            years.append(container.h3.find('span', class_='lister-item-year').text)
            time.append(container.find('span', class_='runtime').text if container.p.find('span', class_='runtime') else '_')
            imdb_ratings.append(float(container.strong.text))
            metascores.append(container.find('span', class_='metascore').text if container.find('span', class_='metascore') else '-')
            nv = container.find_all('span', attrs={'name': 'nv'})
            votes.append(nv[0].text)
            us_gross.append(nv[1].text if len(nv) > 1 else '-')
        sleep(randint(2, 10))
    return titles, years, time, imdb_ratings, metascores, votes, us_gross
def main():
    headers = {"Accept-Language": "en-US, en;q=0.5"}
    url = "https:
    titles, years, time, imdb_ratings, metascores, votes, us_gross = scrape_imdb_data(url, headers)
    movies_data = {
        'movie': titles,
        'year': years,
        'timeMin': time,
        'imdb': imdb_ratings,
        'metascore': metascores,
        'votes': votes,
        'us_grossMillions': us_gross,
    }
    movies_df = pd.DataFrame(movies_data)
    movies_df['year'] = movies_df['year'].str.extract('(\d+)').astype(int)
    movies_df['timeMin'] = movies_df['timeMin'].str.extract('(\d+)').astype(int)
    movies_df['votes'] = movies_df['votes'].str.replace(',', '').astype(int)
    movies_df['metascore'] = movies_df['metascore'].str.extract('(\d+)')
    movies_df['metascore'] = pd.to_numeric(movies_df['metascore'], errors='coerce')
    movies_df['us_grossMillions'] = movies_df['us_grossMillions'].str.replace('$', '').str.replace('M', '').astype(float)
    movies_df.to_csv('movie.csv', index=False)
    print(movies_df.to_string())
    print(movies_df.dtypes)
if __name__ == "__main__":
    main()