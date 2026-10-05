class class1:
    def fonk1(self, b2, b1 = None):
        self.b2 = b2
        self.b1 = b1
    def fonk2(self, other):
        if other is None:
            return False
        return self.b2 = = other.b2
    def fonk3(self):
        return str(self.b2)
def fonk4(insertion_sort):
    def fonk5(self, *args, **kwargs):
        if self.a2 > 1:
            class2.a1 += 1
        fonk16(self)
    return insertion_counter
class class2:
    a1 = 0
    def fonk6(self, b3 = None):
        self.b4 = None
        self.b5 = None
        self.a2 = 0
        if b3:
            for item in b3:
                self.fonk14(item)
    def fonk7(self):
        return self.a2
    def fonk8(self, other):
        if self.a2 != other.a2:
            return False
        if self.b4 != other.b4 or self.b5 != other.b5:
            return False
        b6 = self.b4
        b7 = other.b4
        while b6 is not None:
            if b6 != b7:
                return False
            b6 = b6.b1
            b7 = b7.b1
        return True
    def fonk9(self):
        b8 = []
        b9 = self.b4
        while b9:
            b8.append(b9.b2)
            b9 = b9.b1
        return str(b8)
    def fonk10(self):
        return self.a2
    def fonk11(self):
        return self.a2 = = 0
    def fonk12(self):
        return self.b4.b2 if self.b4 else None
    def fonk13(self, b11):
        b10 = class1(b11, self.b4)
        if self.fonk11():
            self.b5 = b10
        self.b4 = b10
        self.a2 += 1
    def fonk14(self, b11):
        b10 = class1(b11)
        if self.fonk11():
            self.b4 = b10
        else:
            self.b5.b1 = b10
        self.b5 = b10
        self.a2 += 1
    def fonk15(self):
        if self.fonk11():
            return None
        b11 = self.b4.b2
        self.b4 = self.b4.b1
        self.a2 -= 1
        if self.fonk11():
            self.b5 = None
        return b11
    @_insertion_wrapper
    def fonk16(self):
        if self.b4 is None:
            return
        b12 = self.b4.b1
        b13 = class2()
        b13.fonk14(self.fonk15())
        b14 = self.fonk15()
        while b12 is not None:
            if b14 >= b13.b5.b2:
                b13.fonk14(b14)
            elif b14 <= b13.b4.b2:
                b13.fonk13(b14)
            else:
                b15 = b13.b4
                while b15.b1 is not None:
                    if b14 <= b15.b1.b2 and b14 > b15.b2:
                        b16 = class1(b14, b15.b1)
                        b15.b1 = b16
                        b13.a2 += 1
                        b15 = b15.b1
                    else:
                        b15 = b15.b1
            b14 = self.fonk15()
            b12 = b12.b1
        self.b4 = b13.b4
        self.b5 = b13.b5
        self.a2 = b13.a2
b17 = class2()
b17.fonk14(6)
b17.fonk14(2)
b17.fonk14(3)
b17.fonk14(1)
b17.fonk14(4)
b17.fonk14(5)
print(b17)
b17.fonk16()
print(b17)