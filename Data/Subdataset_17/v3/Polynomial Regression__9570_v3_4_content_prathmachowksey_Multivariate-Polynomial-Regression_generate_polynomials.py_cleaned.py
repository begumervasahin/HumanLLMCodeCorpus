import numpy as np
import pandas as pd
from itertools import combinations_with_replacement
def get_powers(degree):
    powers = []
    for i in range(1, degree + 1):
        powers.extend(combinations_with_replacement([0, 1], i))
    return powers
def transform_data(X, powers):
    X_new = np.ones((X.shape[0], len(powers)))
    for n in range(X.shape[0]):
        for i, power in enumerate(powers):
            for j in power:
                X_new[n, i] *= X[n, j]
    return X_new
data = pd.read_csv('3D_spatial_network.txt', names=["id", "latitude", "longitude", "altitude"])
print("Initial data preview:")
print(data.head())
data = data.drop("id", axis=1)
print("Data after dropping 'id' column:")
print(data.head())
data = (data - data.mean()) / data.std()
print("Normalized data preview:")
print(data.head())
X = data.iloc[:, :2].values
y = data.iloc[:, 2:3].values
degrees = range(1, 7)
power_combinations = {degree: get_powers(degree) for degree in degrees}
transformed_data = {degree: transform_data(X, power_combinations[degree]) for degree in degrees}
y = (y - y.mean()) / y.std()
for degree in degrees:
    transformed_data[degree] = (transformed_data[degree] - transformed_data[degree].mean()) / transformed_data[degree].std()
for degree in degrees:
    np.save(f'X_{degree}.npy', transformed_data[degree])
np.save('y.npy', y)
print("Data transformation and saving complete.")