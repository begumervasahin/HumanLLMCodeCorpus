class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
        self.b3 = None
        self.b4 = None
        self.b5 = None
        self.b6 = True
    def fonk2(self):
        return self.b4 is not None
    def fonk3(self):
        return self.b3 is not None
    def fonk4(self):
        return (self.fonk3() and not self.fonk2()) or \
               (self.fonk2() and not self.fonk3())
class class2:
    def fonk5(self, b7 = None):
        self.b7 = b7
    def fonk6(self, node):
        pass
class class3(class2):
    def fonk7(self, b7 = None):
        super().fonk7(b7)
    def fonk8(self, b1, b2):
        if not self.b7:
            self.b7 = class1(b1, b2)
            return
        b8 = self.b7
        b9 = None
        b10 = True
        while b8 is not None:
            b9 = b8
            if b8.b6:
                if b1 <= b8.b1:
                    b8 = b8.b3
                    b10 = True
                else:
                    b8 = b8.b4
                    b10 = False
            else:
                if b8.fonk2() and b1 > b8.b4.b1:
                    b8 = b8.b4
                    b10 = False
                elif b8.fonk3() and b1 < b8.b3.b1:
                    b8 = b8.b3
                    b10 = True
                else:
                    b8.b6 = True
                    b8.b1 = b1
                    b8.b2 = b2
                    return
        b11 = class1(b1, b2)
        b11.b5 = b9
        if b10:
            b9.b3 = b11
            b11.b12 = True
        else:
            b9.b4 = b11
            b11.b12 = False
        if b9.fonk4():
            self.fonk6(b11)
    def fonk9(self, b1):
        b8 = self.b7
        while b8:
            if b1 < b8.b1:
                b8 = b8.b3
            elif b1 > b8.b1:
                b8 = b8.b4
            else:
                if b8.b6:
                    b8.b6 = False
                    return True
                else:
                    b8 = b8.b3
        return False
    def fonk10(self, b1, allow_restructuring):
        b13 = []
        b8 = self.b7
        while b8:
            if allow_restructuring and not b8.b6:
                b13.append(b8)
            if b1 < b8.b1:
                b8 = b8.b3
            elif b1 > b8.b1:
                b8 = b8.b4
            else:
                if b8.b6:
                    break
                else:
                    b8 = b8.b3
        for item in b13:
            self.delete_node(item)
        return b8
if b14 = = "__main__":
    pass