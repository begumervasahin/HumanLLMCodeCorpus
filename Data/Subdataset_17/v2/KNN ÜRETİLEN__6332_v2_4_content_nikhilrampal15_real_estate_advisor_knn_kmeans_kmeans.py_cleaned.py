
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
def create_clusters(centroids, house_data, column_name):
    houses = house_data[column_name].values
    total_distances = []
    for centroid in centroids:
        distance_to_centroid = [
            math.sqrt((home - centroid)**2) for home in houses
        ]
        house_data['cluster'] = centroid
        total_distances.append(sum(distance_to_centroid))
    avg_distances = [dist / len(total_distances) for dist in total_distances]
    return avg_distances
average_distances = create_clusters(initial_centroids, data, 'zestimate')
def check_convergence(previous, current):
    for old, new in zip(previous, current):
        if abs(old - new) > 1:
            new_centroids = generate_centroids(data, 5, 'zestimate')
            return create_clusters(new_centroids, data, 'zestimate')
    return current
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.0f' % x)
converged_centroids = check_convergence(average_distances, initial_centroids)
print(converged_centroids)