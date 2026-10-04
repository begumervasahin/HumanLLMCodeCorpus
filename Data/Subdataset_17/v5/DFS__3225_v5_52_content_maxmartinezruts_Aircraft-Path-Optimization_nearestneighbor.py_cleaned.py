from sklearn.neighbors import NearestNeighbors
import numpy as np
def create_sample_dataset():
    return np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
def train_nearest_neighbors_model(X, n_neighbors=2, algorithm='ball_tree'):
    model = NearestNeighbors(n_neighbors=n_neighbors, algorithm=algorithm)
    model.fit(X)
    return model
def get_nearest_neighbors(model, X):
    distances, indices = model.kneighbors(X)
    return distances, indices
def display_results(model, distances, indices):
    print("Trained NearestNeighbors model:\n", model)
    print("\nDistances to nearest neighbors:\n", distances)
    print("\nIndices of nearest neighbors:\n", indices)
def main():
    X = create_sample_dataset()
    model = train_nearest_neighbors_model(X)
    distances, indices = get_nearest_neighbors(model, X)
    display_results(model, distances, indices)
if __name__ == "__main__":
    main()