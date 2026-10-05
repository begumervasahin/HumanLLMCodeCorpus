import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
import math
df = pd.read_csv("kmeans.csv")
rows = df.shape[0]
cols = df.shape[1]
points = []
scores = []
def distance(x, y, centroid=[]):
    a = centroid[0]
    b = centroid[1]
    i = abs(b - y)
    j = abs(a - x)
    k = math.sqrt(i ** 2 + j ** 2)
    return k
def label_point(x, y, centroids=[]):
    minimum_distance = 100000
    label = 1
    counter = 1
    for i in centroids:
        d = distance(x, y, i)
        if d < minimum_distance:
            label = counter
            minimum_distance = d
        counter += 1
    return label
def get_labels(points=[]):
    labels = []
    for i in points:
        labels.append(i[2])
    return labels
N = int(input("Please enter the number of centroids you would like to use (1-7): "))
if N <= 0 or N >= 8:
    raise ValueError('Please enter a number between 1 and 7.')
centroids = []
for i in range(N):
    a = round(random.uniform(0, df.mean()[0]), 1)
    b = round(random.uniform(0, df.mean()[1]), 1)
    centroid = [a, b]
    centroids.append(centroid)
for i in range(rows):
    point = df.iloc[i, :]
    x = point[0]
    y = point[1]
    label = label_point(x, y, centroids)
    point = [x, y, label]
    points.append(point)
for _ in range(N):
    for j in range(len(centroids)):
        centroid = centroids[j]
        x_avg = 0
        y_avg = 0
        count = 0
        for k in points:
            if k[2] == j + 1:
                x_avg += k[0]
                y_avg += k[1]
                count += 1
        if count == 0:
            count = 2
        x_avg = x_avg / count
        y_avg = y_avg / count
        centroids[j][0] = x_avg
        centroids[j][1] = y_avg
    for i in range(len(points)):
        point = points[i]
        x = point[0]
        y = point[1]
        label = label_point(x, y, centroids)
        points[i][2] = label
x = df.iloc[:, 0]
y = df.iloc[:, 1]
label = get_labels(points)
colors = ['red', 'green', 'blue', 'purple', 'cyan', 'magenta', 'yellow', 'pink']
plt.scatter(x, y, c=label, cmap=matplotlib.colors.ListedColormap(colors))
color = ['black']
for i in centroids:
    plt.scatter(i[0], i[1], color=color)
plt.show()