class class1:
    def fonk1(self, b3):
        self.b1 = None
        self.b2 = None
        self.b3 = b3
class class2:
    def fonk2(self):
        self.b4 = None
    def fonk3(self, b6):
        if self.b4 is not None:
            return self.fonk4(b6, self.b4)
        else:
            return None
    def fonk4(self, b6, b9):
        b5 = b7 = None
        if b6 = = b9.b3:
            return b9
        if b9.b1:
            b5 = self.fonk4(b6, b9.b1)
        if b9.b2:
            b7 = self.fonk4(b6, b9.b2)
        if b5 is not None:
            return b5
        elif b7 is not None:
            return b7
    def fonk5(self, new_node, b8):
        if self.b4 is None:
            self.b4 = new_node
        else:
            if b8.b1 is None:
                b8.b1 = new_node
            else:
                b8 = b8.b1
                while b8.b2 is not None:
                    b8 = b8.b2
                b8.b2 = new_node
    def fonk6(self, b9, b8 = None):
        if b9 is None:
            return
        if self.b4 = = b9:
            if self.b4.b1:
                self.b4 = None
        else:
            if b9 = = b8.b1:
                b8.b1 = b8.b1.b2
            else:
                b8 = b8.b1
                while b8.b2 != b9:
                    b8 = b8.b2
                b8.b2 = b8.b2.b2
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
    print(b10.fonk3('F').b3)
    print(b10.fonk3('G').b3)
    b10.fonk6(b17, b11)
    print(b10.fonk3('E').b3)
if b18 = = "__main__":
    fonk7()