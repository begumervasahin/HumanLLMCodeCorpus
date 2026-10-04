class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
class class2:
    def fonk2(self):
        self.b4 = None
        self.b5 = []
    def fonk3(self, b1):
        self.b5.append(b1)
    def fonk4(self, b1, address, index):
        if self.b4 is None:
            b6 = class1(b1)
            self.b4 = b6
            b7 = b6
        else:
            b7 = address
        b8 = 2 * index + 1
        b9 = 2 * index + 2
        if b8 < len(self.b5):
            b10 = class1(self.b5[b8])
            b7.b2 = b10
            self.fonk4(self.b5[b8], b10, b8)
        if b9 < len(self.b5):
            b11 = class1(self.b5[b9])
            b7.b3 = b11
            self.fonk4(self.b5[b9], b11, b9)
    def fonk5(self, b7):
        if b7 is None:
            return
        self.fonk5(b7.b2)
        print(b7.b1, b12 = ' ')
        self.fonk5(b7.b3)
    def fonk6(self, b7):
        if b7 is None:
            return
        b13 = [b7]
        while b13:
            b14 = b13.pop(0)
            print(b14.b1, b12 = ' ')
            if b14.b2:
                b13.append(b14.b2)
            if b14.b3:
                b13.append(b14.b3)
    def fonk7(self, b7):
        if b7 is None:
            return -1
        b15 = self.fonk7(b7.b2)
        b16 = self.fonk7(b7.b3)
        return max(b15, b16) + 1
def fonk8():
    b17 = class2()
    b17.fonk3(2)
    b17.fonk3(3)
    b17.fonk3(5)
    b17.fonk3(7)
    b17.fonk3(1)
    b17.fonk3(10)
    b17.fonk3(9)
    b17.fonk3(8)
    b17.fonk4(b17.b5[0], b17.b4, 0)
    print("In-order traversal:")
    b17.fonk5(b17.b4)
    print()
    print("Level-order traversal:")
    b17.fonk6(b17.b4)
    print()
    print("Height of the tree:")
    print(b17.fonk7(b17.b4))
    print()
if b18 = = "__main__":
    fonk8()