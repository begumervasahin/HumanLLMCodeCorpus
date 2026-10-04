import os
import re
import pandas as pd
from sqlalchemy import create_engine
b1 = './data/'
b2 = os.path.join(b1, 'movies.csv')
b3 = os.path.join(b1, 'ratings.csv')
b4 = pd.read_csv(b2)
b5 = pd.read_csv(b3)
b6 = False
b7 = True
b8 = pd.merge(b5, b4, how='outer', on='movieId')
def fonk1(title):
    b9 = re.findall(r"\(([0-9]{4})\)", title)
    return b9[0] if b9 else 0
b8['year'] = b8['title'].apply(extract_year)
b8['title'] = b8['title'].str.replace(r"\(([0-9]{4})\)", "", b10 = True)
b11 = ['userId', 'movieId', 'rating', 'title', 'genres', 'year', 'timestamp']
b8 = b8[b11]
b8.sort_values(b12 = 'movieId', inplace=True)
b8.dropna(b13 = ['userId'], inplace=True)
if b6:
    b14 = 'localhost'
    b15 = '5432'
    b16 = 'movielens'
    b17 = f'postgresql:
    b18 = create_engine(b17)
    b8.to_sql('movies_ratings', b18, b19 = 'replace', index=False)
if b7:
    b20 = create_engine('sqlite:
    b8.to_sql('movie_ratings', b20, b19 = 'replace', index=False)
os.remove(b2)
os.remove(b3)