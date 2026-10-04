import csv
from random import shuffle
class class1:
    def fonk1(self, b1 = None, b2=None, b3=None):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
    def fonk2(self, x):
        self.fonk3(x)
    @staticmethod
    def fonk3(current, x):
        if current is None:
            return class1(x)
        elif x < current.b1:
            current.b2 = class1.fonk3(current.b2, x)
        else:
            current.b3 = class1.fonk3(current.b3, x)
        return current
    def fonk4(self, b4 = None):
        if b4 is None:
            return 0
        return max(self.fonk4(b4.b2), self.fonk4(b4.b3)) + 1
def fonk5(b9):
    b5 = list(range(b9))
    shuffle(b5)
    return b5
def fonk6(b7):
    b4 = class1(b7[0])
    for b1 in b7[1:]:
        b4.fonk2(b1)
    return b4
def fonk7():
    print("b9 is the number of nodes in the Binary Search class1")
    print("h is the corresponding average height of 500 randomly generated samples\b9")
    b6 = [["Number of Nodes", "Average Height"]]
    a1 = 500
    print("Generating b6...")
    for b9 in range(100, 1001, 100):
        a2 = 0
        for _ in range(a1):
            b7 = fonk5(b9)
            b4 = fonk6(b7)
            a2 += b4.fonk4(b4)
        b8 = a2 / a1
        b6.append([b9, b8])
        print(f"b9 = {b9:4d}, h = {b8:.3f}")
    with open("b6.csv", "w+", b10 = '') as csv_file:
        b11 = csv.b11(csv_file)
        b11.writerows(b6)
if b12 = = "__main__":
    fonk7()