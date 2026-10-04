class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
    def fonk2(self):
        return str(self.b1)
class class2:
    def fonk3(self, b3 = None):
        self.b3 = b3
    def fonk4(self, b1):
        b4 = class1(b1)
        if self.b3 is None:
            self.b3 = b4
            return
        b5 = self.b3
        while b5.b2 is not None:
            b5 = b5.b2
        b5.b2 = b4
    def fonk5(self):
        b6 = []
        b5 = self.b3
        while b5 is not None:
            b6.fonk4(str(b5.b1))
            b5 = b5.b2
        return " -> ".join(b6)
def fonk6(b9, b10):
    b7 = class1(0)
    b8 = b7
    while b9 is not None and b10 is not None:
        if b9.b1 <= b10.b1:
            b8.b2 = b9
            b9 = b9.b2
        else:
            b8.b2 = b10
            b10 = b10.b2
        b8 = b8.b2
    b8.b2 = b9 if b9 is not None else b10
    return class2(b7.b2)
class class3(class2):
    def fonk7(self):
        return self.fonk8(self.b3)
    def fonk8(self, b5):
        if b5.b2 is None:
            return b5.b1
        return fonk6(b5.b1, self.fonk8(b5.b2))
b11 = class2(class1(1))
b11.fonk4(3)
b11.fonk4(5)
b12 = class2(class1(2))
b12.fonk4(4)
b13 = fonk6(b11.b3, b12.b3)
print("Merged Linked List:", b13)
b14 = class3(class1(b11))
b14.fonk4(b12)
b15 = b14.fonk7()
print("Flattened Nested Linked List:", b15)