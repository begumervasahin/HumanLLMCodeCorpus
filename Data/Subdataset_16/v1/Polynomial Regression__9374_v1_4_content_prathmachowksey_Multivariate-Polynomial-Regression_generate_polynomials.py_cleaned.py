import numpy as np
import pandas as pd
from itertools import combinations_with_replacement
def fonk1(degree):
    b1 = [0, 1]
    b2 = []
    for i in range(1, degree + 1):
        b2.append([x for x in combinations_with_replacement(b1, i)])
    b3 = []
    for sublist in b2:
        for x in sublist:
            b3.append(x)
    return b3
def fonk2(b6, b2):
    b4 = np.ones((b6.shape[0], len(b2)))
    for n in range(b6.shape[0]):
        for i in range(len(b2)):
            for j in b2[i]:
                b4[n][i] = b4[n][i] * b6[n][j]
    return b4
b5 = pd.read_csv('3D_spatial_network.txt', names=["id", "latitude", "longitude", "altitude"])
print(b5.head())
b5 = b5.drop("id", axis=1)
print(b5.head())
b5 = (b5 - b5.mean()) / b5.std()
print(b5.head())
b6 = b5.iloc[:, 0:2].values
b7 = b5.iloc[:, 2:3].values
b8 = [1, 2, 3, 4, 5, 6]
b9 = {degree: fonk1(degree) for degree in b8}
b10 = {degree: fonk2(b6, b9[degree]) for degree in b8}
b7 = (b7 - b7.mean()) / b7.std()
for degree in b8:
    b10[degree] = (b10[degree] - b10[degree].mean()) / b10[degree].std()
for degree in b8:
    np.save(f'X_{degree}.npy', b10[degree])
np.save('b7.npy', b7)
print("Data transformation and saving complete.")