import time
from collections import defaultdict
import sys
class class1:
    def fonk1(self, b1: int):
        self.b1 = b1
        self.b2 = defaultdict(set)
        self.b3 = dict()
    def fonk2(self) -> int:
        return self.b1
    def fonk3(self, t: int, h: int, b11: int):
        self.b2[t].add(h)
        self.b3[(t, h)] = b11
    def fonk4(self, t: int) -> set:
        return self.b2[t]
    def fonk5(self, t: int, h: int) -> int:
        return self.b3[(t, h)]
    def fonk6(self, t: int, h: int):
        self.b2[t].remove(h)
        del self.b3[(t, h)]
    def fonk7(self):
        a1 = 0
        for t in self.b2:
            for h in self.b2[t]:
                print(f"Edge from {t} to {h} with weight {self.b3[(t, h)]}")
                a1 += 1
        print(f"There are {a1} edges in total.")
    def fonk8(self) -> list:
        self.b4 = [[0 if t == h else sys.maxsize for h in range(self.b1)] for t in range(self.b1)]
        for t in range(self.b1):
            for h in self.b2[t]:
                self.b4[t][h] = self.b3[(t, h)]
        for k in range(self.b1):
            self.b5 = [row[:] for row in self.b4]
            for t in range(self.b1):
                for h in range(self.b1):
                    self.b4[t][h] = min(self.b5[t][h], self.b5[t][k] + self.b5[k][h])
        for t in range(self.b1):
            if self.b4[t][t] < 0:
                print("There is a negative cycle!")
                sys.exit()
        return self.b4
if b6 = = "__main__":
    b7 = 'APSPtest3.txt'
    b8 = time.time()
    with open(b7, 'r') as file:
        b1, b9 = map(int, file.readline().strip().split())
        b10 = class1(b1)
        for line in file:
            t, h, b11 = map(int, line.strip().split())
            b10.fonk3(t - 1, h - 1, b11)
    b12 = b10.fonk8()
    for t in range(b1):
        for h in range(b1):
            print(f"From {t} to {h} the shortest path is {b12[t][h]}")
    b13 = min(min(row) for row in b12)
    print(f"Minimum distance is {b13}")
    b14 = time.time()
    print(f"Time taken: {b14 - b8:.4f} seconds")