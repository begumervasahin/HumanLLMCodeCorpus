from random import shuffle
import csv
class class1:
    def fonk1(self, b1 = None, b2=None, b3=None):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
class class2:
    def fonk2(self):
        self.b4 = None
    def fonk3(self, x):
        self.b4 = self.fonk4(self.b4, x)
    def fonk4(self, current, x):
        if current is None:
            return class1(x)
        elif current.b1 > x:
            current.b2 = self.fonk4(current.b2, x)
        else:
            current.b3 = self.fonk4(current.b3, x)
        return current
    def fonk5(self, b5 = None):
        if b5 is None:
            b5 = self.b4
        if b5 is None:
            return 0
        return max(self.fonk5(b5.b2), self.fonk5(b5.b3)) + 1
def fonk6(b11):
    b6 = [i for i in range(b11)]
    shuffle(b6)
    return b6
def fonk7(b8):
    b5 = class2()
    for num in b8:
        b5.fonk3(num)
    return b5
def fonk8():
    print("b11 is the number of vertices in the Binary Search Tree.")
    print("h is the corresponding average height of 500 randomly generated samples.\b11")
    b7 = [["number of nodes", "height"]]
    a1 = 500
    print("Generating b7...")
    for b11 in range(100, 1001, 100):
        a2 = 0
        for _ in range(a1):
            b8 = fonk6(b11)
            b9 = fonk7(b8)
            a2 += b9.fonk5()
        b10 = a2 / a1
        b7.append([b11, b10])
        print(f"b11 = {b7[-1][0]}, h = {b7[-1][1]:.3f}")
    with open("b7.csv", "w", b12 = "") as csv_file:
        b13 = csv.b13(csv_file)
        b13.writerows(b7)
if b14 = = "__main__":
    fonk8()