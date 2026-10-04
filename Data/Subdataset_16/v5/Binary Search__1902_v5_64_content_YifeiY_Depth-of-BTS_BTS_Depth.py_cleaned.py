import csv
from random import shuffle
class class1:
    def fonk1(self, b1 = None):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
    def fonk2(self, x):
        if self.b1 is None:
            self.b1 = x
        else:
            self.fonk3(self, x)
    @staticmethod
    def fonk3(current, x):
        if current is None:
            return class1(x)
        elif x < current.b1:
            current.b2 = class1.fonk3(current.b2, x)
        else:
            current.b3 = class1.fonk3(current.b3, x)
        return current
    def fonk4(self):
        if self.b1 is None:
            return 0
        return self.fonk5(self)
    @staticmethod
    def fonk5(node):
        if node is None:
            return 0
        return max(class1.fonk5(node.b2), class1.fonk5(node.b3)) + 1
def fonk6(b13):
    b4 = list(range(b13))
    shuffle(b4)
    return b4
def fonk7(b7):
    b5 = class1()
    for b1 in b7:
        b5.fonk2(b1)
    return b5
def fonk8(b13, b6 = 500):
    a1 = 0
    for _ in range(b6):
        b7 = fonk6(b13)
        b5 = fonk7(b7)
        a1 += b5.fonk4()
    return a1 / b6
def fonk9(b11, b8 = "b11.csv"):
    with open(b8, "w+", b9 = '') as csv_file:
        b10 = csv.b10(csv_file)
        b10.writerows(b11)
def fonk10():
    print("b13 is the number of nodes in the Binary Search class1")
    print("h is the corresponding average height of 500 randomly generated samples\b13")
    b11 = [["Number of Nodes", "Average Height"]]
    print("Generating b11...")
    for b13 in range(100, 1001, 100):
        b12 = fonk8(b13)
        b11.append([b13, b12])
        print(f"b13 = {b13:4d}, h = {b12:.3f}")
    fonk9(b11)
if b14 = = "__main__":
    fonk10()