import random
import copy
import numpy as np
from itertools import combinations
from cromossome import Cromossome
from train_rbfn import train
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
        for _ in range(size):
            b7 = Cromossome()
            b7.b8 = random.sample(range(0, len(self.b1["INPUT"])), random.randint(self.a1, self.b4))
            self.b3.append(b7)
    def fonk3(self, chromosome):
        b9 = []
        for center_index in chromosome:
            b9.append([self.b1["INPUT"].values[center_index].tolist()])
        return np.asarray(b9)
    def fonk4(self, chromosome):
        b10 = train(self.b5, self.b6, self.fonk3(chromosome.b8))
        chromosome.b11 = [b10.aic(self.b1), b10.aic(self.b2)]
    def fonk5(self, generations):
        for generation in range(1, generations + 1):
            print("Generation", generation)
            self.fonk6()
            self.fonk7()
            b12 = []
            while len(b12) < len(self.b3):
                b13 = [self.fonk8() for _ in range(2)]
                b14 = self.fonk9(b13) if random.random() <= 0.90 else [copy.deepcopy(parent) for parent in b13]
                for child in b14:
                    self.fonk10(child)
                    self.fonk11(child)
                    self.fonk12(child)
                    if child.b8 != b13[0].b8 and child.b8 != b13[1].b8:
                        self.fonk4(child)
                        b13.append(child)
                b15 = []
                while len(b15) < 2:
                    for b7 in b13:
                        b7.b16 = True
                    self.fonk13(b13)
                    b15.extend([b7 for b7 in b13 if b7.b16][:2 - len(b15)])
                    b13 = [e for e in b13 if not e.b16]
                b12.extend(b15)
            self.b3 = b12
        self.fonk14()
        b17 = [b7 for b7 in self.b3 if b7.b16][0]
        print("Best configuration:", self.fonk3(b17.b8))
        return train(self.b5, self.b6, self.fonk3(b17.b8))
    def fonk6(self):
        for b7 in self.b3:
            self.fonk4(b7)
    def fonk7(self):
        self.b3.sort(b18 = lambda x: x.b11[0], reverse=True)
        for i, b7 in enumerate(self.b3):
            b7.b19 = i + 1
    def fonk8(self):
        b20 = sum(b7.b19 for b7 in self.b3)
        b21 = random.uniform(0, b20)
        a2 = 0
        for b7 in self.b3:
            a2 += b7.b19
            if a2 > b21:
                return b7
    def fonk9(self, b13):
        smaller_parent, b22 = min(b13, b18=lambda x: len(x.b8)), max(b13, b18=lambda x: len(x.b8))
        b23 = set(smaller_parent.b8).intersection(b22.b8)
        b24 = list(set(smaller_parent.b8) - b23)
        if b24:
            b25 = random.randint(1, len(b24))
            b26 = [gene for gene in random.sample(b24, b25)]
            b24 = list(set(b22.b8) - b23)
            if b24:
                b27 = [gene for gene in random.sample(b24, b25)]
                for gene1, gene2 in zip(b26, b27):
                    b28 = smaller_parent.b8.index(gene1)
                    b29 = b22.b8.index(gene2)
                    smaller_parent.b8[b28], b22.b8[b29] = b22.b8[b29], smaller_parent.b8[b28]
        return [copy.deepcopy(smaller_parent), copy.deepcopy(b22)]
    def fonk10(self, chromosome):
        for locus in range(len(chromosome.b8)):
            if random.random() <= 0.01:
                b30 = set(range(len(self.b1["INPUT"]))) - set(chromosome.b8)
                b31 = random.sample(b30, 1)[0]
                chromosome.b8[locus] = b31
    def fonk11(self, chromosome):
        if random.random() <= 0.01:
            b32 = random.randint(0, len(chromosome.b8) - 1)
            b33 = b32 + random.randint(1, len(chromosome.b8) - b32)
            if (b33 - b32) == len(chromosome.b8):
                b33 -= 1
            chromosome.b8 = [gene for index, gene in enumerate(chromosome.b8) if index not in range(b32, b33)]
    def fonk12(self, chromosome):
        if random.random() <= 0.01 and len(chromosome.b8) < self.b4:
            b34 = random.randint(1, self.b4 - len(chromosome.b8))
            b30 = set(range(len(self.b1["INPUT"]))) - set(chromosome.b8)
            b35 = random.sample(b30, b34)
            chromosome.b8.extend(b35)
    def fonk13(self, b3):
        for ind1, ind2 in combinations(b3, 2):
            if ind1.partially_less_than(ind2):
                ind2.b16 = False
            elif ind2.partially_less_than(ind1):
                ind1.b16 = False
    def fonk14(self):
        for b7 in self.b3:
            b7.b16 = True
        self.fonk13(self.b3)