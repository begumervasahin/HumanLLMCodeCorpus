
import numpy as np
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
def generate_circular_data(num_points=210, noise_level=0.1):
    angles = np.linspace(0, 2 * np.pi, num_points)
    radii = [1, 2, 3, 4]
    circles_data = []
    for r in radii:
        x = r * np.cos(angles) + noise_level * np.random.randn(num_points)
        y = r * np.sin(angles) + noise_level * np.random.randn(num_points)
        circles_data.append(np.vstack((x, y)).T)
    return np.vstack(circles_data)
def generate_blob_data(num_samples=3000, cluster_std=1.0, random_state=99):
    centers = [(-8, -8), (0, 0), (8, 8), (20, 20), (-20, -20)]
    X, _ = make_blobs(n_samples=num_samples, n_features=2, cluster_std=cluster_std, centers=centers, random_state=random_state)
    return X
circular_data = generate_circular_data()
blob_data = generate_blob_data()
plt.figure(figsize=(16, 8))
plt.subplot(1, 2, 1)
plt.title('Circles')
plt.scatter(circular_data[:, 0], circular_data[:, 1], s=5, color='blue')
plt.xlabel('X')
plt.ylabel('Y')
plt.subplot(1, 2, 2)
plt.title('Blobs')
plt.scatter(blob_data[:, 0], blob_data[:, 1], s=5, color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.tight_layout()
plt.show()