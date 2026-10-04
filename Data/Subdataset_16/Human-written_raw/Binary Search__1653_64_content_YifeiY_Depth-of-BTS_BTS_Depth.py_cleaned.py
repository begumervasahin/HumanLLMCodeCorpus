from random import shuffle
import csv
class class1():
    def fonk1(self,b1 = None,b2 = None,b3 = None):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
    def fonk2(self,x):
        self.fonk3(x)
    def fonk3(b4,x):
        if b4 = = None:
            return class1(x,None,None)
        elif b4.b1 > x:
            b4.b2 = class1.fonk3(b4.b2,x)
        else:
            b4.b3 = class1.fonk3(b4.b3,x)
        return b4
    def fonk4(self,b5 = None):
        if b5 = = None:
            return 0
        return max(self.fonk4(b5.b2),self.fonk4(b5.b3)) + 1
def fonk5(b9):
    b6 = [i for i in range (b9)]
    shuffle(b6)
    return b6
def fonk6(b8):
    b5 = class1(b8[0], None, None)
    for i in range (1,len(b8)):
        b5.fonk2(b8[i])
    return b5
def fonk7():
    print("b9 is the number of vertices in the Binary Search class1 \nh is the corresponding average height of 500 randomly generated sample\b9")
    b7 = [["number of nodes","height"]]
    a1 = 500
    print("Generating b7.....")
    for b9 in range (100, 1001, 100):
        a2 = 0
        for t in range (a1):
            b8 = fonk5(b9)
            b5 = fonk6(b8)
            a2 = a2 + b5.fonk4(b5)
        b7.append([b9,a2/500])
        print("b9 = %4d, h = %2.3f" % (b7[-1][0], b7[-1][1]))
    with open("b7.csv","w+") as csv_file:
        b10 = csv.b10(csv_file)
        b10.writerows(b7)
fonk7()