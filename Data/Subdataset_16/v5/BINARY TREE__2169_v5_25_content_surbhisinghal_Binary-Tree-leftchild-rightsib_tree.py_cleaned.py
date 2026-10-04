class class1:
    def fonk1(self, b3):
        self.b1 = None
        self.b2 = None
        self.b3 = b3
class class2:
    def fonk2(self):
        self.b4 = None
    def fonk3(self, target):
        if self.b4 is not None:
            return self.fonk4(target, self.b4)
        return None
    def fonk4(self, target, node):
        if node.b3 = = target:
            return node
        b5 = self.fonk4(target, node.b1) if node.b1 else None
        b6 = self.fonk4(target, node.b2) if node.b2 else None
        return b5 if b5 is not None else b6
    def fonk5(self, node, b8):
        if self.b4 is None:
            self.b4 = node
        else:
            if b8.b1 is None:
                b8.b1 = node
            else:
                b7 = b8.b1
                while b7.b2:
                    b7 = b7.b2
                b7.b2 = node
    def fonk6(self, node, b8 = None):
        if node is None:
            return
        if self.b4 = = node:
            self.b4 = None if self.b4.b1 is None else self.b4
            return
        if b8.b1 = = node:
            b8.b1 = node.b2
        else:
            b7 = b8.b1
            while b7.b2 != node:
                b7 = b7.b2
            b7.b2 = node.b2
def fonk7():
    b9 = class2()
    b10 = class1('A')
    b9.fonk5(b10, None)
    b11 = class1('B')
    b9.fonk5(b11, b10)
    b12 = class1('C')
    b13 = class1('D')
    b9.fonk5(b12, b11)
    b9.fonk5(b13, b11)
    b14 = class1('E')
    b15 = class1('F')
    b16 = class1('G')
    b9.fonk5(b14, b10)
    b9.fonk5(b15, b10)
    b9.fonk5(b16, b10)
    print(b9.fonk3('F').b3)
    print(b9.fonk3('G').b3)
    b9.fonk6(b16, b10)
    print(b9.fonk3('E').b3)
if b17 = = "__main__":
    fonk7()