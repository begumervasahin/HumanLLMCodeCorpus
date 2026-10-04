import numpy as np
import scipy.special
class class1:
    def fonk1(self, b2, b1 = False):
        self.b2 = b2
        self.b1 = b1
    def fonk2(self, b13):
        b3 = b13 - np.mean(b13, b6=0)
        U, S, b4 = np.linalg.svd(b3, full_matrices=False)
        b5 = U @ np.diag(S)[:, :self.b2]
        if self.b1:
            b5 /= np.std(b5, b6 = 0)
        return b5
class class2:
    def fonk3(self, gradients):
        return [0.01 * grad for grad in gradients]
class class3:
    def fonk4(self, b13, epochs, b15):
        n_samples, b7 = b13.shape
        b8 = class1(b7, b1=True)
        b9 = b8.fonk4(b13)
        self.b10 = np.random.rand(b7, b7)
        for epoch in range(epochs):
            b11 = np.zeros_like(self.b10)
            for x in b9:
                b11 += (1 - 2 * scipy.special.expit(self.b10 @ x.T)) @ x + np.linalg.inv(self.b10.T)
            b11 /= n_samples
            b12 = b15.fonk3([b11])[0]
            self.b10 += b12
        return b9 @ self.b10
def fonk5():
    np.random.seed(0)
    b13 = np.random.rand(100, 5)
    b14 = class3()
    b15 = class2()
    b16 = b14.fonk4(b13, epochs=1000, b15=b15)
    print(b16[:5])
if b17 = = "__main__":
    fonk5()