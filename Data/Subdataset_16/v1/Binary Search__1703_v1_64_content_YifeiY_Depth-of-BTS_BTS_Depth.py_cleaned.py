import random
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
        elif x < self.b1:
            if self.b2 is None:
                self.b2 = class1(x)
            else:
                self.b2.fonk3(x)
        else:
            if self.b3 is None:
                self.b3 = class1(x)
            else:
                self.b3.fonk3(x)
    def fonk4(self):
        if self.b1 is None:
            return 0
        b4 = self.b2.fonk4() if self.b2 else 0
        b5 = self.b3.fonk4() if self.b3 else 0
        return max(b4, b5) + 1
def fonk5(b11):
    b6 = list(range(b11))
    random.shuffle(b6)
    return b6
def fonk6(b9):
    b7 = class1(b9[0])
    for b1 in b9[1:]:
        b7.fonk2(b1)
    return b7
def fonk7():
    print("b11 is the number of vertices in the Binary Search class1")
    print("h is the corresponding average height of 500 randomly generated samples\b11")
    b8 = [["number of nodes", "average height"]]
    a1 = 500
    print("Generating b8.....")
    for b11 in range(100, 1001, 100):
        a2 = 0
        for _ in range(a1):
            b9 = fonk5(b11)
            b7 = fonk6(b9)
            a2 += b7.fonk4()
        b10 = a2 / a1
        b8.append([b11, b10])
        print(f"b11 = {b11:4d}, h = {b10:.3f}")
    with open("b8.csv", "w", b12 = '') as csv_file:
        b13 = csv.b13(csv_file)
        b13.writerows(b8)
if b14 = = "__main__":
    fonk7()