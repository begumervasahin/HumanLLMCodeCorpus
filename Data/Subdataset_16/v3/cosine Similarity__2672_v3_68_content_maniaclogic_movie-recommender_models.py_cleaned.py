import pandas as pd
import numpy as np
import pickle
from sklearn.decomposition import NMF
def fonk1():
    b1 = pd.read_csv('b1.csv', header=0)
    b2 = pd.read_csv('b2.csv', header=0)
    b3 = pd.read_csv('b3.csv', header=0)
    b4 = pd.read_csv('b4.csv', header=0)
    b2 = b2[['userId', 'movieId', 'rating']]
    b3 = b3[['userId', 'movieId', 'tag']]
    b4 = b4[['movieId', 'imdbId']]
    return b1, b2, b3, b4
def fonk2(b9):
    return pd.concat(b9, b5 = 'outer', sort=True)
def fonk3(df):
    b6 = df[['movieId', 'userId', 'rating']]
    b7 = b6.pivot_table(index='userId', columns='movieId', values='rating')
    b7.fillna(3.0, b8 = True)
    return b7, b6
def fonk4(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)
def fonk5(b13, b14):
    np.save('W_matrix.npy', b13)
    np.save('H_matrix.npy', b14)
def fonk6():
    b1, b2, b3, b4 = fonk1()
    b9 = [b1, b3, b4, b2]
    b10 = fonk2(b9)
    R, b11 = fonk3(b10)
    b12 = fonk4('nmf_model.bin')
    print(f"NMF components shape: {b12.components_.shape}")
    print(f"NMF reconstruction error: {b12.reconstruction_err_}")
    b13 = b12.transform(R)
    b14 = b12.components_
    print(f"b13 matrix shape: {b13.shape}")
    print(f"b14 matrix shape: {b14.shape}")
    fonk5(b13, b14)
if b15 = = '__main__':
    fonk6()