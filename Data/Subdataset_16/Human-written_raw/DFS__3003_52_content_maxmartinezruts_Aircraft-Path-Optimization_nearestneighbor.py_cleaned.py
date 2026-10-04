from sklearn.neighbors import NearestNeighbors
import numpy as np
b1 = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
b2 = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(b1)
print(b2)
distances, b3 = b2.kneighbors(b1)
print(distances,b3)