
import pandas as pd
import numpy as np
import random
import math
from read_csvfile import read_csvfile
city = "san-francisco-ca"
filename = f"data/propertyInfo/{city}.csv"
data = read_csvfile(filename)
data["cluster"] = -1
def generate_centroids(house_data, k, column_name):
    return [random.randint(1, house_data[column_name].max()) for _ in range(k)]
initial_centroids = generate_centroids(data, 5, 'zestimate')
def assign_clusters(centroids, house_data, column_name):
    houses = house_data[column_name].values
    total_distances = []
    house_data['cluster'] = -1
    for centroid in centroids:
        distance_to_centroid = [
            math.sqrt((home - centroid)**2) for home in houses
        ]
        house_data.loc[house_data[column_name].apply(lambda x: math.sqrt((x - centroid)**2)).idxmin(), 'cluster'] = centroid
        total_distances.append(sum(distance_to_centroid))
    avg_distances = [dist / len(houses) for dist in total_distances]
    return house_data, avg_distances
data, average_distances = assign_clusters(initial_centroids, data, 'zestimate')
def check_convergence(previous_centroids, current_centroids, tolerance=1.0):
    for old, new in zip(previous_centroids, current_centroids):
        if abs(old - new) > tolerance:
            return False
    return True
def update_centroids(house_data, column_name):
    new_centroids = house_data.groupby('cluster')[column_name].mean().tolist()
    return new_centroids
def k_means_clustering(house_data, k, column_name, max_iterations=100):
    centroids = generate_centroids(house_data, k, column_name)
    for _ in range(max_iterations):
        previous_centroids = centroids
        house_data, _ = assign_clusters(centroids, house_data, column_name)
        centroids = update_centroids(house_data, column_name)
        if check_convergence(previous_centroids, centroids):
            break
    return centroids
final_centroids = k_means_clustering(data, 5, 'zestimate')
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.0f' % x)
print("Final centroids:", final_centroids)
print("Clustered Data:")
print(data)