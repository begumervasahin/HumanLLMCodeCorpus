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
        b8 = [str(node.b2) for node in self]
        return '[' + ', '.join(b8) + ']'
    def fonk10(self):
        return self.a2
    def fonk11(self):
        return self.a2 = = 0
    def fonk12(self):
        return self.b4.b2 if self.b4 else None
    def fonk13(self, b10):
        b9 = class1(b10, self.b4)
        if self.fonk11():
            self.b5 = b9
        self.b4 = b9
        self.a2 += 1
    def fonk14(self, b10):
        b9 = class1(b10)
        if self.fonk11():
            self.b4 = b9
        else:
            self.b5.b1 = b9
        self.b5 = b9
        self.a2 += 1
    def fonk15(self):
        if self.fonk11():
            return None
        b10 = self.b4.b2
        self.b4 = self.b4.b1
        self.a2 -= 1
        if self.fonk11():
            self.b5 = None
        return b10
    @_insertion_wrapper
    def fonk16(self):
        if self.b4 is None:
            return
        b11 = self.b4.b1
        b12 = class2()
        b12.fonk14(self.fonk15())
        b13 = self.fonk15()
        while b11 is not None:
            if b13 >= b12.b5.b2:
                b12.fonk14(b13)
            elif b13 <= b12.b4.b2:
                b12.fonk13(b13)
            else:
                b14 = b12.b4
                while b14.b1 is not None:
                    if b13 <= b14.b1.b2 and b13 > b14.b2:
                        b15 = class1(b13, b14.b1)
                        b14.b1 = b15
                        b12.a2 += 1
                        b14 = b14.b1
                    else:
                        b14 = b14.b1
            b13 = self.fonk15()
            b11 = b11.b1
        self.b4 = b12.b4
        self.b5 = b12.b5
        self.a2 = b12.a2
b16 = class2()
b16.fonk14(6)
b16.fonk14(2)
b16.fonk14(3)
b16.fonk14(1)
b16.fonk14(4)
b16.fonk14(5)
print(b16)
b16.fonk16()
print(b16)