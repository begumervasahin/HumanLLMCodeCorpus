import numpy as np
from preprocess import read_images, create_data_matrix
from subspace import pca, knn, predict, accuracy
class Model:
    def __init__(self, path, K):
        self.path = path
        self.images, self.labels = read_images(self.path)
        self.matrix = create_data_matrix(self.images)
        self.K = K
class TrainingModel(Model):
    def __init__(self, path, K):
        super().__init__(path, K)
class TestingModel(Model):
    def __init__(self, path, K):
        super().__init__(path, K)
    def reduce(self, training_matrix):
        return [pca(training_matrix, self.matrix, rank) for rank in self.K]
    def knn(self, reduced, labels):
        return [knn(reduced_data[0], labels) for reduced_data in reduced]
    def predict(self, knn_models, reduced):
        return [predict(knn, K, reduced_data[1], self.labels)
                for knn, K, reduced_data in zip(knn_models, self.K, reduced)]
    def accuracy(self, knn_models, reduced):
        return [accuracy(knn, K, reduced_data[1], self.labels)
                for knn, K, reduced_data in zip(knn_models, self.K, reduced)]
if __name__ == "__main__":
    training_path = 'path/to/training/data'
    testing_path = 'path/to/testing/data'
    K_values = [10, 20, 30]
    training_model = TrainingModel(training_path, K_values)
    testing_model = TestingModel(testing_path, K_values)
    reduced_data = testing_model.reduce(training_model.matrix)
    knn_models = testing_model.knn(reduced_data, training_model.labels)
    predictions = testing_model.predict(knn_models, reduced_data)
    accuracies = testing_model.accuracy(knn_models, reduced_data)
    print("Predictions:", predictions)
    print("Accuracies:", accuracies)