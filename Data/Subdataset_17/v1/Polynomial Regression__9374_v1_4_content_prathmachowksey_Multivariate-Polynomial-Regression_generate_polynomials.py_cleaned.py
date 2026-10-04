import numpy as np
import pandas as pd
from itertools import combinations_with_replacement
def get_powers(degree):
    l = [0, 1]
    powers = []
    for i in range(1, degree + 1):
        powers.append([x for x in combinations_with_replacement(l, i)])
    powers_flattened = []
    for sublist in powers:
        for x in sublist:
            powers_flattened.append(x)
    return powers_flattened
def transform_data(X, powers):
    X_new = np.ones((X.shape[0], len(powers)))
    for n in range(X.shape[0]):
        for i in range(len(powers)):
            for j in powers[i]:
                X_new[n][i] = X_new[n][i] * X[n][j]
    return X_new
data = pd.read_csv('3D_spatial_network.txt', names=["id", "latitude", "longitude", "altitude"])
print(data.head())
data = data.drop("id", axis=1)
print(data.head())
data = (data - data.mean()) / data.std()
print(data.head())
X = data.iloc[:, 0:2].values
y = data.iloc[:, 2:3].values
degrees = [1, 2, 3, 4, 5, 6]
power_combinations = {degree: get_powers(degree) for degree in degrees}
transformed_data = {degree: transform_data(X, power_combinations[degree]) for degree in degrees}
y = (y - y.mean()) / y.std()
for degree in degrees:
    transformed_data[degree] = (transformed_data[degree] - transformed_data[degree].mean()) / transformed_data[degree].std()
for degree in degrees:
    np.save(f'X_{degree}.npy', transformed_data[degree])
np.save('y.npy', y)
print("Data transformation and saving complete.")