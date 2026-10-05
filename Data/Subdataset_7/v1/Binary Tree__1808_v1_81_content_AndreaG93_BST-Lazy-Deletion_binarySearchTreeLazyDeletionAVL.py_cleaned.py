class class1:
    def fonk1(self, key, value):
        self.b1 = key
        self.b2 = value
        self.b3 = None
        self.b4 = None
        self.b5 = None
        self.b6 = True
    def fonk2(self):
        return self.b4 is not None
    def fonk3(self):
        return self.b3 is not None
    def fonk4(self):
        return (self.fonk3() and not self.fonk2()) or (self.fonk2() and not self.fonk3())
class class2:
    def fonk5(self, b7 = None):
        self.b8 = b7
    def fonk6(self, node):
        pass
class class3(class2):
    def fonk7(self, b7 = None):
        super().fonk7(b7)
    def fonk8(self, key, value):
        if not self.b8:
            self.b8 = class1(key, value)
            return
        else:
            b9 = self.b8
            b10 = None
            b11 = True
            while b9 is not None:
                b10 = b9
                if b9.b6:
                    if key <= b9.b1:
                        b9 = b9.b3
                        b11 = True
                    else:
                        b9 = b9.b4
                        b11 = False
                else:
                    if b9.fonk2() and key > b9.b4.b1:
                        b9 = b9.b4
                        b11 = False
                    elif b9.fonk3() and key < b9.b3.b1:
                        b9 = b9.b3
                        b11 = True
                    else:
                        b9.b6 = True
                        b9.b1 = key
                        b9.b2 = value
                        return
            b12 = class1(key, value)
            b12.b5 = b10
            if b11:
                b10.b3 = b12
                b12.b13 = True
            else:
                b10.b4 = b12
                b12.b13 = False
            if b10.fonk4():
                self.fonk6(b12)
    def fonk9(self, key):
        b9 = self.b8
        while b9:
            if key < b9.b1:
                b9 = b9.b3
            elif key > b9.b1:
                b9 = b9.b4
            else:
                if b9.b6:
                    b9.b6 = False
                    return True
                else:
                    b9 = b9.b3
        return False
    def fonk10(self, key, allowRestructuring):
        b14 = []
        b9 = self.b8
        while b9:
            if allowRestructuring and not b9.b6:
                b14.append(b9)
            if key < b9.b1:
                b9 = b9.b3
            elif key > b9.b1:
                b9 = b9.b4
            else:
                if b9.b6:
                    break
                else:
                    b9 = b9.b3
        for item in b14:
            self.deleteNode(item)
        return b9
if b15 = = "__main__":
    pass