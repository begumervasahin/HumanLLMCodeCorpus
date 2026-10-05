import time
import sys
from collections import defaultdict
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = defaultdict(set)
        self.b3 = dict()
    def fonk2(self, source, destination, b10):
        self.b2[source].add(destination)
        self.b3[(source, destination)] = b10
    def fonk3(self, source, destination):
        self.b2[source].remove(destination)
        del self.b3[(source, destination)]
    def fonk4(self):
        b4 = [[0 if i == j else sys.maxsize for j in range(self.b1)] for i in range(self.b1)]
        for source in self.b2:
            for destination in self.b2[source]:
                b4[source][destination] = self.b3[(source, destination)]
        for k in range(self.b1):
            for i in range(self.b1):
                for j in range(self.b1):
                    b4[i][j] = min(b4[i][j], b4[i][k] + b4[k][j])
        for i in range(self.b1):
            if b4[i][i] < 0:
                print("Negative cycle detected!")
                return None
        return b4
    def fonk5(self):
        a1 = 0
        for source in self.b2:
            for destination in self.b2[source]:
                print(f"Edge from {source} to {destination} with b10 {self.b3[(source, destination)]}")
                a1 += 1
        print(f"There are {a1} b2 in total.")
if b5 = = "__main__":
    b6 = 'APSPtest3.txt'
    b7 = time.time()
    with open(b6, 'r') as f:
        b1, b8 = map(int, f.readline().strip().split())
        b9 = class1(b1)
        for line in f:
            source, destination, b10 = map(int, line.strip().split())
            b9.fonk2(source - 1, destination - 1, b10)
    b11 = b9.fonk4()
    if b11:
        for source in range(b1):
            for destination in range(b1):
                print(f"From {source} to {destination}, shortest path is {b11[source][destination]}")
        print("Minimum shortest path:", min(min(b11)))
    b12 = time.time()
    print("Execution time:", b12 - b7)