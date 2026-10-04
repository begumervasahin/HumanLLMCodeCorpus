import numpy as np
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
def create_circles():
    angles = np.arange(0, 2 * np.pi, 0.03)
    num_points = len(angles)
    circle1 = np.array([np.cos(angles) + 0.1 * np.random.randn(num_points),
                        np.sin(angles) + 0.1 * np.random.randn(num_points)]).T
    circle2 = np.array([2 * np.cos(angles) + 0.1 * np.random.randn(num_points),
                        2 * np.sin(angles) + 0.1 * np.random.randn(num_points)]).T
    circle3 = np.array([3 * np.cos(angles) + 0.1 * np.random.randn(num_points),
                        3 * np.sin(angles) + 0.1 * np.random.randn(num_points)]).T
    circle4 = np.array([4 * np.cos(angles) + 0.1 * np.random.randn(num_points),
                        4 * np.sin(angles) + 0.1 * np.random.randn(num_points)]).T
    circles_data = np.concatenate((circle1, circle2, circle3, circle4), axis=0)
    return circles_data
def create_blobs():
    centers = [(-8, -8), (0, 0), (8, 8), (20, 20), (-20, -20)]
    blobs_data, _ = make_blobs(n_samples=3000, n_features=2, cluster_std=1.0, centers=centers, shuffle=False, random_state=99)
    return blobs_data
circles_data = create_circles()
blobs_data = create_blobs()
plt.figure(figsize=(16, 8))
plt.subplot(1, 2, 1)
plt.title('Circles')
plt.scatter(circles_data[:, 0], circles_data[:, 1], s=5)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.subplot(1, 2, 2)
plt.title('Blobs')
plt.scatter(blobs_data[:, 0], blobs_data[:, 1], s=5)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.tight_layout()
plt.show()