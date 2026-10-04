import numpy as np
import pandas as pd
from itertools import combinations_with_replacement
def fonk1(degree):
    b1 = [0, 1]
    b2 = []
    for i in range(1, degree + 1):
        b2.extend(combinations_with_replacement(b1, i))
    return b2
def fonk2(b5, b2):
    b3 = np.ones((b5.shape[0], len(b2)))
    for n in range(b5.shape[0]):
        for i, power in enumerate(b2):
            for p in power:
                b3[n, i] *= b5[n, p]
    return b3
b4 = pd.read_csv('3D_spatial_network.txt', names=["id", "latitude", "longitude", "altitude"])
print(b4.head())
b4 = b4.drop("id", axis=1)
b4 = (b4 - b4.mean()) / b4.std()
print(b4.head())
b5 = b4.iloc[:, 0:2].values
b6 = b4.iloc[:, 2:3].values
b7 = [1, 2, 3, 4, 5, 6]
b8 = {}
for degree in b7:
    b2 = fonk1(degree)
    b9 = fonk2(b5, b2)
    b9 = (b9 - b9.mean(axis=0)) / b9.std(axis=0)
    b8[degree] = b9
b6 = (b6 - b6.mean()) / b6.std()
for degree, b9 in b8.items():
    np.save(f'X_{degree}.npy', b9)
np.save('b6.npy', b6)
print("Sample b2 for degree 3:", fonk1(3))
print("Original b5 samples:", b5[:3])
print("Transformed b5 samples for degree 3:", b8[3][:3])