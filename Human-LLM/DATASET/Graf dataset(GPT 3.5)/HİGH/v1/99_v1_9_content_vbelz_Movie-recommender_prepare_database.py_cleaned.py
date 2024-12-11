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
def fonk1(x):
    '''Extract year from title'''
    b7 = re.findall("\(([0-9]{4})\)", x)
    try:
        b7 = b7[0]
    except:
        b7 = 0
    return b7
b6['year'] = b6['title'].apply(get_year)
b6['title'] = b6['title'].str.replace("\(([0-9]{4})\)", "")
b8 = ['userId', 'movieId', 'rating', 'title', 'genres', 'year', 'timestamp']
b6 = b6[b8]
b6.sort_values(b9 = ['movieId'], inplace=True)
b6.dropna(b10 = ['userId'], how='any', inplace=True)
if b4:
    b11 = 'localhost'
    b12 = '5432'
    b13 = 'movielens'
    b14 = f'postgres:
    b15 = create_engine(b14)
    b6.to_sql('movies_ratings', b15)
if b5:
    b16 = create_engine('sqlite:
    b6.to_sql('movie_ratings', b16)
os.remove(b1 + 'movies.csv')
os.remove(b1 + 'ratings.csv')