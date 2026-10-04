
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
list_of_centroids = generate_centroids(data, 5, 'zestimate')
def create_clusters(centroids, house_data, column_name):
    avg_of_centroid_distances = []
    for centroid in centroids:
        distances = []
        for idx, house_value in house_data[column_name].items():
            distance = math.sqrt(abs(house_value - centroid) ** 2)
            distances.append(distance)
            house_data.at[idx, 'cluster'] = centroid
        avg_of_centroid_distances.append(sum(distances) / len(house_data))
    return avg_of_centroid_distances
clustering_results = create_clusters(list_of_centroids, data, 'zestimate')
def check_convergence(old_centroids, new_centroids, threshold=1):
    return all(abs(old - new) <= threshold for old, new in zip(old_centroids, new_centroids))
def kmeans(house_data, k, column_name, max_iterations=100):
    centroids = generate_centroids(house_data, k, column_name)
    for _ in range(max_iterations):
        old_centroids = centroids
        clustering_results = create_clusters(centroids, house_data, column_name)
        centroids = [np.mean(house_data[house_data['cluster'] == centroid][column_name]) for centroid in centroids]
        if check_convergence(old_centroids, centroids):
            break
    return house_data
result_data = kmeans(data, 5, 'zestimate')
print(result_data)
pd.set_option('display.max_rows', len(data['zestimate']))
pd.set_option('display.float_format', lambda x: '%.0f' % x)