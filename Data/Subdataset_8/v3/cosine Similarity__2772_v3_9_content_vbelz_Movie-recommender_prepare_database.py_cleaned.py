import os
import re
import pandas as pd
from sqlalchemy import create_engine
data_folder = './data/'
df_movies = pd.read_csv(data_folder + 'movies.csv')
df_ratings = pd.read_csv(data_folder + 'ratings.csv')
save_to_postgres = False
save_to_sqlite = True
df_merge = pd.merge(df_ratings, df_movies, how='outer', left_on='movieId', right_on='movieId')
def get_year(title):
    '''Extract year from title'''
    year_match = re.findall("\(([0-9]{4})\)", title)
    return year_match[0] if year_match else 0
df_merge['year'] = df_merge['title'].apply(get_year)
df_merge['title'] = df_merge['title'].str.replace("\(([0-9]{4})\)", "")
columns_of_interest = ['userId', 'movieId', 'rating', 'title', 'genres', 'year', 'timestamp']
df_merge = df_merge[columns_of_interest]
df_merge.sort_values(by='movieId', inplace=True)
df_merge.dropna(subset=['userId'], inplace=True)
if save_to_postgres:
    db_connection = create_engine('postgres:
    df_merge.to_sql('movies_ratings', db_connection, index=False)
if save_to_sqlite:
    db_connection_lite = create_engine('sqlite:
    df_merge.to_sql('movie_ratings', db_connection_lite, index=False)
os.remove(os.path.join(data_folder, 'movies.csv'))
os.remove(os.path.join(data_folder, 'ratings.csv'))