import sys
class class1:
    def fonk1(self, b2):
        self.b1 = self.b4 = None
        self.b2 = b2
class class2:
    def fonk2(self):
        self.b3 = None
    def fonk3(self, b2):
        self.b3 = self.fonk4(self.b3, b2)
    def fonk4(self, b3, b2):
        if b3 is None:
            return class1(b2)
        else:
            if b2 <= b3.b2:
                b3.b4 = self.fonk4(b3.b4, b2)
            else:
                b3.b1 = self.fonk4(b3.b1, b2)
        return b3
    def fonk5(self):
        return self.fonk6(self.b3)
    def fonk6(self, b3):
        if b3 is None:
            return -1
        b5 = self.fonk6(b3.b4)
        b6 = self.fonk6(b3.b1)
        return max(b5, b6) + 1
    def fonk7(self):
        self.fonk8(self.b3)
        print()
    def fonk8(self, b3):
        if b3 is not None:
            self.fonk8(b3.b4)
            print(b3.b2, b7 = " ")
            self.fonk8(b3.b1)
    def fonk9(self):
        self.fonk10(self.b3)
        print()
    def fonk10(self, b3):
        if b3 is not None:
            self.fonk10(b3.b4)
            self.fonk10(b3.b1)
            print(b3.b2, b7 = " ")
    def fonk11(self):
        self.fonk12(self.b3)
        print()
    def fonk12(self, b3):
        if b3 is not None:
            print(b3.b2, b7 = " ")
            self.fonk12(b3.b4)
            self.fonk12(b3.b1)
    def fonk13(self):
        if self.b3 is None:
            return
        b8 = [self.b3]
        while b8:
            b9 = b8.pop(0)
            print(b9.b2, b7 = " ")
            if b9.b4:
                b8.append(b9.b4)
            if b9.b1:
                b8.append(b9.b1)
b10 = class2()
b11 = [5, 3, 7, 2, 4, 6, 8]
for value in b11:
    b10.fonk3(value)
print("Inorder traversal:", b7 = " ")
b10.fonk7()
print("Postorder traversal:", b7 = " ")
b10.fonk9()
print("Preorder traversal:", b7 = " ")
b10.fonk11()
print("Level order traversal:", b7 = " ")
b10.fonk13()
print("Height of the b10:", b10.fonk5())