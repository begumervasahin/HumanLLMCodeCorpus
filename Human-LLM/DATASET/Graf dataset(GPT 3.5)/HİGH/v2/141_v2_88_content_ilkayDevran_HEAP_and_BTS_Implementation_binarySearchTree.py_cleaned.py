from __future__ import division
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
        self.b4 = None
class class2:
    def fonk2(self):
        self.b5 = None
    def fonk3(self, b7):
        if b7 is not None:
            self.fonk3(b7.b2)
            print(b7.b1, b6 = " ")
            self.fonk3(b7.b3)
    def fonk4(self, b1, b7 = None):
        if b7 is None:
            b7 = self.b5
        if self.b5.b1 = = b1:
            return self.b5
        else:
            if b7.b1 = = b1:
                return b7
            elif b1 < b7.b1 and b7.b2 is not None:
                return self.fonk4(b1, b7 = b7.b2)
            elif b1 > b7.b1 and b7.b3 is not None:
                return self.fonk4(b1, b7 = b7.b3)
            else:
                return None
    def fonk5(self, b7 = None):
        if b7 is None:
            b7 = self.b5
        while b7.b2 is not None:
            b7 = b7.b2
        return b7
    def fonk6(self, b7 = None):
        if b7 is None:
            b7 = self.b5
        while b7.b3 is not None:
            b7 = b7.b3
        return b7
    def fonk7(self, b1, b7 = None):
        if b7 is None:
            b7 = self.fonk4(b1)
            b8 = b7
        if b7.b3 is not None:
            return self.fonk5(b7 = b7.b3)
        b9 = b7.b4
        while b9 is not None and b7 is b9.b3:
            b7 = b9
            b9 = b9.b4
        if b9 is None:
            print(str(b1) + ' is the largest b1, no successor exists')
            return b8
        else:
            return b9
    def fonk8(self, b1, b7 = None):
        if b7 is None:
            b7 = self.fonk4(b1)
            b8 = b7
        if b7.b2 is not None:
            return self.fonk6(b7 = b7.b2)
        b9 = b7.b4
        while b9 is not None and b7 is b9.b2:
            b7 = b9
            b9 = b9.b4
        if b9 is None:
            print(str(b1) + ' is the largest b1, no predecessor exists')
            return b8
        else:
            return b9
    def fonk9(self, b1, b7 = None):
        if b7 is None:
            b7 = self.b5
        if self.b5 is None:
            self.b5 = class1(b1)
        else:
            if b1 <= b7.b1:
                if b7.b2 is None:
                    b7.b2 = class1(b1)
                    b7.b2.b4 = b7
                    return
                else:
                    return self.fonk9(b1, b7 = b7.b2)
            else:
                if b7.b3 is None:
                    b7.b3 = class1(b1)
                    b7.b3.b4 = b7
                    return
                else:
                    return self.fonk9(b1, b7 = b7.b3)
    def fonk10(self, b1, b7 = None):
        if b7 is None:
            b7 = self.fonk4(b1)
        if self.b5.b1 = = b7.b1:
            b9 = self.b5
        else:
            b9 = b7.b4
        if b7.b2 is None and b7.b3 is None:
            if b1 <= b9.b1:
                b9.b2 = None
            else:
                b9.b3 = None
            return
        if b7.b2 is not None and b7.b3 is None:
            if b7.b2.b1 < b9.b1:
                b9.b2 = b7.b2
            else:
                b9.b3 = b7.b2
            return
        if b7.b3 is not None and b7.b2 is None:
            if b7.b1 <= b9.b1:
                b9.b2 = b7.b3
            else:
                b9.b3 = b7.b3
            return
        if b7.b2 is not None and b7.b3 is not None:
            b10 = self.fonk5(b7)
            b7.b1 = b10.b1
            b10.b4.b2 = None
            return
    def fonk11(self, b7):
        if b7 is None:
            return 0
        else:
            return 1 + max(self.fonk11(b7.b2), self.fonk11(b7.b3))
    def fonk12(self, b7):
        if b7 is None:
            return 0
        else:
            return 1 + min(self.fonk12(b7.b2), self.fonk12(b7.b3))
    def fonk13(self):
        return self.fonk12(self.b5) / self.fonk11(self.b5)
def fonk14(b12):
    b11 = class2()
    for i in range(len(b12)):
        b11.fonk9(b12[i])
    print("\n---TREE INFO---\n")
    print("INORDER WALK: ", b6 = "")
    b11.fonk3(b11.b5)
    print("\nSEARCH for", b12[0], "\b11-->", b6 = " ")
    if b11.fonk4(b12[0]) is not None:
        print("Key EXISTS!")
    else:
        print("Key does NOT exist!")
    print("SEARCH for", b12[5], "\b11-->", b6 = " ")
    if b11.fonk4(b12[5]) is not None:
        print("Key EXISTS!")
    else:
        print("Key does NOT exist!")
    print("SEARCH for", b12[0]*2, "\b11-->", b6 = " ")
    if b11.fonk4(b12[0]*2) is not None:
        print("Key EXISTS!")
    else:
        print("Key does NOT exist!")
    print("Minimum b1 in the class2:", b11.fonk5().b1)
    print("Maximum b1 in the class2:", b11.fonk6().b1)
    print("Successor of", b12[4], "is", b11.fonk7(b12[4]).b1)
    print("Predecessor of", b12[4], "is", b11.fonk8(b12[4]).b1)
    print("Delete b5", b12[0], ":", b6 = " ")
    b11.fonk10(b12[0])
    b11.fonk3(b11.b5)
    print("\nHeight of the class2:", b11.fonk11(b11.b5))
    print("Depth of the class2:", b11.fonk12(b11.b5))
    print("Ratio Depth/Height:", b11.fonk13())
    print("\n")
def fonk15(length, rng):
    from random import randint
    b12 = [randint(0, length) for _ in range(rng)]
    return b12
def fonk16():
    fonk14(fonk15(30, 100))
    fonk14(fonk15(50, 1000))
    fonk14(fonk15(100, 500))
if b13 = = '__main__':
    fonk16()