import numpy as np
import pandas as pd
from itertools import combinations_with_replacement
def get_powers(degree):
    base = [0, 1]
    powers = []
    for i in range(1, degree + 1):
        powers.extend(combinations_with_replacement(base, i))
    return powers
def transform_data(X, powers):
    num_samples = X.shape[0]
    num_features = len(powers)
    X_new = np.ones((num_samples, num_features))
    for n in range(num_samples):
        for i, power in enumerate(powers):
            for p in power:
                X_new[n, i] *= X[n, p]
    return X_new
data = pd.read_csv('3D_spatial_network.txt', names=["id", "latitude", "longitude", "altitude"])
print("Initial data sample:\n", data.head())
data = data.drop("id", axis=1)
data = (data - data.mean()) / data.std()
print("Standardized data sample:\n", data.head())
X = data.iloc[:, 0:2].values
y = data.iloc[:, 2:3].values
y = (y - y.mean()) / y.std()
degrees = [1, 2, 3, 4, 5, 6]
transformed_data = {}
for degree in degrees:
    powers = get_powers(degree)
    X_transformed = transform_data(X, powers)
    X_transformed = (X_transformed - X_transformed.mean(axis=0)) / X_transformed.std(axis=0)
    transformed_data[degree] = X_transformed
    np.save(f'X_{degree}.npy', X_transformed)
np.save('y.npy', y)
print("Sample powers for degree 3:\n", get_powers(3))
print("Original X samples:\n", X[:3])
print("Transformed X samples for degree 3:\n", transformed_data[3][:3])