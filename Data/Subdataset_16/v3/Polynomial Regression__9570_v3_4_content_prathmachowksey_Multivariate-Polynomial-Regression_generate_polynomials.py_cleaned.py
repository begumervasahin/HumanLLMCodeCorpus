import numpy as np
import pandas as pd
from itertools import combinations_with_replacement
def fonk1(degree):
    b1 = []
    for i in range(1, degree + 1):
        b1.extend(combinations_with_replacement([0, 1], i))
    return b1
def fonk2(b4, b1):
    b2 = np.ones((b4.shape[0], len(b1)))
    for n in range(b4.shape[0]):
        for i, power in enumerate(b1):
            for j in power:
                b2[n, i] *= b4[n, j]
    return b2
b3 = pd.read_csv('3D_spatial_network.txt', names=["id", "latitude", "longitude", "altitude"])
print("Initial b3 preview:")
print(b3.head())
b3 = b3.drop("id", axis=1)
print("Data after dropping 'id' column:")
print(b3.head())
b3 = (b3 - b3.mean()) / b3.std()
print("Normalized b3 preview:")
print(b3.head())
b4 = b3.iloc[:, :2].values
b5 = b3.iloc[:, 2:3].values
b6 = range(1, 7)
b7 = {degree: fonk1(degree) for degree in b6}
b8 = {degree: fonk2(b4, b7[degree]) for degree in b6}
b5 = (b5 - b5.mean()) / b5.std()
for degree in b6:
    b8[degree] = (b8[degree] - b8[degree].mean()) / b8[degree].std()
for degree in b6:
    np.save(f'X_{degree}.npy', b8[degree])
np.save('b5.npy', b5)
print("Data transformation and saving complete.")