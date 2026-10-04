import os
import re
import pandas as pd
from sqlalchemy import create_engine
def load_data(movies_file, ratings_file):
    df_movies = pd.read_csv(movies_file)
    df_ratings = pd.read_csv(ratings_file)
    return df_movies, df_ratings
def merge_data(df_movies, df_ratings):
    return pd.merge(df_ratings, df_movies, how='outer', on='movieId')
def extract_year(title):
    match = re.findall(r"\(([0-9]{4})\)", title)
    return match[0] if match else 0
def clean_data(df):
    df['year'] = df['title'].apply(extract_year)
    df['title'] = df['title'].str.replace(r"\(([0-9]{4})\)", "", regex=True)
    cols = ['userId', 'movieId', 'rating', 'title', 'genres', 'year', 'timestamp']
    df = df[cols]
    df.sort_values(by='movieId', inplace=True)
    df.dropna(subset=['userId'], inplace=True)
    return df
def save_to_sqlite(df, db_path):
    engine = create_engine(f'sqlite:
    df.to_sql('movie_ratings', engine, if_exists='replace', index=False)
def save_to_postgres(df, connection_string):
    engine = create_engine(connection_string)
    df.to_sql('movies_ratings', engine, if_exists='replace', index=False)
def main():
    data_folder = './data/'
    movies_file = os.path.join(data_folder, 'movies.csv')
    ratings_file = os.path.join(data_folder, 'ratings.csv')
    df_movies, df_ratings = load_data(movies_file, ratings_file)
    df_merged = merge_data(df_movies, df_ratings)
    df_cleaned = clean_data(df_merged)
    SAVE_TO_POSTGRES = False
    SAVE_TO_SQLITE = True
    if SAVE_TO_SQLITE:
        save_to_sqlite(df_cleaned, os.path.join(data_folder, 'movielens.db'))
    if SAVE_TO_POSTGRES:
        HOST = 'localhost'
        PORT = '5432'
        DBNAME = 'movielens'
        connection_string = f'postgresql:
        save_to_postgres(df_cleaned, connection_string)
    os.remove(movies_file)
    os.remove(ratings_file)
if __name__ == '__main__':
    main()