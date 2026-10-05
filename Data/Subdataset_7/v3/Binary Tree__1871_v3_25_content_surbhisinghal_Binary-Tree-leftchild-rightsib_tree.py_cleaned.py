class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
class class2:
    def fonk2(self):
        self.b4 = None
    def fonk3(self, target):
        if self.b4 is not None:
            return self.fonk4(target, self.b4)
        else:
            return None
    def fonk4(self, target, b9):
        if b9 is None:
            return None
        if b9.b1 = = target:
            return b9
        b5 = self.fonk4(target, b9.b2)
        if b5:
            return b5
        b6 = self.fonk4(target, b9.b3)
        if b6:
            return b6
        return None
    def fonk5(self, new_node, b8):
        if self.b4 is None:
            self.b4 = new_node
        else:
            b7 = b8.b2 if b8 else self.b4
            while b7.b3:
                b7 = b7.b3
            b7.b3 = new_node
    def fonk6(self, b9, b8 = None):
        if b9 is None:
            return
        if self.b4 = = b9:
            if self.b4.b2:
                self.b4 = None
        else:
            if b9 = = b8.b2:
                b8.b2 = b9.b3
            else:
                b7 = b8.b2 if b8 else self.b4
                while b7.b3 != b9:
                    b7 = b7.b3
                b7.b3 = b9.b3
def fonk7():
    b10 = class2()
    b11 = class1('A')
    b10.fonk5(b11, None)
    b12 = class1('B')
    b10.fonk5(b12, b11)
    b13 = class1('C')
    b14 = class1('D')
    b10.fonk5(b14, b12)
    b10.fonk5(b13, b12)
    b15 = class1('E')
    b16 = class1('F')
    b17 = class1('G')
    b10.fonk5(b15, b11)
    b10.fonk5(b16, b11)
    b10.fonk5(b17, b11)
    print(b10.fonk3('F').b1)
    print(b10.fonk3('G').b1)
    b10.fonk6(b17, b11)
    print(b10.fonk3('E').b1)
if b18 = = "__main__":
    fonk7()