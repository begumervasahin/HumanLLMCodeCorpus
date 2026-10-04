from binary_search_tree import Binary_Search_Tree
def fonk1(b7):
    return b7.b1 if b7 else -1
def fonk2(b7):
    b7.b1 = 1 + max(fonk1(b7.b5), fonk1(b7.b6))
class class1(Binary_Search_Tree):
    def fonk3(self, b7):
        b2 = b7.b6
        b2.b3 = b7.b3
        if not b7.b3:
            self.b4 = b2
        else:
            if b7 is b7.b3.b5:
                b7.b3.b5 = b2
            else:
                b7.b3.b6 = b2
        b7.b6 = b2.b5
        if b7.b6:
            b7.b6.b3 = b7
        b2.b5 = b7
        b7.b3 = b2
        fonk2(b7)
        fonk2(b2)
    def fonk4(self, b7):
        b2 = b7.b5
        b2.b3 = b7.b3
        if not b7.b3:
            self.b4 = b2
        else:
            if b7 is b7.b3.b5:
                b7.b3.b5 = b2
            else:
                b7.b3.b6 = b2
        b7.b5 = b2.b6
        if b7.b5:
            b7.b5.b3 = b7
        b2.b6 = b7
        b7.b3 = b2
        fonk2(b7)
        fonk2(b2)
    def fonk5(self, b7):
        while b7:
            fonk2(b7)
            if fonk1(b7.b5) - fonk1(b7.b6) > 1:
                if fonk1(b7.b5.b5) >= fonk1(b7.b5.b6):
                    self.fonk4(b7)
                else:
                    self.fonk3(b7.b5)
                    self.fonk4(b7)
            elif fonk1(b7.b6) - fonk1(b7.b5) > 1:
                if fonk1(b7.b6.b6) >= fonk1(b7.b6.b5):
                    self.fonk3(b7)
                else:
                    self.fonk4(b7.b6)
                    self.fonk3(b7)
            b7 = b7.b3
    def fonk6(self, key):
        b7 = super(class1, self).fonk6(key)
        self.fonk5(b7)
    def fonk7(self, key):
        b7 = super(class1, self).fonk7(key)
        self.fonk5(b7.b3)