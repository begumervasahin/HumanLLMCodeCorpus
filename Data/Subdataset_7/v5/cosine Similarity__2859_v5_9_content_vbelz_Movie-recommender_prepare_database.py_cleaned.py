import os
import re
import pandas as pd
from sqlalchemy import create_engine
b1 = './data/'
b2 = pd.read_csv(os.path.join(b1, 'movies.csv'))
b3 = pd.read_csv(os.path.join(b1, 'ratings.csv'))
b4 = False
b5 = True
b6 = pd.merge(b3, b2, how='outer', on='movieId')
def fonk1(title):
    '''Extract year from title'''
    b7 = re.findall("\(([0-9]{4})\)", title)
    return b7[0] if b7 else 0
b6['year'] = b6['title'].apply(extract_year_from_title)
b6['title'] = b6['title'].str.replace("\(([0-9]{4})\)", "")
b8 = ['userId', 'movieId', 'rating', 'title', 'genres', 'year', 'timestamp']
b6 = b6[b8].sort_values(by='movieId')
b6.dropna(b9 = ['userId'], inplace=True)
if b4:
    b10 = create_engine('postgres:
    b6.to_sql('movies_ratings', b10, b11 = False)
if b5:
    b12 = create_engine('sqlite:
    b6.to_sql('movie_ratings', b12, b11 = False)
os.remove(os.path.join(b1, 'movies.csv'))
os.remove(os.path.join(b1, 'ratings.csv'))