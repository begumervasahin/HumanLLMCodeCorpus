import pandas as pd
import numpy as np
import pickle
from sklearn.decomposition import NMF
def load_data():
    movies = pd.read_csv('movies.csv', header=0)
    ratings = pd.read_csv('ratings.csv', header=0)
    tags = pd.read_csv('tags.csv', header=0)
    links = pd.read_csv('links.csv', header=0)
    ratings = ratings[['userId', 'movieId', 'rating']]
    tags = tags[['userId', 'movieId', 'tag']]
    links = links[['movieId', 'imdbId']]
    return movies, ratings, tags, links
def combine_data(data_dfs):
    return pd.concat(data_dfs, join='outer', sort=True)
def df_to_matrix(df):
    pre_data = df[['movieId', 'userId', 'rating']]
    data_matrix = pre_data.pivot_table(index='userId', columns='movieId', values='rating')
    data_matrix.fillna(3.0, inplace=True)
    return data_matrix, pre_data
def load_nmf_model(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)
def save_transformed_data(W, H):
    np.save('W_matrix.npy', W)
    np.save('H_matrix.npy', H)
def main():
    movies, ratings, tags, links = load_data()
    data_dfs = [movies, tags, links, ratings]
    combined_df = combine_data(data_dfs)
    R, PRE = df_to_matrix(combined_df)
    nmf = load_nmf_model('nmf_model.bin')
    print(f"NMF components shape: {nmf.components_.shape}")
    print(f"NMF reconstruction error: {nmf.reconstruction_err_}")
    W = nmf.transform(R)
    H = nmf.components_
    print(f"W matrix shape: {W.shape}")
    print(f"H matrix shape: {H.shape}")
    save_transformed_data(W, H)
if __name__ == '__main__':
    main()