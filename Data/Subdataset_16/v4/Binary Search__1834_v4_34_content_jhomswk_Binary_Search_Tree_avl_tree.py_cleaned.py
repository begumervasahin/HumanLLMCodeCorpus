from binary_search_tree import Binary_Search_Tree
def fonk1(b8):
    return b8.b1 if b8 else -1
def fonk2(b8):
    b8.b1 = 1 + max(fonk1(b8.b5), fonk1(b8.b6))
class class1(Binary_Search_Tree):
    def fonk3(self, b8):
        b2 = b8.b6
        b2.b3 = b8.b3
        if b8.b3 is None:
            self.b4 = b2
        else:
            if b8 is b8.b3.b5:
                b8.b3.b5 = b2
            else:
                b8.b3.b6 = b2
        b8.b6 = b2.b5
        if b8.b6:
            b8.b6.b3 = b8
        b2.b5 = b8
        b8.b3 = b2
        fonk2(b8)
        fonk2(b2)
    def fonk4(self, b8):
        b2 = b8.b5
        b2.b3 = b8.b3
        if b8.b3 is None:
            self.b4 = b2
        else:
            if b8 is b8.b3.b5:
                b8.b3.b5 = b2
            else:
                b8.b3.b6 = b2
        b8.b5 = b2.b6
        if b8.b5:
            b8.b5.b3 = b8
        b2.b6 = b8
        b8.b3 = b2
        fonk2(b8)
        fonk2(b2)
    def fonk5(self, b8):
        while b8:
            fonk2(b8)
            b7 = fonk1(b8.b5) - fonk1(b8.b6)
            if b7 > 1:
                if fonk1(b8.b5.b5) >= fonk1(b8.b5.b6):
                    self.fonk4(b8)
                else:
                    self.fonk3(b8.b5)
                    self.fonk4(b8)
            elif b7 < -1:
                if fonk1(b8.b6.b6) >= fonk1(b8.b6.b5):
                    self.fonk3(b8)
                else:
                    self.fonk4(b8.b6)
                    self.fonk3(b8)
            b8 = b8.b3
    def fonk6(self, key):
        b8 = super(class1, self).fonk6(key)
        self.fonk5(b8)
    def fonk7(self, key):
        b8 = super(class1, self).fonk7(key)
        if b8:
            self.fonk5(b8.b3)