import pandas as pd
import numpy as np
import random
import math
def read_csvfile(filename):
    return pd.read_csv(filename)
city = "san-francisco-ca"
filename = f"data/propertyInfo/{city}.csv"
data = read_csvfile(filename)
data["cluster"] = -1
def generate_centroids(data, k, column_name):
    return [random.randint(1, data[column_name].max()) for _ in range(k)]
list_of_centroids = generate_centroids(data, 5, 'zestimate')
def assign_clusters(centroids, data, column_name):
    houses = data[column_name]
    for x, centroid in enumerate(centroids):
        for idx, house in enumerate(houses):
            offset = len(houses) * x
            home = np.asscalar(house.astype(int))
            data.loc[idx + offset, 'cluster'] = centroid
assign_clusters(list_of_centroids, data, 'zestimate')
def calculate_avg_distance(centroids, data, column_name):
    houses = data[column_name]
    avg_distances = []
    for x, centroid in enumerate(centroids):
        distances = []
        for idx, house in enumerate(houses):
            offset = len(houses) * x
            home = np.asscalar(house.astype(int))
            distance = math.sqrt(abs(home - centroid) ** 2)
            distances.append(distance)
        avg_distance = sum(distances) / len(distances)
        avg_distances.append(avg_distance)
    return avg_distances
clustering_function = calculate_avg_distance(list_of_centroids, data, 'zestimate')
def check_convergence(old_centroids, new_centroids):
    return all(abs(old - new) <= 1 for old, new in zip(old_centroids, new_centroids))
while True:
    old_centroids = list_of_centroids.copy()
    list_of_centroids = generate_centroids(data, 5, 'zestimate')
    assign_clusters(list_of_centroids, data, 'zestimate')
    if check_convergence(old_centroids, list_of_centroids):
        break
pd.set_option('display.max_rows', len(data['zestimate']))
pd.set_option('display.float_format', lambda x: '%.0f' % x)
print(data[['zestimate', 'cluster']])