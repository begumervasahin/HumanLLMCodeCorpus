from binary_search_tree import Binary_Search_Tree
def fonk1(b9):
    return b9.b1 if b9 else -1
def fonk2(b9):
    b9.b1 = 1 + max(fonk1(b9.b5), fonk1(b9.b6))
class class1(Binary_Search_Tree):
    def fonk3(self, b9):
        b2 = b9.b6
        b2.b3 = b9.b3
        if b9.b3 is None:
            self.b4 = b2
        else:
            if b9 is b9.b3.b5:
                b9.b3.b5 = b2
            else:
                b9.b3.b6 = b2
        b9.b6 = b2.b5
        if b9.b6:
            b9.b6.b3 = b9
        b2.b5 = b9
        b9.b3 = b2
        fonk2(b9)
        fonk2(b2)
    def fonk4(self, b9):
        b7 = b9.b5
        b7.b3 = b9.b3
        if b9.b3 is None:
            self.b4 = b7
        else:
            if b9 is b9.b3.b5:
                b9.b3.b5 = b7
            else:
                b9.b3.b6 = b7
        b9.b5 = b7.b6
        if b9.b5:
            b9.b5.b3 = b9
        b7.b6 = b9
        b9.b3 = b7
        fonk2(b9)
        fonk2(b7)
    def fonk5(self, b9):
        while b9:
            fonk2(b9)
            b8 = fonk1(b9.b5) - fonk1(b9.b6)
            if b8 > 1:
                if fonk1(b9.b5.b5) >= fonk1(b9.b5.b6):
                    self.fonk4(b9)
                else:
                    self.fonk3(b9.b5)
                    self.fonk4(b9)
            elif b8 < -1:
                if fonk1(b9.b6.b6) >= fonk1(b9.b6.b5):
                    self.fonk3(b9)
                else:
                    self.fonk4(b9.b6)
                    self.fonk3(b9)
            b9 = b9.b3
    def fonk6(self, key):
        b10 = super(class1, self).fonk6(key)
        self.fonk5(b10)
    def fonk7(self, key):
        b11 = super(class1, self).fonk7(key)
        if b11:
            self.fonk5(b11.b3)