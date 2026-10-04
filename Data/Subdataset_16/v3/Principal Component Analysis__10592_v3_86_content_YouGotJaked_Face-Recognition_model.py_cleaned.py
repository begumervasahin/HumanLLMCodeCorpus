import numpy as np
from preprocess import read_images, create_data_matrix
from subspace import pca, knn, predict, accuracy
class class1:
    def fonk1(self, b1, b4):
        self.b1 = b1
        self.images, self.b2 = read_images(self.b1)
        self.b3 = create_data_matrix(self.images)
        self.b4 = b4
class class2(class1):
    def fonk2(self, b1, b4):
        super().fonk3(b1, b4)
class class3(class1):
    def fonk3(self, b1, b4):
        super().fonk3(b1, b4)
    def fonk4(self, training_matrix):
        return [pca(training_matrix, self.b3, rank) for rank in self.b4]
    def fonk5(self, reduced, b2):
        return [fonk5(b11[0], b2) for b11 in reduced]
    def fonk6(self, b12, reduced):
        return [fonk6(knn, b4, b11[1], self.b2)
                for knn, b4, b11 in zip(b12, self.b4, reduced)]
    def fonk7(self, b12, reduced):
        return [fonk7(knn, b4, b11[1], self.b2)
                for knn, b4, b11 in zip(b12, self.b4, reduced)]
if b5 = = "__main__":
    b6 = 'b1/to/training/data'
    b7 = 'b1/to/testing/data'
    b8 = [10, 20, 30]
    b9 = class2(b6, b8)
    b10 = class3(b7, b8)
    b11 = b10.fonk4(b9.b3)
    b12 = b10.fonk5(b11, b9.b2)
    b13 = b10.fonk6(b12, b11)
    b14 = b10.fonk7(b12, b11)
    print("Predictions:", b13)
    print("Accuracies:", b14)