import time
from collections import defaultdict
import sys
class class1:
    def fonk1(self, b1: int):
        self.b1 = b1
        self.b2 = defaultdict(set)
        self.b3 = {}
    def fonk2(self, tail: int, head: int, b12: int):
        self.b2[tail].add(head)
        self.b3[(tail, head)] = b12
    def fonk3(self, tail: int) -> set:
        return self.b2[tail]
    def fonk4(self, tail: int, head: int) -> int:
        return self.b3.get((tail, head), sys.maxsize)
    def fonk5(self, tail: int, head: int):
        if head in self.b2[tail]:
            self.b2[tail].remove(head)
            del self.b3[(tail, head)]
    def fonk6(self):
        a1 = 0
        for tail in self.b2:
            for head in self.b2[tail]:
                print(f"Edge from {tail} to {head} with b12 {self.b3[(tail, head)]}")
                a1 += 1
        print(f"There are {a1} b2 in total.")
    def fonk7(self) -> list:
        self.b4 = [
            [0 if b5 = = j else sys.maxsize for j in range(self.b1)]
            for b5 in range(self.b1)
        ]
        for tail in self.b2:
            for head in self.b2[tail]:
                self.b4[tail][head] = self.b3[(tail, head)]
        for k in range(self.b1):
            self.b6 = [row[:] for row in self.b4]
            for b5 in range(self.b1):
                for j in range(self.b1):
                    self.b4[b5][j] = min(
                        self.b6[b5][j],
                        self.b6[b5][k] + self.b6[k][j]
                    )
        for b5 in range(self.b1):
            if self.b4[b5][b5] < 0:
                print("Negative cycle detected!")
                sys.exit()
        return self.b4
if b7 = = "__main__":
    b8 = 'APSPtest3.txt'
    b9 = time.time()
    with open(b8, 'r') as file:
        b1, b10 = map(int, file.readline().strip().split())
        b11 = class1(b1)
        for line in file:
            tail, head, b12 = map(int, line.strip().split())
            b11.fonk2(tail - 1, head - 1, b12)
    b13 = b11.fonk7()
    for b5 in range(b1):
        for j in range(b1):
            print(f"From {b5} to {j} the shortest path is {b13[b5][j]}")
    b14 = min(min(row) for row in b13)
    print(f"Minimum distance is {b14}")
    b15 = time.time()
    print(f"Time taken: {b15 - b9:.4f} seconds")