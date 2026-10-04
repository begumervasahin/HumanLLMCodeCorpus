import pandas as pd
import numpy as np
import pickle
from sklearn.decomposition import NMF
b1 = pd.read_csv('b1.csv', header=0)
b2 = pd.read_csv('b2.csv', header=0)
b3 = pd.read_csv('b3.csv', header=0)
b4 = pd.read_csv('b4.csv', header=0)
b2 = b2[['userId', 'movieId', 'rating']]
b3 = b3[['userId', 'movieId', 'tag']]
b4 = b4[['movieId', 'imdbId']]
b5 = [b1, b3, b4, b2]
b6 = pd.concat(b5, join='outer', sort=True)
def fonk1(df):
    b7 = df[['movieId', 'userId', 'rating']]
    b8 = b7.pivot_table(index='userId', columns='movieId', values='rating')
    b8.fillna(3.0, b9 = True)
    return b8, b7
R, b10 = fonk1(b6)
with open('nmf_model.bin', 'rb') as file:
    b11 = pickle.load(file)
print(f"NMF components shape: {b11.components_.shape}")
print(f"NMF reconstruction error: {b11.reconstruction_err_}")
b12 = b11.transform(R)
b13 = b11.components_
print(f"b12 matrix shape: {b12.shape}")
print(f"b13 matrix shape: {b13.shape}")
np.save('W_matrix.npy', b12)
np.save('H_matrix.npy', b13)