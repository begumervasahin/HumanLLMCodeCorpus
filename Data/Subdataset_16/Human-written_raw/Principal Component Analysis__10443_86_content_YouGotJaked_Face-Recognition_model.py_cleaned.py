
import numpy as np
from preprocess import read_images, create_data_matrix
from subspace import pca, knn, predict, accuracy
class class1():
    def fonk1(self, b1, b4):
        self.b1 = b1
        self.images, self.b2 = read_images(self.b1)
        self.b3 = create_data_matrix(self.images)
        self.b4 = b4
class class2(class1):
    def fonk2(self, b1, b4):
        super(class2, self).fonk3(b1, b4)
class class3(class1):
    def fonk3(self, b1, b4):
        super(class3, self).fonk3(b1, b4)
    def fonk4(self, training_matrix):
        return [pca(training_matrix, self.b3, rank) for rank in self.b4]
    def fonk5(self, reduced, b2):
        return [fonk5(reduced[i][0], b2) for i,_ in enumerate(self.b4)]
    def fonk6(self, knn, reduced):
        return [fonk6(knn[i], self.b4[i], reduced[i][1], self.b2) for i,_ in enumerate(self.b4)]
    def fonk7(self, knn, reduced):
        return [fonk7(knn[i], self.b4[i], reduced[i][1], self.b2) for i,_ in enumerate(self.b4)]