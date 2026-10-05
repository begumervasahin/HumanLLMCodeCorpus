import numpy as np
from sklearn.datasets import make_blobs
def create_circles(num_points=209):
    theta = np.linspace(0, 2 * np.pi, num_points)
    circle1 = generate_circle_points(theta, 1)
    circle2 = generate_circle_points(theta, 2)
    circle3 = generate_circle_points(theta, 3)
    circle4 = generate_circle_points(theta, 4)
    circles = np.concatenate((circle1, circle2, circle3, circle4), axis=1)
    return circles.T
def generate_circle_points(theta, radius):
    return np.array([
        radius * np.cos(theta) + 0.1 * np.random.randn(len(theta)),
        radius * np.sin(theta) + 0.1 * np.random.randn(len(theta))
    ])
def create_blobs(num_samples=3000, num_features=2, cluster_std=1.0, random_state=99):
    centers = [(-8, -8), (0, 0), (8, 8), (20, 20), (-20, -20)]
    X, _ = make_blobs(n_samples=num_samples, n_features=num_features, cluster_std=cluster_std, centers=centers, shuffle=False, random_state=random_state)
    return X