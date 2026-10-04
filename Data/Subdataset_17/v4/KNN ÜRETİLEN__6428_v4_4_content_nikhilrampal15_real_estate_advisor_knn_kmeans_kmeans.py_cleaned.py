
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
    centroids = [random.randint(1, house_data[column_name].max()) for _ in range(k)]
    return centroids
list_of_centroids = generate_centroids(data, 5, 'zestimate')
def create_clusters(centroids, house_data, column_name):
    sum_of_centroid_distances = []
    for centroid in centroids:
        distance_to_centroids = []
        for idx, house_value in house_data[column_name].items():
            distance = math.sqrt(abs(house_value - centroid) ** 2)
            distance_to_centroids.append(distance)
            house_data.at[idx, 'cluster'] = centroid
        sum_of_centroid_distances.append(sum(distance_to_centroids))
    avg_of_centroid_distances = [total / len(house_data) for total in sum_of_centroid_distances]
    return avg_of_centroid_distances
clustering_results = create_clusters(list_of_centroids, data, 'zestimate')
def check_convergence(old_centroids, new_centroids):
    old_centroids = list(map(int, old_centroids))
    new_centroids = list(map(int, new_centroids))
    for old, new in zip(old_centroids, new_centroids):
        if abs(old - new) > 1:
            new_centroids = generate_centroids(data, 5, 'zestimate')
            return create_clusters(new_centroids, data, 'zestimate')
    return new_centroids
pd.set_option('display.max_rows', len(data['zestimate']))
pd.set_option('display.float_format', lambda x: '%.0f' % x)
print(check_convergence(clustering_results, list_of_centroids))