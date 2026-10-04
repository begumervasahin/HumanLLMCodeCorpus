from sklearn.neighbors import NearestNeighbors
import numpy as np
def main():
    X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
    nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree')
    nbrs.fit(X)
    print(nbrs)
    distances, indices = nbrs.kneighbors(X)
    print("Distances:\n", distances)
    print("Indices:\n", indices)
if __name__ == "__main__":
    main()