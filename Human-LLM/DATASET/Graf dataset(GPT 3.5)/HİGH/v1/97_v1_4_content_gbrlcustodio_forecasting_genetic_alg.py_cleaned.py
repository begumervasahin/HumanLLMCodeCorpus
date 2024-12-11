import random
import copy
import numpy as np
import train_rbfn
from itertools import repeat, combinations
from cromossome import Cromossome
from math import log
class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
        self.b3 = []
        self.a1 = 2
        self.b4 = b1["INPUT"].size - 1
        self.b5 = np.asarray([[x.tolist()] for x in b1["INPUT"].values])
        self.b6 = np.asarray([[x.tolist()] for x in b1["OUTPUT"].values])
    def fonk2(self, size):
        for _ in repeat(None, size):
            b7 = Cromossome()
            b7.b8 = random.sample(range(0, len(self.b1["INPUT"])), random.randint(self.a1, self.b4))
            self.b3.append(b7)
    def fonk3(self, cromossome):
        b9 = []
        for center in cromossome:
            b9.append([self.b1["INPUT"].values[center].tolist()])
        return np.asarray(b9)
    def fonk4(self, cromossome):
        b10 = train_rbfn.train(self.b5, self.b6, self.fonk3(cromossome.b8))
        cromossome.b11 = [b10.aic(self.b1), b10.aic(self.b2)]
    def fonk5(self, generations):
        a2 = 1
        for _ in repeat(None, generations):
            print("Generation ", a2)
            a2 += 1
            for b7 in self.b3:
                self.fonk4(b7)
            self.fonk7()
            b12 = []
            while len(b12) < len(self.b3):
                b13 = [self.fonk8() for _ in range(2)]
                b14 = self.fonk9(b13) if random.random() <= 0.90 else [copy.deepcopy(i) for i in b13]
                for offspring in b14:
                    self.fonk10(offspring)
                    self.fonk11(offspring)
                    self.fonk12(offspring)
                    if offspring.b8 != b13[0].b8 and offspring.b8 != b13[1].b8:
                        self.fonk4(offspring)
                        b13.append(offspring)
                b15 = []
                while len(b15) < 2:
                    for b7 in b13:
                        b7.b16 = True
                    self.fonk6(b13)
                    b15.extend([b7 for b7 in b13 if b7.b16][:2 - len(b15)])
                    b13 = [e for e in b13 if not e.b16]
                b12.extend(b15)
            self.b3 = b12
        for b7 in self.b3:
            b7.b16 = True
        self.fonk6(self.b3)
        b17 = [b7 for b7 in self.b3 if b7.b16][0]
        print(self.fonk3(b17.b8))
        return train_rbfn.train(self.b5, self.b6, self.fonk3(b17.b8))
    def fonk6(self, population):
        for a, b in combinations(population, 2):
            if a.partially_less_than(b):
                b.b16 = False
            elif b.partially_less_than(a):
                a.b16 = False
    def fonk7(self):
        b18 = []
        a3 = 0
        while self.b3:
            for b7 in self.b3:
                b7.b16 = True
            self.fonk6(self.b3)
            for b7 in self.b3:
                if b7.b16:
                    b7.b19 = len(self.b3) - a3
                    b18.append(b7)
            self.b3 = [b7 for b7 in self.b3 if not b7.b16]
            a3 += 1
        self.b3 = b18
    def fonk8(self):
        b20 = sum(b7.b19 for b7 in self.b3)
        b21 = random.uniform(0, b20)
        a4 = 0
        for b7 in self.b3:
            a4 += b7.b19
            if a4 > b21:
                return b7
    def fonk9(self, b13):
        if len(b13[0].b8) <= len(b13[-1].b8):
            b23, b22 = [copy.deepcopy(parent) for parent in b13]
        else:
            b22, b23 = [copy.deepcopy(parent) for parent in b13]
        b24 = set(b23.b8).intersection(b22.b8)
        b25 = list(set(b23.b8) - b24)
        if b25:
            b26 = random.randint(1, len(b25))
            b27 = [b25[i] for i in sorted(random.sample(range(len(b25)), b26))]
            b25 = list(set(b22.b8) - b24)
            if b25:
                b28 = [b25[i] for i in sorted(random.sample(range(len(b25)), b26))]
                b29 = [b23.b8.index(item) for item in b27]
                b30 = [b22.b8.index(item) for item in b28]
                for i, j in zip(b29, b30):
                    b23.b8[i], b22.b8[j] = b22.b8[j], b23.b8[i]
        return [b23, b22]
    def fonk10(self, cromossome):
        for locus in range(len(cromossome.b8)):
            if random.random() <= 0.01:
                cromossome.b8[locus] = random.sample(set(range(0, len(self.b1["INPUT"]))).difference(cromossome.b8), 1)[0]
    def fonk11(self, cromossome):
        if random.random() <= 0.01:
            b31 = random.randint(0, len(cromossome.b8) - 1)
            b32 = b31 + random.randint(1, len(cromossome.b8) - b31)
            if (b32 - b31) == len(cromossome.b8):
                b32 -= 1
            cromossome.b8 = [gene for index, gene in enumerate(cromossome.b8) if index not in range(b31, b32)]
    def fonk12(self, cromossome):
        if random.random() <= 0.01 and len(cromossome.b8) < self.b4:
            b26 = random.randint(1, self.b4 - len(cromossome.b8))
            cromossome.b8.extend(random.sample(set(range(0, len(self.b1["INPUT"]))).difference(cromossome.b8), b26))