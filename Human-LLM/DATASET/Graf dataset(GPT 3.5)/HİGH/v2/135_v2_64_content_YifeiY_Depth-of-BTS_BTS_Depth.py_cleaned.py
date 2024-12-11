from random import shuffle
import csv
class class1:
    def fonk1(self, b1 = None, b2=None, b3=None):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
    def fonk2(self, x):
        self.fonk3(x)
    def fonk3(self, x):
        if self.b1 is None:
            self.b1 = x
            self.b2 = None
            self.b3 = None
        elif self.b1 > x:
            if self.b2 is None:
                self.b2 = class1(x, None, None)
            else:
                self.b2.fonk3(x)
        else:
            if self.b3 is None:
                self.b3 = class1(x, None, None)
            else:
                self.b3.fonk3(x)
    def fonk4(self):
        return self.fonk5(self)
    def fonk5(self, node):
        if node is None:
            return 0
        return max(self.fonk5(node.b2), self.fonk5(node.b3)) + 1
def fonk6(b9):
    b4 = [i for i in range(b9)]
    shuffle(b4)
    return b4
def fonk7(b7):
    b5 = class1()
    for element in b7:
        b5.fonk2(element)
    return b5
def fonk8():
    print("b9 is the number of vertices in the Binary Search Tree\nh is the corresponding average height of 500 randomly generated samples\b9")
    b6 = [["number of nodes", "height"]]
    a1 = 500
    print("Generating b6.....")
    for b9 in range(100, 1001, 100):
        a2 = 0
        for _ in range(a1):
            b7 = fonk6(b9)
            b5 = fonk7(b7)
            a2 += b5.fonk4()
        b8 = a2 / a1
        b6.append([b9, b8])
        print(f"b9 = {b6[-1][0]}, h = {b6[-1][1]:.3f}")
    with open("b6.csv", "w+", b10 = '') as csv_file:
        b11 = csv.b11(csv_file)
        b11.writerows(b6)
if b12 = = "__main__":
    fonk8()