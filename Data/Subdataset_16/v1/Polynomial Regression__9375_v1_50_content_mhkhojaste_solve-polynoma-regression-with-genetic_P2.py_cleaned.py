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
    def fonk2(self, r, s):
        self.a4 = r
        self.a5 = s
    def fonk3(self):
        return np.random.uniform(b4 = 0, high=1, size=(self.a2, self.a6))
    def fonk4(self, my_array):
        b5 = np.zeros(len(my_array))
        for i in range(my_array.shape[0]):
            b6 = (my_array[i][0] * np.power(self.b1, 3) +
                    my_array[i][1] * np.power(self.b1, 2) +
                    my_array[i][2] * self.b1 +
                    my_array[i][3])
            b5[i] = 1 / (1 + np.sum(np.power(np.subtract(b6, self.b3), 2)) / len(b6))
        return b5
    def fonk5(self, b20, b5):
        b7 = np.zeros(shape=(10, self.a6))
        for i in range(10):
            b8 = np.arange(len(b20))
            np.random.shuffle(b8)
            b8 = b8[:2]
            b9 = []
            for j in range(len(b8)):
                b9.append(b5[b8[j]])
            b9.sort(b10 = True)
            b7[i] = b20[b5.tolist().index(b9[0])]
        return b7
    def fonk6(self, b20):
        b11 = []
        for i in range(len(b20)):
            for j in range(i + 1, len(b20)):
                b12 = b20[i]
                b13 = b20[j]
                b14 = np.arange(self.a6)
                np.random.shuffle(b14)
                b15 = [b12[b14[0]], b12[b14[1]], b13[b14[2]], b13[b14[3]]]
                b16 = np.random.uniform(b4=0, high=100, size=self.a6)
                for k in range(len(b16)):
                    if b16[k] / 100 <= self.a4:
                        b15[k] += np.random.normal(0, self.a5, 1)[0]
                b11.append(b15)
        return np.asarray(b11)
if b17 = = "__main__":
    b18 = class1()
    b18.fonk2(0.2, 0.5)
    b19 = b18.fonk3()
    b5 = b18.fonk4(b19)
    b20 = b18.fonk5(b19, b5)
    b11 = b18.fonk6(b20)
    print("Initial Population:\n", b19)
    print("Fitness Scores:\n", b5)
    print("Selected Parents:\n", b20)
    print("Children:\n", b11)