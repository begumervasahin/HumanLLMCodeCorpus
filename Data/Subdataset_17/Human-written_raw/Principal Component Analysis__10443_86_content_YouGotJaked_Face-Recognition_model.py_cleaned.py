
import numpy as np
from preprocess import read_images, create_data_matrix
from subspace import pca, knn, predict, accuracy
class Model():
    def __init__(self, path, K):
        self.path = path
        self.images, self.labels = read_images(self.path)
        self.matrix = create_data_matrix(self.images)
        self.K = K
class TrainingModel(Model):
    def __init__(self, path, K):
        super(TrainingModel, self).__init__(path, K)
class TestingModel(Model):
    def __init__(self, path, K):
        super(TestingModel, self).__init__(path, K)
    def reduce(self, training_matrix):
        return [pca(training_matrix, self.matrix, rank) for rank in self.K]
    def knn(self, reduced, labels):
        return [knn(reduced[i][0], labels) for i,_ in enumerate(self.K)]
    def predict(self, knn, reduced):
        return [predict(knn[i], self.K[i], reduced[i][1], self.labels) for i,_ in enumerate(self.K)]
    def accuracy(self, knn, reduced):
        return [accuracy(knn[i], self.K[i], reduced[i][1], self.labels) for i,_ in enumerate(self.K)]