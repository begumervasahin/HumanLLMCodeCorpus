import numpy as np
import matplotlib.pyplot as plt
class class1:
    def fonk1(self, datafile):
        self.x, self.y, self.b1 = np.loadtxt(datafile, unpack=True)
    def fonk2(self, nsteps, min_val, max_val):
        b2 = np.linspace(min_val, max_val, num=nsteps)
        b3 = np.linspace(min_val, max_val, num=nsteps)
        b4 = abs(max_val - min_val) / nsteps
        b5 = abs(max_val - min_val) / nsteps
        self.a1 = 0
        self.a2 = 0
        self.b6 = np.zeros((nsteps, nsteps))
        for i in range(nsteps):
            for j in range(nsteps):
                a3 = 1
                for k in range(len(self.x)):
                    a3 *= (1 / (np.sqrt(2 * np.pi) * self.b1[k])) * \
                                np.exp(-((self.y[k] - (b2[i] * self.x[k] + b3[j])) ** 2) / (2 * self.b1[k] ** 2))
                self.b6[i, j] = a3
        b7 = np.sum(self.b6) * b4 * b5
        self.b7 = b7
        for i in range(nsteps):
            for j in range(nsteps):
                self.a1 += b2[i] * self.b6[i, j] * b5 * b4 / self.b7
                self.a2 += b3[j] * self.b6[i, j] * b5 * b4 / self.b7
        self.b8 = np.sqrt(np.sum((b2[:, None] - self.a1) ** 2 * self.b6 * b5 * b4 / self.b7))
        self.b9 = np.sqrt(np.sum((b3[None, :] - self.a2) ** 2 * self.b6 * b5 * b4 / self.b7))
        self.b10 = np.sum((b2[:, None] - self.a1) * (b3[None, :] - self.a2) * self.b6 * b5 * b4 / self.b7)
        self.b11 = self.b10 / (self.b8 * self.b9)
    def fonk3(self):
        plt.plot(self.x, self.y, 'o', b12 = 'Data')
        b13 = np.linspace(0, 10, 100)
        b14 = self.a1 * b13 + self.a2
        plt.plot(b13, b14, b12 = 'Model')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.show()