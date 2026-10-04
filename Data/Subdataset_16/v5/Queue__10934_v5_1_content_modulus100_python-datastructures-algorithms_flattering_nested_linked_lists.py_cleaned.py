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
        if not self.b3:
            self.b3 = b4
            return
        b5 = self.b3
        while b5.b2:
            b5 = b5.b2
        b5.b2 = b4
    def fonk5(self):
        b6 = []
        b5 = self.b3
        while b5:
            b6.fonk4(str(b5.b1))
            b5 = b5.b2
        return " -> ".join(b6)
def fonk6(b8, b9):
    b7 = class1(0)
    b5 = b7
    while b8 and b9:
        if b8.b1 <= b9.b1:
            b5.b2 = b8
            b8 = b8.b2
        else:
            b5.b2 = b9
            b9 = b9.b2
        b5 = b5.b2
    b5.b2 = b8 if b8 else b9
    return class2(b7.b2)
class class3(class2):
    def fonk7(self):
        return self.fonk8(self.b3)
    def fonk8(self, node):
        if not node.b2:
            return node.b1
        return fonk6(node.b1, self.fonk8(node.b2))
if b10 = = '__main__':
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