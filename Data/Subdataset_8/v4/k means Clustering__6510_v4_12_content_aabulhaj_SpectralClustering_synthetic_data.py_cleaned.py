import numpy as np
from sklearn.datasets import make_blobs
def create_circles():
    theta = np.arange(0, 2 * np.pi, 0.03)
    num_points = len(theta)
    circle1 = np.array([np.cos(theta) + 0.1 * np.random.randn(num_points),
                        np.sin(theta) + 0.1 * np.random.randn(num_points)])
    circle2 = np.array([2 * np.cos(theta) + 0.1 * np.random.randn(num_points),
                        2 * np.sin(theta) + 0.1 * np.random.randn(num_points)])
    circle3 = np.array([3 * np.cos(theta) + 0.1 * np.random.randn(num_points),
                        3 * np.sin(theta) + 0.1 * np.random.randn(num_points)])
    circle4 = np.array([4 * np.cos(theta) + 0.1 * np.random.randn(num_points),
                        4 * np.sin(theta) + 0.1 * np.random.randn(num_points)])
    circles = np.concatenate((circle1, circle2, circle3, circle4), axis=1)
    return circles.T
def create_blobs():
    centers = [(-8, -8), (0, 0), (8, 8), (20, 20), (-20, -20)]
    X, _ = make_blobs(n_samples=3000, n_features=2, cluster_std=1.0, centers=centers, shuffle=False, random_state=99)
    return X