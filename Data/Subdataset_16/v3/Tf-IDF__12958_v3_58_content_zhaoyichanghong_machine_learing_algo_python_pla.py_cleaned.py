import numpy as np
from sklearn.metrics import accuracy_score
class class1:
    def fonk1(self, b6, b7):
        n_samples, b1 = b6.shape
        self.b2 = np.zeros(b1)
        self.a1 = 0
        while True:
            b3 = True
            for i in range(n_samples):
                b4 = self.fonk2(b6[i])
                if b7[i] * b4 <= 0:
                    self.b2 += b7[i] * b6[i]
                    self.a1 += b7[i]
                    b3 = False
            if b3:
                break
    def fonk2(self, x):
        return np.sign(np.dot(x, self.b2) + self.a1)
    def fonk3(self, b6):
        return np.sign(np.dot(b6, self.b2) + self.a1)
if b5 = = "__main__":
    b6 = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
    b7 = np.array([1, -1, 1, -1])
    b8 = class1()
    b8.fonk1(b6, b7)
    b9 = b8.fonk3(b6)
    print("Predictions:", b9)
    print("Accuracy:", accuracy_score(b7, b9))