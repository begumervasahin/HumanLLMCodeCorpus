import sys
import argparse
from heapq import heappop, heappush
class class1:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
    def fonk2(self):
        return f"e {self.b1} {self.b2} {self.b3}"
class class2:
    def fonk3(self):
        self.b4 = {}
    def fonk4(self, x):
        self.b4[x] = x
    def fonk5(self, x):
        if self.b4[x] != x:
            self.b4[x] = self.fonk5(self.b4[x])
        return self.b4[x]
    def fonk6(self, x, y):
        self.b4[self.fonk5(x)] = self.fonk5(y)
class class3:
    def fonk7(self, b6):
        self.b5 = []
        self.b6 = b6
    def fonk8(self, b11):
        for b15 in b11:
            heappush(self.b5, (b15.b3, b15))
    def fonk9(self):
        return len(self.b5)
    def fonk10(self):
        return self.b5[0][1]
    def fonk11(self):
        heappop(self.b5)
def fonk12():
    b7 = argparse.ArgumentParser(description='Minimum Spanning Tree (MST) Solver')
    b7.add_argument("-b6", "--heap_d", b8 = 2, type=int, b9="balanced head width")
    b7.add_argument("-o", "--output", b9 = "Output file to write solution")
    b7.add_argument("-i", "--infile", b9 = "Input graph file. Graph must be in DIMACS format")
    b10 = b7.parse_args()
    b11 = []
    b12 = []
    b13 = []
    b6 = b10.heap_d
    b14 = class3(b6)
    if b10.infile:
        with open(b10.infile) as f:
            for line in f:
                if line.startswith("e"):
                    _, b1, b2, b3 = map(int, line.split()[1:])
                    b15 = class1(b1, b2, b3)
                    b11.append(b15)
                    b12.extend([b1, b2])
    else:
        print("Enter b15 line by line in the format e b1 b2 w. Press enter each time. Press enter twice when done.")
        for line in sys.stdin:
            if not line.strip():
                break
            if line.startswith("e"):
                _, b1, b2, b3 = map(int, line.split()[1:])
                b15 = class1(b1, b2, b3)
                b11.append(b15)
                b12.extend([b1, b2])
    b12 = list(set(b12))
    if len(b12) <= 0:
        print("Error: Invalid number of nodes")
        sys.exit(0)
    if len(b11) <= 0:
        print("Error: Invalid number of b11")
        sys.exit(0)
    b14.fonk8(b11)
    b16 = class2()
    for i in b12:
        b16.fonk4(i)
    a1 = 0
    while b14.fonk9() != 0:
        _, b17 = b14.fonk10()
        if b16.fonk5(b17.b1) != b16.fonk5(b17.b2):
            b16.fonk6(b17.b1, b17.b2)
            b13.append(b17)
            a1 += b17.b3
        b14.fonk11()
    if b10.output:
        with open(b10.output, "w") as f:
            f.write(f"c Total cost of tree {a1}\n")
            for b15 in b13:
                f.write(str(b15) + "\n")
    else:
        print(f"c Total cost of tree {a1}")
        for b15 in b13:
            print(b15)
if b18 = = "__main__":
    fonk12()