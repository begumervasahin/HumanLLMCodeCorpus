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
            print(b7.b1, b6 = ' ')
            self.fonk3(b7.b3)
    def fonk4(self, b1, b7 = None):
        if b7 is None:
            b7 = self.b5
        while b7 is not None:
            if b1 = = b7.b1:
                return b7
            elif b1 < b7.b1:
                b7 = b7.b2
            else:
                b7 = b7.b3
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
    def fonk7(self, b1):
        b7 = self.fonk4(b1)
        if b7 is None:
            return None
        if b7.b3 is not None:
            return self.fonk5(b7.b3)
        b4 = b7.b4
        while b4 is not None and b7 = = b4.b3:
            b7 = b4
            b4 = b4.b4
        return b4
    def fonk8(self, b1):
        b7 = self.fonk4(b1)
        if b7 is None:
            return None
        if b7.b2 is not None:
            return self.fonk6(b7.b2)
        b4 = b7.b4
        while b4 is not None and b7 = = b4.b2:
            b7 = b4
            b4 = b4.b4
        return b4
    def fonk9(self, b1):
        if self.b5 is None:
            self.b5 = class1(b1)
            return
        b8 = self.b5
        while b8 is not None:
            if b1 <= b8.b1:
                if b8.b2 is None:
                    b8.b2 = class1(b1)
                    b8.b2.b4 = b8
                    return
                else:
                    b8 = b8.b2
            else:
                if b8.b3 is None:
                    b8.b3 = class1(b1)
                    b8.b3.b4 = b8
                    return
                else:
                    b8 = b8.b3
    def fonk10(self, b1):
        b7 = self.fonk4(b1)
        if b7 is None:
            return
        if b7.b2 is None and b7.b3 is None:
            if b7.b4 is None:
                self.b5 = None
            elif b7.b4.b2 = = b7:
                b7.b4.b2 = None
            else:
                b7.b4.b3 = None
        elif b7.b2 is not None and b7.b3 is None:
            if b7.b4 is None:
                self.b5 = b7.b2
            elif b7.b4.b2 = = b7:
                b7.b4.b2 = b7.b2
            else:
                b7.b4.b3 = b7.b2
        elif b7.b2 is None and b7.b3 is not None:
            if b7.b4 is None:
                self.b5 = b7.b3
            elif b7.b4.b2 = = b7:
                b7.b4.b2 = b7.b3
            else:
                b7.b4.b3 = b7.b3
        else:
            b9 = self.fonk7(b1)
            b7.b1 = b9.b1
            if b9.b4.b2 = = b9:
                b9.b4.b2 = None
            else:
                b9.b4.b3 = None
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
def fonk14(b11):
    b10 = class2()
    for b1 in b11:
        b10.fonk9(b1)
    print("\n---TREE INFO---\n")
    print("INORDER WALK: ", b6 = '')
    b10.fonk3(b10.b5)
    print("\nSEARCH for", str(b11[0]), "-->", b6 = ' ')
    print("Key EXISTS!" if b10.fonk4(b11[0]) is not None else "Key does NOT exist!")
    print("SEARCH for", str(b11[5]), "-->", b6 = ' ')
    print("Key EXISTS!" if b10.fonk4(b11[5]) is not None else "Key does NOT exist!")
    print("SEARCH for", str(b11[0] * 2), "-->", b6 = ' ')
    print("Key EXISTS!" if b10.fonk4(b11[0] * 2) is not None else "Key does NOT exist!")
    print("Minimum b1 in the Tree:", b10.fonk5().b1)
    print("Maximum b1 in the Tree:", b10.fonk6().b1)
    print("Successor of", str(b11[4]), "is", b10.fonk7(b11[4]).b1)
    print("Predecessor of", str(b11[4]), "is", b10.fonk8(b11[4]).b1)
    print("Delete b5", str(b11[0]) + ":", b6 = ' ')
    b10.fonk10(b11[0])
    b10.fonk3(b10.b5)
    print("\nHeight of the Tree:", b10.fonk11(b10.b5))
    print("Depth of the Tree:", b10.fonk12(b10.b5))
    print("Ratio Depth/Height:", b10.fonk13(), "\n")
def fonk15(length, rng):
    from random import randint
    b11 = [randint(0, length) for _ in range(rng)]
    return b11
def fonk16():
    fonk14(fonk15(30, 100))
    fonk14(fonk15(50, 1000))
    fonk14(fonk15(100, 500))
if b12 = = '__main__':
    fonk16()