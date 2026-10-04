
class class1:
    def fonk1(self, b2, b3, b1 = None):
        self.b2 = b2
        self.b3 = b3
        self.b4 = None
        self.b5 = None
        self.b1 = b1
        self.b6 = True
        self.a1 = 0
        self.b7 = None
    def fonk2(self):
        return self.b5 is not None
    def fonk3(self):
        return self.b4 is not None
    def fonk4(self):
        return (self.b4 is None) != (self.b5 is None)
class class2:
    def fonk5(self, b8 = None):
        self.b8 = b8
    def fonk6(self, b11):
        while b11:
            b9 = b11.b4.a1 if b11.b4 else -1
            b10 = b11.b5.a1 if b11.b5 else -1
            b11.a1 = max(b9, b10) + 1
            b11 = b11.b1
    def fonk7(self, b11):
        if b11.b7:
            b11.b1.b4 = None
        else:
            b11.b1.b5 = None
        self.fonk6(b11.b1)
class class3(class2):
    def fonk8(self, b8 = None):
        super().fonk8(b8)
    def fonk9(self, b2, b3):
        if not self.b8:
            self.b8 = class1(b2, b3)
            return
        b12 = self.b8
        b13 = None
        b14 = True
        while b12:
            b13 = b12
            if b12.b6:
                if b2 <= b12.b2:
                    b12 = b12.b4
                    b14 = True
                else:
                    b12 = b12.b5
                    b14 = False
            else:
                if b12.fonk2() and b2 > b12.b5.b2:
                    b12 = b12.b5
                    b14 = False
                elif b12.fonk3() and b2 < b12.b4.b2:
                    b12 = b12.b4
                    b14 = True
                else:
                    b12.b6 = True
                    b12.b2 = b2
                    b12.b3 = b3
                    return
        b15 = class1(b2, b3, b1=b13)
        if b14:
            b13.b4 = b15
            b15.b7 = True
        else:
            b13.b5 = b15
            b15.b7 = False
        if b13.fonk4():
            self.fonk6(b15)
    def fonk10(self, b2):
        b12 = self.b8
        while b12:
            if b2 < b12.b2:
                b12 = b12.b4
            elif b2 > b12.b2:
                b12 = b12.b5
            else:
                if b12.b6:
                    b12.b6 = False
                    return True
                b12 = b12.b4
        return False
    def fonk11(self, b2, b16 = True):
        b17 = []
        b12 = self.b8
        while b12:
            if b16 and not b12.b6:
                b17.append(b12)
            if b2 < b12.b2:
                b12 = b12.b4
            elif b2 > b12.b2:
                b12 = b12.b5
            else:
                if b12.b6:
                    break
                b12 = b12.b4
        for item in b17:
            self.fonk7(item)
        return b12
if b18 = = "__main__":
    b19 = class3()
    b19.fonk9(10, "Value for 10")
    b19.fonk9(20, "Value for 20")
    b19.fonk9(5, "Value for 5")
    b19.fonk10(10)
    b11 = b19.fonk11(10, b16=True)
    print("Search result:", b11.b3 if b11 and b11.b6 else "Not found")