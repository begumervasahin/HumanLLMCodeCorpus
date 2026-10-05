import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random
import math
df = pd.read_csv("kmeans.csv")
points = []
centroids = []
def calculate_distance(x, y, centroid=[]):
    centroid_x, centroid_y = centroid
    distance_x = abs(centroid_x - x)
    distance_y = abs(centroid_y - y)
    distance = math.sqrt(distance_x ** 2 + distance_y ** 2)
    return distance
def assign_label(x, y, centroids=[]):
    min_distance = float('inf')
    label = 0
    for index, centroid in enumerate(centroids, start=1):
        distance = calculate_distance(x, y, centroid)
        if distance < min_distance:
            min_distance = distance
            label = index
    return label
def get_labels(points=[]):
    return [point[2] for point in points]
def get_num_centroids():
    while True:
        try:
            num_centroids = int(input("Please enter the number of centroids you would like to use (1-7): "))
            if 1 <= num_centroids <= 7:
                return num_centroids
            else:
                print("Please enter a number between 1 and 7.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
num_centroids = get_num_centroids()
for _ in range(num_centroids):
    centroid_x = round(random.uniform(0, df.mean()[0]), 1)
    centroid_y = round(random.uniform(0, df.mean()[1]), 1)
    centroids.append([centroid_x, centroid_y])
for _, point in df.iterrows():
    x, y = point
    label = assign_label(x, y, centroids)
    points.append([x, y, label])
for _ in range(num_centroids):
    for i, centroid in enumerate(centroids):
        sum_x, sum_y, count = 0, 0, 0
        for point in points:
            if point[2] == i + 1:
                sum_x += point[0]
                sum_y += point[1]
                count += 1
        centroid[0] = sum_x / count if count != 0 else centroid[0]
        centroid[1] = sum_y / count if count != 0 else centroid[1]
    for point in points:
        point[2] = assign_label(point[0], point[1], centroids)
x_values = df.iloc[:, 0]
y_values = df.iloc[:, 1]
labels = get_labels(points)
colors = ['red', 'green', 'blue', 'purple', 'cyan', 'magenta', 'yellow', 'pink']
plt.scatter(x_values, y_values, c=labels, cmap=plt.cm.tab10)
for centroid in centroids:
    plt.scatter(centroid[0], centroid[1], color='black')
plt.show()