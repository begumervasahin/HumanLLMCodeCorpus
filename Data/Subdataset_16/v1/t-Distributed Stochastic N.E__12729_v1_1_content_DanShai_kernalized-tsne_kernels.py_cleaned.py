import numpy as np
class class1:
    def fonk1(self, b7, b1 = {"kernel": "pca", "b3": .5, "degree": 1, "pcomp": 4}):
        self.b2 = b7.copy()
        self.b1 = b1
    def fonk2(self):
        b3 = self.b1["b3"]
        b4 = self.b1["degree"]
        b5 = self.b1["pcomp"]
        b6 = self.b1["kernel"]
        b7 = self.b2
        if b6 = = "poly":
            b2 = self.fonk6(b7, b3=b3, degree=b4, b8=b5).real
        elif b6 = = "anova":
            b2 = self.fonk11(b7, b3=b3, degree=b4, b8=b5).real
        elif b6 = = "rbf":
            b2 = self.fonk7(b7, b3=b3, b8=b5).real
        elif b6 = = "cosine":
            b2 = self.fonk8(b7, b8=b5).real
        elif b6 = = "iquad":
            b2 = self.fonk9(b7, b3=b3, degree=b4, b8=b5).real
        elif b6 = = "cauchy":
            b2 = self.fonk10(b7, b3=b3, b8=b5).real
        elif b6 = = "fourier":
            b2 = self.fonk12(b7, b3=b3, b8=b5).real
        else:
            b2 = self.fonk5(b7, b8=b5).real
        return b2
    def fonk3(self, M, b8 = 4):
        b11, b9 = np.linalg.eig(M)
        b10 = b11.argsort()[::-1]
        b11 = b11[b10].real
        b9 = b9[:, b10]
        b12 = b9[:, 0:b8]
        return b12
    def fonk4(self, b15):
        b13 = b15.shape[0]
        b14 = np.ones((b13, b13)) / b13
        b15 = b15 - b14.dot(b15) - b15.dot(b14) + b14.dot(b15).dot(b14)
        return b15
    def fonk5(self, b2, b8 = 2):
        b2 -= np.mean(b2, 0)
        b16 = np.cov(b2.T)
        b12 = self.fonk3(b16, b8=b8)
        b7 = np.dot(b2, b12)
        return b7
    def fonk6(self, b2, b3 = 1, degree=2, b8=2):
        b2 -= np.mean(b2, 0)
        b15 = (b3 * b2.dot(b2.T) + 1) ** degree
        b15 = self.fonk4(b15)
        return self.fonk3(b15, b8 = b8)
    def fonk7(self, b2, b3 = .1, b8=2):
        b2 -= np.mean(b2, 0)
        b17 = np.sum((b2[None, :] - b2[:, None])**2, -1)
        b15 = np.exp(-b3 * b17)
        b15 = self.fonk4(b15)
        return self.fonk3(b15, b8 = b8)
    def fonk8(self, b2, b8 = 2):
        b2 -= np.mean(b2, 0)
        b18 = ((b2 ** 2).sum(axis=1)).reshape(b2.shape[0], 1)
        b15 = b2.dot(b2.T) / (b18)
        b15 = self.fonk4(b15)
        return self.fonk3(b15, b8 = b8)
    def fonk9(self, b2, b3 = 1, degree=1, b8=2):
        b2 -= np.mean(b2, 0)
        b19 = np.sum((b2[None, :] - b2[:, None])**2, -1)
        b15 = 1. / (b19 + b3**2) ** degree
        b15 = self.fonk4(b15)
        return self.fonk3(b15, b8 = b8)
    def fonk10(self, b2, b3 = .2, b8=2):
        b2 -= np.mean(b2, 0)
        b19 = np.sum((b2[None, :] - b2[:, None])**2, -1)
        b15 = 1 / (1 + b19 * b3)
        b15 = self.fonk4(b15)
        return self.fonk3(b15, b8 = b8)
    def fonk11(self, b2, b3 = .01, degree=1, b8=2):
        b2 -= np.mean(b2, 0)
        b15 = np.zeros((b2.shape[0], b2.shape[0]))
        for d in range(b2.shape[1]):
            b20 = b2[:, d].reshape(-1, 1)
            b15 += np.exp(-b3 * (b20 - b20.T) ** 2) ** degree
        b15 = self.fonk4(b15)
        return self.fonk3(b15, b8 = b8)
    def fonk12(self, b2, b3 = .1, b8=2):
        b2 -= np.mean(b2, 0)
        b15 = np.ones((b2.shape[0], b2.shape[0]))
        b3 = min(.1, b3)
        for d in range(b2.shape[1]):
            b18 = b2[:, d].reshape(-1, 1)
            b15 *= (1 - b3 ** 2) / (2 * (1 - 2 * b3 * np.cos(b18 - b18.T)) + b3 ** 2)
        b15 = self.fonk4(b15)
        return self.fonk3(b15, b8 = b8)
if b21 = = "__main__":
    b22 = np.random.rand(100, 10)
    b23 = class1(b22, b1={"kernel": "rbf", "b3": 0.5, "pcomp": 3})
    b24 = b23.fonk2()
    print("Processed b22 shape:", b24.shape)