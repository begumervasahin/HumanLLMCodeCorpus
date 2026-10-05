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
    def fonk4(self):
        self.b4 = self.fonk5(0)
    def fonk5(self, index):
        if index >= len(self.b5):
            return None
        b6 = class1(self.b5[index])
        b6.b2 = self.fonk5(2 * index + 1)
        b6.b3 = self.fonk5(2 * index + 2)
        return b6
    def fonk6(self, b6):
        if b6 is None:
            return
        self.fonk6(b6.b2)
        print(b6.b1)
        self.fonk6(b6.b3)
    def fonk7(self, b6):
        if b6 is None:
            return
        b7 = [b6]
        while b7:
            b8 = b7.pop(0)
            print(b8.b1)
            if b8.b2:
                b7.append(b8.b2)
            if b8.b3:
                b7.append(b8.b3)
    def fonk8(self, b6):
        if b6 is None:
            return -1
        b9 = self.fonk8(b6.b2)
        b10 = self.fonk8(b6.b3)
        return max(b9, b10) + 1
b11 = class2()
b11.fonk3(2)
b11.fonk3(3)
b11.fonk3(5)
b11.fonk3(7)
b11.fonk3(1)
b11.fonk3(10)
b11.fonk3(9)
b11.fonk3(8)
b11.fonk4()
print("Inorder Traversal:")
b11.fonk6(b11.b4)
print("\nLevel Order Traversal:")
b11.fonk7(b11.b4)
print("\nHeight of the tree:", b11.fonk8(b11.b4))