import os
import re
import pandas as pd
from sqlalchemy import create_engine
b1 = './data/'
b2 = pd.read_csv(b1 + 'movies.csv')
b3 = pd.read_csv(b1 + 'ratings.csv')
b4 = False
b5 = True
b6 = pd.merge(b3, b2, how='outer', left_on='movieId', right_on='movieId')
def fonk1(title):
    '''Extract year from title'''
    b7 = re.findall("\(([0-9]{4})\)", title)
    return b7[0] if b7 else 0
b6['year'] = b6['title'].apply(extract_year_from_title)
b6['title'] = b6['title'].str.replace("\(([0-9]{4})\)", "")
b8 = ['userId', 'movieId', 'rating', 'title', 'genres', 'year', 'timestamp']
b6 = b6[b8]
b6.sort_values(b9 = 'movieId', inplace=True)
b6.dropna(b10 = ['userId'], inplace=True)
if b4:
    b11 = create_engine('postgres:
    b6.to_sql('movies_ratings', b11, b12 = False)
if b5:
    b13 = create_engine('sqlite:
    b6.to_sql('movie_ratings', b13, b12 = False)
os.remove(os.path.join(b1, 'movies.csv'))
os.remove(os.path.join(b1, 'ratings.csv'))