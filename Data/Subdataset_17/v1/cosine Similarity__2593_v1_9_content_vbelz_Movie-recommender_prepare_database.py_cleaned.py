import os
import re
import pandas as pd
from sqlalchemy import create_engine
data_folder = './data/'
movies_file = os.path.join(data_folder, 'movies.csv')
ratings_file = os.path.join(data_folder, 'ratings.csv')
df_movies = pd.read_csv(movies_file)
df_ratings = pd.read_csv(ratings_file)
SAVE_TO_POSTGRES = False
SAVE_TO_SQLITE = True
df_merge = pd.merge(df_ratings, df_movies, how='outer', on='movieId')
def extract_year(title):
    match = re.findall(r"\(([0-9]{4})\)", title)
    return match[0] if match else 0
df_merge['year'] = df_merge['title'].apply(extract_year)
df_merge['title'] = df_merge['title'].str.replace(r"\(([0-9]{4})\)", "", regex=True)
cols = ['userId', 'movieId', 'rating', 'title', 'genres', 'year', 'timestamp']
df_merge = df_merge[cols]
df_merge.sort_values(by='movieId', inplace=True)
df_merge.dropna(subset=['userId'], inplace=True)
if SAVE_TO_POSTGRES:
    HOST = 'localhost'
    PORT = '5432'
    DBNAME = 'movielens'
    connection_string = f'postgresql:
    db_engine = create_engine(connection_string)
    df_merge.to_sql('movies_ratings', db_engine, if_exists='replace', index=False)
if SAVE_TO_SQLITE:
    sqlite_engine = create_engine('sqlite:
    df_merge.to_sql('movie_ratings', sqlite_engine, if_exists='replace', index=False)
os.remove(movies_file)
os.remove(ratings_file)