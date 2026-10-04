import pandas as pd
import numpy as np
import pickle
from sklearn.decomposition import NMF
b1 = pd.read_csv('movies.csv', header=0)
b2 = pd.read_csv('b2.csv', header=0)
b3 = pd.read_csv('b3.csv', header=0)
b4 = pd.read_csv('b4.csv', header=0)
b2 = b2[['userId', 'movieId', 'rating']]
b3 = b3[['userId', 'movieId', 'tag']]
b4 = b4[['movieId', 'imdbId']]
b5 = [movies, b3, b4, b2]
b6 = pd.concat(b5, join='outer', sort=True)
def fonk1(df):
    b7 = b6[['movieId', 'userId', 'rating']]
    b8 = b7.pivot_table(index='userId', columns='movieId', values='rating')
    b8.fillna(3.0, b9 = True)
    return b8, b7
R, b10 = fonk1(b6)
b11 = NMF(n_components=100, init='random', solver='cd', max_iter=300)
b12 = open('nmf_model.bin', 'rb').read()
b11 = pickle.loads(b12)