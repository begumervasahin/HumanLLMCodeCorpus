
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
def fonk1(b12):
    b1 = ['latitude', 'longitude', 'reviewCount', 'checkins']
    b2 = pd.read_csv(b12, sep=',', quotechar='"', header=0)
    return b2[b1]
def fonk2(b2, features):
    b3 = StandardScaler()
    b4 = b3.fit_transform(b2[features])
    return b4
def fonk3(b4, b5 = 4):
    b6 = KMeans(n_clusters=b5, random_state=42)
    b6.fit(b4)
    b7 = b6.predict(b4)
    b8 = b6.cluster_centers_
    return b6, b7, b8
def fonk4(b6, b8):
    print(f"Within-cluster sum of squares: {b6.inertia_:.2f}")
    for i, centroid in enumerate(b8, 1):
        print(f"Centroid {i}: b9 = {centroid[0]:.4f}, Longitude = {centroid[1]:.4f}")
def fonk5(b2, b7, b8):
    plt.figure(b10 = (10, 6))
    plt.scatter(b2['latitude'], b2['longitude'], b11 = b7, s=50, cmap='viridis', label='Cluster Points')
    plt.scatter(b8[:, 0], b8[:, 1], b11 = 'red', marker='*', s=200, alpha=0.5, label='Centroids')
    plt.title("Cluster Visualization of Yelp Data")
    plt.xlabel("b9")
    plt.ylabel("Longitude")
    plt.legend()
    plt.savefig('b9-Longitude.jpg')
    plt.show()
def fonk6():
    b12 = "./yelp.csv"
    b2 = fonk1(b12)
    b4 = fonk2(b2, ['latitude', 'longitude'])
    b6, b7, b8 = fonk3(b4)
    fonk4(b6, b8)
    fonk5(b2, b7, b8)
if b13 = = "__main__":
    fonk6()