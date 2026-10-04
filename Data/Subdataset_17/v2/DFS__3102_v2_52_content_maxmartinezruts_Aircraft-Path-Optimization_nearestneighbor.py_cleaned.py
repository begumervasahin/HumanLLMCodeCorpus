from sklearn.neighbors import NearestNeighbors
import numpy as np
def create_dataset():
    return np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
def fit_nearest_neighbors(X):
    nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree')
    nbrs.fit(X)
    return nbrs
def find_nearest_neighbors(nbrs, X):
    distances, indices = nbrs.kneighbors(X)
    return distances, indices
def main():
    X = create_dataset()
    nbrs = fit_nearest_neighbors(X)
    print("Fitted NearestNeighbors model:\n", nbrs)
    distances, indices = find_nearest_neighbors(nbrs, X)
    print("\nDistances to nearest neighbors:\n", distances)
    print("\nIndices of nearest neighbors:\n", indices)
if __name__ == "__main__":
    main()