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
    def fonk3(self, tail: int, head: int, b11: int):
        self.b2[tail].add(head)
        self.b3[(tail, head)] = b11
    def fonk4(self, tail: int) -> set:
        return self.b2[tail]
    def fonk5(self, tail: int, head: int) -> int:
        return self.b3.get((tail, head), sys.maxsize)
    def fonk6(self, tail: int, head: int):
        if head in self.b2[tail]:
            self.b2[tail].remove(head)
            del self.b3[(tail, head)]
    def fonk7(self):
        a1 = 0
        for tail in self.b2:
            for head in self.b2[tail]:
                print(f"Edge from {tail} to {head} with b11 {self.b3[(tail, head)]}")
                a1 += 1
        print(f"There are {a1} b2 in total.")
    def fonk8(self) -> list:
        self.b4 = [[0 if i == j else sys.maxsize for j in range(self.b1)] for i in range(self.b1)]
        for tail in range(self.b1):
            for head in self.b2[tail]:
                self.b4[tail][head] = self.b3[(tail, head)]
        for k in range(self.b1):
            self.b5 = [row[:] for row in self.b4]
            for i in range(self.b1):
                for j in range(self.b1):
                    self.b4[i][j] = min(self.b5[i][j], self.b5[i][k] + self.b5[k][j])
        for i in range(self.b1):
            if self.b4[i][i] < 0:
                print("Negative cycle detected!")
                sys.exit()
        return self.b4
if b6 = = "__main__":
    b7 = 'APSPtest3.txt'
    b8 = time.time()
    with open(b7, 'r') as file:
        num_vertices, b9 = map(int, file.readline().strip().split())
        b10 = class1(num_vertices)
        for line in file:
            tail, head, b11 = map(int, line.strip().split())
            b10.fonk3(tail - 1, head - 1, b11)
    b12 = b10.fonk8()
    for i in range(num_vertices):
        for j in range(num_vertices):
            print(f"From {i} to {j} the shortest path is {b12[i][j]}")
    b13 = min(min(row) for row in b12)
    print(f"Minimum distance is {b13}")
    b14 = time.time()
    print(f"Time taken: {b14 - b8:.4f} seconds")