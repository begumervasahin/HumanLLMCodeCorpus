import numpy as np
import pandas as pd
class class1:
    def fonk1(self, b1 = "my_numbers.csv"):
        self.a1 = 10000
        self.a2 = 50
        self.a3 = 2
        self.a4 = 0.1
        self.a5 = 1
        self.a6 = 4
        self.b2 = np.arange(1, 101)
        b3 = pd.read_csv(b1)
        self.b4 = b3["Y"].values
    def fonk2(self, a4, a5):
        self.a4 = a4
        self.a5 = a5
    def fonk3(self):
        return np.random.uniform(b5 = 0, high=1, size=(self.a2, self.a6))
    def fonk4(self, b20):
        b6 = np.zeros(len(b20))
        for i in range(b20.shape[0]):
            b7 = (
                b20[i][0] * np.power(self.b2, 3) +
                b20[i][1] * np.power(self.b2, 2) +
                b20[i][2] * self.b2 +
                b20[i][3]
            )
            b8 = np.sum(np.power(b7 - self.b4, 2)) / len(b7)
            b6[i] = 1 / (1 + b8)
        return b6
    def fonk5(self, b20, b6):
        b9 = np.zeros((10, self.a6))
        for i in range(10):
            b10 = np.random.choice(len(b20), size=self.a3, replace=False)
            b11 = b6[b10]
            b12 = b10[np.argmax(b11)]
            b9[i] = b20[b12]
        return b9
    def fonk6(self, b21):
        b13 = []
        for i in range(len(b21)):
            for j in range(i + 1, len(b21)):
                b14 = b21[i]
                b15 = b21[j]
                b16 = np.random.choice(self.a6, self.a6, replace=False)
                b17 = [b14[b16[0]], b14[b16[1]],
                         b15[b16[2]], b15[b16[3]]]
                for k in range(self.a6):
                    if np.random.rand() <= self.a4:
                        b17[k] += np.random.normal(0, self.a5)
                b13.append(b17)
        return np.asarray(b13)
if b18 = = "__main__":
    b19 = class1()
    b19.fonk2(0.2, 0.5)
    b20 = b19.fonk3()
    print("Initial Population:\n", b20)
    b6 = b19.fonk4(b20)
    print("Fitness Scores:\n", b6)
    b21 = b19.fonk5(b20, b6)
    print("Selected Parents:\n", b21)
    b13 = b19.fonk6(b21)
    print("Children:\n", b13)