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
        self.a6 = 4
        self.b2 = self.fonk2("my_numbers.csv")
    def fonk2(self, filename):
        b3 = pd.read_csv(filename)
        return b3["Y"].values
    def fonk3(self, a4, a5):
        self.a4 = a4
        self.a5 = a5
    def fonk4(self):
        return np.random.uniform(b4 = 0, high=1, size=(self.a2, self.a6))
    def fonk5(self, population):
        b5 = np.zeros(len(population))
        for i, individual in enumerate(population):
            b6 = (
                individual[0] * np.power(self.b1, 3) +
                individual[1] * np.power(self.b1, 2) +
                individual[2] * self.b1 +
                individual[3]
            )
            b5[i] = 1 / (1 + np.mean(np.square(b6 - self.b2)))
        return b5
    def fonk6(self, population, b5):
        b7 = np.zeros((10, self.a6))
        for i in range(10):
            b8 = np.random.choice(len(population), self.a3, replace=False)
            b9 = b8[np.argmax(b5[b8])]
            b7[i] = population[b9]
        return b7
    def fonk7(self, parents):
        b10 = []
        b11 = len(parents)
        for i in range(b11):
            for j in range(i + 1, b11):
                b12 = self.fonk8(parents[i], parents[j])
                b12 = self.fonk9(b12)
                b10.append(b12)
        return np.asarray(b10)
    def fonk8(self, parent1, parent2):
        b12 = np.zeros(self.a6)
        b13 = np.random.choice(self.a6, self.a6
        b12[b13] = parent1[b13]
        b12[~b13] = parent2[~b13]
        return b12
    def fonk9(self, b12):
        for gene_index in range(len(b12)):
            if np.random.rand() <= self.a4:
                b12[gene_index] += np.random.normal(0, self.a5)
        return b12