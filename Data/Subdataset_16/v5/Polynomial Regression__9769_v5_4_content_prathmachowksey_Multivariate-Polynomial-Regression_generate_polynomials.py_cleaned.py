import numpy as np
import pandas as pd
from itertools import combinations_with_replacement
def fonk1(degree):
    b1 = [0, 1]
    b2 = []
    for i in range(1, degree + 1):
        b2.extend(combinations_with_replacement(b1, i))
    return b2
def fonk2(b7, b2):
    b3 = b7.shape[0]
    b4 = len(b2)
    b5 = np.ones((b3, b4))
    for n in range(b3):
        for i, power in enumerate(b2):
            for p in power:
                b5[n, i] *= b7[n, p]
    return b5
b6 = pd.read_csv('3D_spatial_network.txt', names=["id", "latitude", "longitude", "altitude"])
print("Initial b6 sample:\n", b6.head())
b6 = b6.drop("id", axis=1)
b6 = (b6 - b6.mean()) / b6.std()
print("Standardized b6 sample:\n", b6.head())
b7 = b6.iloc[:, 0:2].values
b8 = b6.iloc[:, 2:3].values
b8 = (b8 - b8.mean()) / b8.std()
b9 = [1, 2, 3, 4, 5, 6]
b10 = {}
for degree in b9:
    b2 = fonk1(degree)
    b11 = fonk2(b7, b2)
    b11 = (b11 - b11.mean(axis=0)) / b11.std(axis=0)
    b10[degree] = b11
    np.save(f'X_{degree}.npy', b11)
np.save('b8.npy', b8)
print("Sample b2 for degree 3:\n", fonk1(3))
print("Original b7 samples:\n", b7[:3])
print("Transformed b7 samples for degree 3:\n", b10[3][:3])