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
            b9 = class1(self.b5[b7])
            b6.b2 = b9
            self.fonk4(self.b5[b7], b9, b7)
        if b8 < len(self.b5):
            b10 = class1(self.b5[b8])
            b6.b3 = b10
            self.fonk4(self.b5[b8], b10, b8)
    def fonk5(self, b6):
        if b6:
            self.fonk5(b6.b2)
            print(b6.b1, b11 = ' ')
            self.fonk5(b6.b3)
    def fonk6(self, b6):
        if not b6:
            return
        b12 = [b6]
        while b12:
            b13 = b12.pop(0)
            print(b13.b1, b11 = ' ')
            if b13.b2:
                b12.append(b13.b2)
            if b13.b3:
                b12.append(b13.b3)
    def fonk7(self, b6):
        if not b6:
            return -1
        b14 = self.fonk7(b6.b2)
        b15 = self.fonk7(b6.b3)
        return max(b14, b15) + 1
b16 = class2()
b17 = [2, 3, 5, 7, 1, 10, 9, 8]
for b13 in b17:
    b16.fonk3(b13)
b16.fonk4(b16.b5[0], b16.b4, 0)
print("In-order Traversal:")
b16.fonk5(b16.b4)
print()
print("Level-order Traversal:")
b16.fonk6(b16.b4)
print()
print("Height of the class2:")
print(b16.fonk7(b16.b4))
print()