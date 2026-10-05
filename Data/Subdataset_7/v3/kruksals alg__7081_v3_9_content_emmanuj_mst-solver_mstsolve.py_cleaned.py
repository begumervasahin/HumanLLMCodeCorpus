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
    def fonk8(self, b7):
        for b9 in b7:
            heappush(self.b5, (b9.b3, b9))
    def fonk9(self):
        return len(self.b5)
    def fonk10(self):
        return self.b5[0][1]
    def fonk11(self):
        heappop(self.b5)
def fonk12(file_path):
    b7 = []
    b8 = []
    with open(file_path) as f:
        for line in f:
            if line.startswith("e"):
                _, b1, b2, b3 = map(int, line.split()[1:])
                b9 = class1(b1, b2, b3)
                b7.append(b9)
                b8.extend([b1, b2])
    return b7, list(set(b8))
def fonk13():
    b7 = []
    b8 = []
    print("Enter b9 line by line in the format e b1 b2 w. Press enter each time. Press enter twice when done.")
    for line in sys.stdin:
        if not line.strip():
            break
        if line.startswith("e"):
            _, b1, b2, b3 = map(int, line.split()[1:])
            b9 = class1(b1, b2, b3)
            b7.append(b9)
            b8.extend([b1, b2])
    return b7, list(set(b8))
def fonk14(b16, a1, output_file):
    with open(output_file, "w") as f:
        f.write(f"c Total cost of tree {a1}\n")
        for b9 in b16:
            f.write(str(b9) + "\n")
def fonk15(b16, a1):
    print(f"c Total cost of tree {a1}")
    for b9 in b16:
        print(b9)
def fonk16():
    b10 = argparse.ArgumentParser(description='Minimum Spanning Tree (MST) Solver')
    b10.add_argument("-b6", "--heap_d", b11 = 2, type=int, b12="balanced head width")
    b10.add_argument("-o", "--output", b12 = "Output file to write solution")
    b10.add_argument("-i", "--infile", b12 = "Input graph file. Graph must be in DIMACS format")
    b13 = b10.parse_args()
    b6 = b13.heap_d
    b14 = class3(b6)
    if b13.infile:
        b7, b8 = fonk12(b13.infile)
    else:
        b7, b8 = fonk13()
    if not b8 or not b7:
        print("Error: Invalid graph")
        sys.exit(1)
    b14.fonk8(b7)
    b15 = class2()
    for i in b8:
        b15.fonk4(i)
    b16 = []
    a1 = 0
    while b14.fonk9() != 0:
        _, b9 = b14.fonk10()
        if b15.fonk5(b9.b1) != b15.fonk5(b9.b2):
            b15.fonk6(b9.b1, b9.b2)
            b16.append(b9)
            a1 += b9.b3
        b14.fonk11()
    if b13.output:
        fonk14(b16, a1, b13.output)
    else:
        fonk15(b16, a1)
if b17 = = "__main__":
    fonk16()