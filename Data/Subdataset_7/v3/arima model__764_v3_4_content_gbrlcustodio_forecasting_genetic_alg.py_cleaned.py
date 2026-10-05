import random
import copy
import numpy as np
import train_rbfn
from itertools import repeat, combinations
from cromossome import Cromossome
class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
        self.b3 = []
        self.a1 = 2
        self.b4 = len(b1["INPUT"]) - 1
        self.b5 = np.asarray([[x.tolist()] for x in b1["INPUT"].values])
        self.b6 = np.asarray([[x.tolist()] for x in b1["OUTPUT"].values])
    def fonk2(self, size):
        for _ in repeat(None, size):
            b7 = Cromossome()
            b7.b8 = random.sample(range(len(self.b1["INPUT"])), random.randint(self.a1, self.b4))
            self.b3.append(b7)
    def fonk3(self, chromosome):
        b9 = []
        for center_idx in chromosome:
            b9.append([self.b1["INPUT"].values[center_idx].tolist()])
        return np.asarray(b9)
    def fonk4(self, chromosome):
        b10 = train_rbfn.train(self.b5, self.b6, self.fonk3(chromosome.b8))
        chromosome.b11 = [b10.aic(self.b1), b10.aic(self.b2)]
    def fonk5(self, generations):
        for generation in range(1, generations + 1):
            print("Generation ", generation)
            self.fonk6()
            self.fonk7()
            b12 = self.fonk13()
            self.b3 = b12
        b13 = self.fonk14()
        print(self.fonk3(b13.b8))
        return train_rbfn.train(self.b5, self.b6, self.fonk3(b13.b8))
    def fonk6(self):
        for b7 in self.b3:
            self.fonk4(b7)
    def fonk7(self):
        b14 = sorted(self.b3, b29=lambda x: x.b15, reverse=True)
        for i, b7 in enumerate(b14):
            b7.b15 = i + 1
    def fonk8(self):
        b16 = sum(b7.b15 for b7 in self.b3)
        b17 = random.uniform(0, b16)
        a2 = 0
        for b7 in self.b3:
            a2 += b7.b15
            if a2 > b17:
                return b7
    def fonk9(self, b27):
        smaller, b18 = sorted(b27, b29=lambda x: len(x.b8))
        b19 = set(smaller.b8).intersection(b18.b8)
        b20 = list(set(smaller.b8) - b19)
        b21 = list(set(b18.b8) - b19)
        if b20:
            b22 = random.randint(1, len(b20))
            b23 = random.sample(b20, b22)
            if b21:
                b24 = random.sample(b21, b22)
                for i, j in zip(b23, b24):
                    smaller.b8[smaller.b8.index(i)], b18.b8[b18.b8.index(j)] = b18.b8[b18.b8.index(j)], smaller.b8[smaller.b8.index(i)]
        return [smaller, b18]
    def fonk10(self, chromosome):
        for idx, gene in enumerate(chromosome.b8):
            if random.random() <= 0.01:
                chromosome.b8[idx] = random.sample(set(range(len(self.b1["INPUT"]))).difference(chromosome.b8), 1)[0]
    def fonk11(self, chromosome):
        if random.random() <= 0.01:
            b25 = random.randint(0, len(chromosome.b8) - 1)
            b26 = b25 + random.randint(1, len(chromosome.b8) - b25 - 1)
            chromosome.b8 = [gene for idx, gene in enumerate(chromosome.b8) if idx < b25 or idx >= b26]
    def fonk12(self, chromosome):
        if random.random() <= 0.01 and len(chromosome.b8) < self.b4:
            b22 = random.randint(1, self.b4 - len(chromosome.b8))
            chromosome.b8.extend(random.sample(set(range(len(self.b1["INPUT"]))).difference(chromosome.b8), b22))
    def fonk13(self):
        b12 = []
        while len(b12) < len(self.b3):
            b27 = [self.fonk8() for _ in range(2)]
            b28 = self.fonk9(b27) if random.random() <= 0.90 else [copy.deepcopy(parent) for parent in b27]
            for child in b28:
                self.fonk10(child)
                self.fonk11(child)
                self.fonk12(child)
                self.fonk4(child)
                b12.append(child)
        return b12
    def fonk14(self):
        return max(self.b3, b29 = lambda x: x.b15)