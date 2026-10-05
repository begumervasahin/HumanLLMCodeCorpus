import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
import math
def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
def assign_labels(data, centroids):
    labels = []
    for point in data:
        distances = [calculate_distance(point[:2], centroid) for centroid in centroids]
        label = distances.index(min(distances)) + 1
        labels.append(label)
    return labels
def update_centroids(data, labels, k):
    new_centroids = []
    for i in range(1, k + 1):
        cluster_points = [data[j][:2] for j in range(len(data)) if labels[j] == i]
        centroid = [sum(coord) / len(cluster_points) for coord in zip(*cluster_points)]
        new_centroids.append(centroid)
    return new_centroids
df = pd.read_csv("kmeans.csv")
k = int(input("Please enter the number of centroids you would like to use (1-7): "))
if not 1 <= k <= 7:
    raise ValueError('Please enter a number between 1 and 7.')
centroids = [[random.uniform(df.iloc[:, 0].min(), df.iloc[:, 0].max()),
              random.uniform(df.iloc[:, 1].min(), df.iloc[:, 1].max())] for _ in range(k)]
data = df.values.tolist()
max_iterations = 1000
for _ in range(max_iterations):
    labels = assign_labels(data, centroids)
    new_centroids = update_centroids(data, labels, k)
    if new_centroids == centroids:
        break
    centroids = new_centroids
plt.scatter(df.iloc[:, 0], df.iloc[:, 1], c=labels, cmap=plt.cm.tab10)
for centroid in centroids:
    plt.scatter(centroid[0], centroid[1], color='black', marker='x', s=100)
plt.show()