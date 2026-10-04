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
    def fonk2(self, a4, a5):
        self.a4 = a4
        self.a5 = a5
    def fonk3(self):
        return np.random.uniform(b4 = 0, high=1, size=(self.a2, self.a6))
    def fonk4(self, population):
        b5 = np.zeros(len(population))
        for i in range(population.shape[0]):
            b6 = (
                population[i][0] * np.power(self.b1, 3) +
                population[i][1] * np.power(self.b1, 2) +
                population[i][2] * self.b1 +
                population[i][3]
            )
            b5[i] = 1 / (1 + np.sum(np.power(b6 - self.b3, 2)) / len(b6))
        return b5
    def fonk5(self, population, b5):
        b7 = np.zeros((10, self.a6))
        for i in range(10):
            b8 = np.random.choice(len(population), self.a3, replace=False)
            b9 = b5[b8]
            b10 = b8[np.argmax(b9)]
            b7[i] = population[b10]
        return b7
    def fonk6(self, parents):
        b11 = []
        b12 = len(parents)
        for i in range(b12):
            for j in range(i + 1, b12):
                b13 = parents[i]
                b14 = parents[j]
                b15 = np.zeros(self.a6)
                b16 = np.random.choice(self.a6, self.a6
                b15[b16] = b13[b16]
                b15[~b16] = b14[~b16]
                b15 = self.fonk7(b15)
                b11.append(b15)
        return np.asarray(b11)
    def fonk7(self, b15):
        for gene_index in range(len(b15)):
            if np.random.rand() <= self.a4:
                b15[gene_index] += np.random.normal(0, self.a5)
        return b15