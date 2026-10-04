import numpy as np
import matplotlib.pyplot as plt
class class1:
    def fonk1(self, datafile):
        self.x, self.y, self.b1 = np.loadtxt(datafile, unpack=True)
    def fonk2(self, nsteps, min_val, max_val):
        b2 = np.linspace(min_val, max_val, num=nsteps)
        b3 = np.linspace(min_val, max_val, num=nsteps)
        b4 = (max_val - min_val) / nsteps
        b5 = (max_val - min_val) / nsteps
        self.a1 = 0
        self.a2 = 0
        self.b6 = np.zeros((nsteps, nsteps))
        for i, ai in enumerate(b2):
            for j, bj in enumerate(b3):
                a3 = 1
                for xi, yi, si in zip(self.x, self.y, self.b1):
                    a3 *= (
                        (1 / (np.sqrt(2 * np.pi) * si)) *
                        np.exp(-((yi - (ai * xi + bj)) ** 2) / (2 * si ** 2))
                    )
                self.b6[i, j] = a3
        self.b7 = np.sum(self.b6) * b4 * b5
        self.a1 = np.sum(b2[:, None] * self.b6 * b4 * b5 / self.b7)
        self.a2 = np.sum(b3[None, :] * self.b6 * b4 * b5 / self.b7)
        b8 = np.sum((b2[:, None] - self.a1) ** 2 * self.b6 * b4 * b5 / self.b7)
        b9 = np.sum((b3[None, :] - self.a2) ** 2 * self.b6 * b4 * b5 / self.b7)
        self.b10 = np.sqrt(b8)
        self.b11 = np.sqrt(b9)
        b12 = np.sum((b2[:, None] - self.a1) * (b3[None, :] - self.a2) * self.b6 * b4 * b5 / self.b7)
        self.b12 = b12
        self.b13 = self.b12 / (self.b10 * self.b11)
    def fonk3(self):
        plt.plot(self.x, self.y, 'o', b14 = 'Data')
        b15 = np.linspace(0, 10, 100)
        b16 = self.a1 * b15 + self.a2
        plt.plot(b15, b16, b14 = 'Model')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Least Squares Model Fit')
        plt.legend()
        plt.show()
