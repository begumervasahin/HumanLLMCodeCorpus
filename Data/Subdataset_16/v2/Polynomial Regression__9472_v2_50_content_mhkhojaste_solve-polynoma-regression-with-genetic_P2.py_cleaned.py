import numpy as np
import pandas as pd
class class1:
    def fonk1(self):
        self.a1 = 10000
        self.a2 = 50
        self.a3 = 2
        self.a4 = 0.1
        self.a5 = 1
        self.b1 = np.arange(1, 101)
        b2 = pd.read_csv("my_numbers.csv")
        self.b3 = b2["Y"].values
        self.a6 = 4
    def fonk2(self, mutation_rate, a5):
        self.a4 = mutation_rate
        self.a5 = a5
    def fonk3(self):
        return np.random.uniform(b4 = 0, high=1, size=(self.a2, self.a6))
    def fonk4(self, b19):
        b5 = np.zeros(len(b19))
        for i in range(b19.shape[0]):
            b6 = (
                b19[i][0] * np.power(self.b1, 3) +
                b19[i][1] * np.power(self.b1, 2) +
                b19[i][2] * self.b1 +
                b19[i][3]
            )
            b7 = np.sum(np.power(np.subtract(b6, self.b3), 2)) / len(b6)
            b5[i] = 1 / (1 + b7)
        return b5
    def fonk5(self, b19, b5):
        b8 = np.zeros((10, self.a6))
        for i in range(10):
            b9 = np.random.choice(len(b19), size=self.a3, replace=False)
            b10 = b5[b9]
            b11 = b9[np.argmax(b10)]
            b8[i] = b19[b11]
        return b8
    def fonk6(self, b20):
        b12 = []
        for i in range(len(b20)):
            for j in range(i + 1, len(b20)):
                b13 = b20[i]
                b14 = b20[j]
                b15 = np.random.choice(self.a6, self.a6, replace=False)
                b16 = [b13[b15[0]], b13[b15[1]], b14[b15[2]], b14[b15[3]]]
                for k in range(self.a6):
                    if np.random.rand() <= self.a4:
                        b16[k] += np.random.normal(0, self.a5)
                b12.append(b16)
        return np.asarray(b12)
if b17 = = "__main__":
    b18 = class1()
    b18.fonk2(0.2, 0.5)
    b19 = b18.fonk3()
    print("Initial Population:\n", b19)
    b5 = b18.fonk4(b19)
    print("Fitness Scores:\n", b5)
    b20 = b18.fonk5(b19, b5)
    print("Selected Parents:\n", b20)
    b12 = b18.fonk6(b20)
    print("Children:\n", b12)