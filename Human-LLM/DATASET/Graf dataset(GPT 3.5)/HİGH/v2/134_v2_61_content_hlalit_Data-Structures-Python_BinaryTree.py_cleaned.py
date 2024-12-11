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
            b7 = b6
            self.b4 = b7
        else:
            b7 = address
        b8 = 2 * index + 1
        b9 = 2 * index + 2
        if b8 < len(self.b5):
            b10 = self.b5[b8]
            b11 = class1(b10)
            b7.b2 = b11
            self.fonk4(b10, b11, b8)
        if b9 < len(self.b5):
            b12 = self.b5[b9]
            b13 = class1(b12)
            b7.b3 = b13
            self.fonk4(b12, b13, b9)
    def fonk5(self, b7):
        if b7 is None:
            return
        else:
            self.fonk5(b7.b2)
            print(b7.b1)
            self.fonk5(b7.b3)
    def fonk6(self, b7):
        if b7 is None:
            return
        b14 = []
        b14.append(b7)
        while len(b14) > 0:
            print(b14[0].b1)
            b15 = b14.pop(0)
            if b15.b2:
                b14.append(b15.b2)
            if b15.b3:
                b14.append(b15.b3)
    def fonk7(self, b7):
        if b7 is None:
            return -1
        else:
            b16 = self.fonk7(b7.b2)
            b17 = self.fonk7(b7.b3)
            return max(b16, b17) + 1
b18 = class2()
b18.fonk3(2)
b18.fonk3(3)
b18.fonk3(5)
b18.fonk3(7)
b18.fonk3(1)
b18.fonk3(10)
b18.fonk3(9)
b18.fonk3(8)
b18.fonk4(b18.b5[0], b18.b4, 0)
print("Inorder Traversal:")
b18.fonk5(b18.b4)
print("\nLevel Order Traversal:")
b18.fonk6(b18.b4)
print("\nHeight of the b18:", b18.fonk7(b18.b4))