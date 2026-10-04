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
            self.b4 = class1(b1)
            b6 = self.b4
        else:
            b6 = address
        b7 = 2 * index + 1
        b8 = 2 * index + 2
        if b7 < len(self.b5):
            b9 = self.b5[b7]
            b10 = class1(b9)
            b6.b2 = b10
            self.fonk4(b9, b10, b7)
        if b8 < len(self.b5):
            b11 = self.b5[b8]
            b12 = class1(b11)
            b6.b3 = b12
            self.fonk4(b11, b12, b8)
    def fonk5(self, b6):
        if b6:
            self.fonk5(b6.b2)
            print(b6.b1, b13 = ' ')
            self.fonk5(b6.b3)
    def fonk6(self, b6):
        if b6 is None:
            return
        b14 = [b6]
        while b14:
            b15 = b14.pop(0)
            print(b15.b1, b13 = ' ')
            if b15.b2:
                b14.append(b15.b2)
            if b15.b3:
                b14.append(b15.b3)
    def fonk7(self, b6):
        if b6 is None:
            return -1
        b16 = self.fonk7(b6.b2)
        b17 = self.fonk7(b6.b3)
        return max(b16, b17) + 1
def fonk8():
    b18 = class2()
    b19 = [2, 3, 5, 7, 1, 10, 9, 8]
    for b15 in b19:
        b18.fonk3(b15)
    b18.fonk4(b18.b5[0], b18.b4, 0)
    print("In-order traversal:")
    b18.fonk5(b18.b4)
    print()
    print("Level-order traversal:")
    b18.fonk6(b18.b4)
    print()
    print("Height of the b18:")
    print(b18.fonk7(b18.b4))
if b20 = = "__main__":
    fonk8()