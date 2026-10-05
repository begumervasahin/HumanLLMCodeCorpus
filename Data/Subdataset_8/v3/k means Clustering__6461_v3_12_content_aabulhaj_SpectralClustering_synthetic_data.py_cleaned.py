import numpy as np
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
def create_circles():
    angles = np.arange(0, 2 * np.pi, 0.03)
    num_points = len(angles)
    noise_level = 0.1
    circle1 = generate_circle(angles, noise_level)
    circle2 = generate_circle(angles, noise_level, radius=2)
    circle3 = generate_circle(angles, noise_level, radius=3)
    circle4 = generate_circle(angles, noise_level, radius=4)
    return np.concatenate((circle1, circle2, circle3, circle4), axis=0)
def generate_circle(angles, noise_level, radius=1):
    circle_x = radius * np.cos(angles) + noise_level * np.random.randn(len(angles))
    circle_y = radius * np.sin(angles) + noise_level * np.random.randn(len(angles))
    return np.column_stack((circle_x, circle_y))
def create_blobs():
    centers = [(-8, -8), (0, 0), (8, 8), (20, 20), (-20, -20)]
    X, _ = make_blobs(n_samples=3000, n_features=2, cluster_std=1.0, centers=centers, shuffle=False, random_state=99)
    return X
circles_data = create_circles()
blobs_data = create_blobs()
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title('Circles')
plt.scatter(circles_data[:, 0], circles_data[:, 1], s=5)
plt.subplot(1, 2, 2)
plt.title('Blobs')
plt.scatter(blobs_data[:, 0], blobs_data[:, 1], s=5)
plt.tight_layout()
plt.show()