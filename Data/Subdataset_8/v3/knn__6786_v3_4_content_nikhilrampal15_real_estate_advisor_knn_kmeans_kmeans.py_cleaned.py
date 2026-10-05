import pandas as pd
import numpy as np
import random
def read_csv(filename):
    return pd.read_csv(filename)
def generate_centroids(data, k, column_name):
    return random.sample(range(1, data[column_name].max() + 1), k)
def assign_clusters(centroids, data, column_name):
    for idx, house in enumerate(data[column_name]):
        closest_centroid = min(centroids, key=lambda x: abs(house - x))
        data.at[idx, 'cluster'] = closest_centroid
def check_convergence(old_centroids, new_centroids):
    return all(abs(old - new) <= 1 for old, new in zip(old_centroids, new_centroids))
city = "san-francisco-ca"
filename = f"data/propertyInfo/{city}.csv"
data = read_csv(filename)
data["cluster"] = -1
k = 5
centroids = generate_centroids(data, k, 'zestimate')
while True:
    old_centroids = centroids.copy()
    centroids = generate_centroids(data, k, 'zestimate')
    assign_clusters(centroids, data, 'zestimate')
    if check_convergence(old_centroids, centroids):
        break
pd.set_option('display.max_rows', len(data['zestimate']))
pd.set_option('display.float_format', lambda x: '%.0f' % x)
print(data[['zestimate', 'cluster']])