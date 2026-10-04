import pandas as pd
import numpy as np
import pickle
from sklearn.decomposition import NMF
movies = pd.read_csv('movies.csv', header=0)
ratings = pd.read_csv('ratings.csv', header=0)
tags = pd.read_csv('tags.csv', header=0)
links = pd.read_csv('links.csv', header=0)
ratings = ratings[['userId', 'movieId', 'rating']]
tags = tags[['userId', 'movieId', 'tag']]
links = links[['movieId', 'imdbId']]
data_dfs = [movies, tags, links, ratings]
DF = pd.concat(data_dfs, join='outer', sort=True)
def df_to_matrix(df):
    pre_data = DF[['movieId', 'userId', 'rating']]
    data = pre_data.pivot_table(index='userId', columns='movieId', values='rating')
    data.fillna(3.0, inplace=True)
    return data, pre_data
R, PRE = df_to_matrix(DF)
with open('nmf_model.bin', 'rb') as file:
    nmf = pickle.load(file)
print(f"NMF components shape: {nmf.components_.shape}")
print(f"NMF reconstruction error: {nmf.reconstruction_err_}")
W = nmf.transform(R)
H = nmf.components_
print(f"W matrix shape: {W.shape}")
print(f"H matrix shape: {H.shape}")
np.save('W_matrix.npy', W)
np.save('H_matrix.npy', H)