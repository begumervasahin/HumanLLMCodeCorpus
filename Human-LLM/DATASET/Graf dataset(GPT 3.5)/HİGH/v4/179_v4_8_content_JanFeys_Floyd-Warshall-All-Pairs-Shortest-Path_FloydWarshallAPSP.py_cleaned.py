import time
import sys
from collections import defaultdict
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = defaultdict(set)
        self.b3 = dict()
    def fonk2(self, source, destination, b4):
        self.b2[source].add(destination)
        self.b3[(source, destination)] = b4
    def fonk3(self, source, destination):
        self.b2[source].remove(destination)
        del self.b3[(source, destination)]
    def fonk4(self):
        a1 = 0
        for source in self.b2:
            for destination in self.b2[source]:
                b4 = self.b3[(source, destination)]
                print(f"Edge from {source} to {destination} with b4 {b4}")
                a1 += 1
        print(f"There are {a1} b2 in total.")
    def fonk5(self):
        b5 = [[0 if i == j else sys.maxsize for j in range(self.b1)] for i in range(self.b1)]
        for source in self.b2:
            for destination in self.b2[source]:
                b5[source][destination] = self.b3[(source, destination)]
        for k in range(self.b1):
            for i in range(self.b1):
                for j in range(self.b1):
                    b5[i][j] = min(b5[i][j], b5[i][k] + b5[k][j])
        for i in range(self.b1):
            if b5[i][i] < 0:
                print("Negative cycle detected!")
                return None
        return b5
if b6 = = "__main__":
    b7 = 'APSPtest3.txt'
    b8 = time.time()
    with open(b7, 'r') as file:
        b1, b9 = map(int, file.readline().strip().split())
        b10 = class1(b1)
        for line in file:
            source, destination, b4 = map(int, line.strip().split())
            b10.fonk2(source - 1, destination - 1, b4)
    b11 = b10.fonk5()
    if b11:
        for source in range(b1):
            for destination in range(b1):
                print(f"From {source} to {destination}, shortest path is {b11[source][destination]}")
        print("Minimum shortest path:", min(min(b11)))
    b12 = time.time()
    print("Execution time:", b12 - b8)