from random import shuffle
import csv
class class1:
    def fonk1(self, b1 = None, b2=None, b3=None):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
    def fonk2(self, x):
        self.fonk3(x)
    def fonk3(self, current, x):
        if current is None:
            return class1(x, None, None)
        elif current.b1 > x:
            current.b2 = self.fonk3(current.b2, x)
        else:
            current.b3 = self.fonk3(current.b3, x)
        return current
    def fonk4(self, b4 = None):
        if b4 is None:
            return 0
        return max(self.fonk4(b4.b2), self.fonk4(b4.b3)) + 1
def fonk5(b8):
    b5 = [i for i in range(b8)]
    shuffle(b5)
    return b5
def fonk6(b7):
    b4 = class1(b7[0], None, None)
    for i in range(1, len(b7)):
        b4.fonk2(b7[i])
    return b4
def fonk7():
    print("b8 is the number of vertices in the Binary Search class1\nh is the corresponding average height of 500 randomly generated samples\b8")
    b6 = [["number of nodes", "height"]]
    a1 = 500
    print("Generating b6.....")
    for b8 in range(100, 1001, 100):
        a2 = 0
        for t in range(a1):
            b7 = fonk5(b8)
            b4 = fonk6(b7)
            a2 += b4.fonk4(b4)
        b6.append([b8, a2 / a1])
        print("b8 = %4d, h = %2.3f" % (b6[-1][0], b6[-1][1]))
    with open("b6.csv", "w+", b9 = '') as csv_file:
        b10 = csv.b10(csv_file)
        b10.writerows(b6)
if b11 = = "__main__":
    fonk7()