import numpy as np
class class1:
    def fonk1(self, b2, b1 = {"kernel": "pca", "b3": .5, "degree": 1, "pcomp": 4}):
        self.b2 = b2.copy()
        self.b1 = b1
    def fonk2(self):
        b3 = self.b1["b3"]
        b4 = self.b1["degree"]
        b5 = self.b1["pcomp"]
        b6 = self.b1["kernel"]
        b2 = self.b2
        if b6 = = "poly":
            b7 = self.fonk6(b2, b3=b3, degree=b4, b8=b5).real
        elif b6 = = "anova":
            b7 = self.fonk11(b2, b3=b3, degree=b4, b8=b5).real
        elif b6 = = "rbf":
            b7 = self.fonk7(b2, b3=b3, b8=b5).real
        elif b6 = = "cosine":
            b7 = self.fonk8(b2, b8=b5).real
        elif b6 = = "iquad":
            b7 = self.fonk9(b2, b3=b3, degree=b4, b8=b5).real
        elif b6 = = "cauchy":
            b7 = self.fonk10(b2, b3=b3, b8=b5).real
        elif b6 = = "fourier":
            b7 = self.fonk12(b2, b3=b3, b8=b5).real
        else:
            b7 = self.fonk5(b2, b8=b5).real
        return b7
    def fonk3(self, matrix, b8 = 4):
        b11, b9 = np.linalg.eig(matrix)
        b10 = b11.argsort()[::-1]
        b11 = b11[b10].real
        print("---------------- b11: ----------------")
        print(b8, b11.shape)
        print(b11[:b8])
        print('---------------------------------------------')
        b9 = b9[:, b10]
        b12 = b9[:, :b8]
        return b12
    def fonk4(self, b18):
        b13 = b18.shape[0]
        b14 = np.ones((b13, b13)) / b13
        b15 = (
            b18 - b14.dot(b18) - b18.dot(b14) + b14.dot(b18).dot(b14)
        )
        return b15
    def fonk5(self, b2, b8 = 2):
        (n, d) = b2.shape
        b2 -= np.mean(b2, b16 = 0)
        b17 = np.cov(b2.T)
        b9 = self.fonk3(b17, b8=b8)
        b7 = np.dot(b2, b9)
        return b7
    def fonk6(self, b2, b3 = 1, degree=2, b8=2):
        b2 -= np.mean(b2, b16 = 0)
        b18 = (b3 * b2.dot(b2.T) + 1) ** degree
        b15 = self.fonk4(b18)
        return self.fonk3(b15, b8 = b8)
    def fonk7(self, b2, b3 = .1, b8=2):
        b2 -= np.mean(b2, b16 = 0)
        b19 = np.sum((b2[None, :] - b2[:, None]) ** 2, b16=-1)
        b18 = np.exp(-b3 * b19)
        b15 = self.fonk4(b18)
        return self.fonk3(b15, b8 = b8)
    def fonk8(self, b2, b8 = 2):
        b2 -= np.mean(b2, b16 = 0)
        b20 = ((b2 ** 2).sum(b16=1)).reshape(b2.shape[0], 1)
        b18 = b2.dot(b2.T) / b20
        b15 = self.fonk4(b18)
        return self.fonk3(b15, b8 = b8)
    def fonk9(self, b2, b3 = 1, degree=1, b8=2):
        b2 -= np.mean(b2, b16 = 0)
        b21 = np.sum((b2[None, :] - b2[:, None]) ** 2, b16=-1)
        b18 = 1. / (b21 + b3 ** 2) ** degree
        b15 = self.fonk4(b18)
        return self.fonk3(b15, b8 = b8)
    def fonk10(self, b2, b3 = .2, b8=2):
        b2 -= np.mean(b2, b16 = 0)
        b21 = np.sum((b2[None, :] - b2[:, None]) ** 2, b16=-1)
        b18 = 1 / (1 + b21 * b3)
        b15 = self.fonk4(b18)
        return self.fonk3(b15, b8 = b8)
    def fonk11(self, b2, b3 = .01, degree=1, b8=2):
        b2 -= np.mean(b2, b16 = 0)
        b18 = np.zeros((b2.shape[0], b2.shape[0]))
        for d in range(b2.shape[1]):
            b22 = b2[:, d].reshape(-1, 1)
            b18 += np.exp(-b3 * (b22 - b22.T) ** 2) ** degree
        b15 = self.fonk4(b18)
        return self.fonk3(b15, b8 = b8)
    def fonk12(self, b2, b3 = .1, b8=2):
        b2 -= np.mean(b2, b16 = 0)
        b18 = np.ones((b2.shape[0], b2.shape[0]))
        b3 = min(.1, b3)
        for d in range(b2.shape[1]):
            b22 = b2[:, d].reshape(-1, 1)
            b18 *= (1 - b3 ** 2) / (2 * (1 - 2 * b3 * np.cos(b22 - b22.T)) + b3 ** 2)
        b15 = self.fonk4(b18)
        return self.fonk3(b15, b8 = b8)