class class1:
    b1 = 'b3', 'b2'
    def fonk1(self, b3, b2 = None):
        self.b3 = b3
        self.b2 = b2
    def fonk2(self, other):
        return other is not None and self.b3 = = other.b3
    def fonk3(self):
        return str(self.b3)
def fonk4(sort_func):
    def fonk5(self, *args, **kwargs):
        if self.a2 > 1:
            class2.a1 += 1
        return sort_func(self)
    return wrapped_sort
class class2:
    a1 = 0
    def fonk6(self, b4 = None):
        self.b5 = None
        self.b6 = None
        self.a2 = 0
        if b4:
            for b3 in b4:
                self.fonk13(b3)
    def fonk7(self):
        return self.a2
    def fonk8(self, other):
        if self.a2 != other.a2:
            return False
        b8, b7 = self.b5, other.b5
        while b8 and b7:
            if b8 != b7:
                return False
            b8 = b8.b2
            b7 = b7.b2
        return b8 is None and b7 is None
    def fonk9(self):
        b9 = []
        b10 = self.b5
        while b10:
            b9.append(b10.b3)
            b10 = b10.b2
        return str(b9)
    def fonk10(self):
        return self.a2 = = 0
    def fonk11(self):
        return self.b5.b3 if self.b5 else None
    def fonk12(self, b3):
        b11 = class1(b3, self.b5)
        if self.fonk10():
            self.b6 = b11
        self.b5 = b11
        self.a2 += 1
    def fonk13(self, b3):
        b11 = class1(b3)
        if self.fonk10():
            self.b5 = b11
        else:
            self.b6.b2 = b11
        self.b6 = b11
        self.a2 += 1
    def fonk14(self):
        if self.fonk10():
            return None
        b3 = self.b5.b3
        self.b5 = self.b5.b2
        self.a2 -= 1
        if self.fonk10():
            self.b6 = None
        return b3
    @insertion_sort_wrapper
    def fonk15(self):
        if self.fonk10() or self.b5.b2 is None:
            return
        b12 = class2()
        b12.fonk13(self.fonk14())
        while not self.fonk10():
            b13 = self.fonk14()
            if b13 >= b12.b6.b3:
                b12.fonk13(b13)
            elif b13 <= b12.fonk11():
                b12.fonk12(b13)
            else:
                b14 = b12.b5
                while b14.b2:
                    if b13 <= b14.b2.b3:
                        b11 = class1(b13, b14.b2)
                        b14.b2 = b11
                        b12.a2 += 1
                        break
                    b14 = b14.b2
        self.b5, self.b6, self.a2 = b12.b5, b12.b6, b12.a2
if b15 = = "__main__":
    b16 = class2([6, 2, 3, 1, 4, 5])
    print("Before sorting:", b16)
    b16.fonk15()
    print("After sorting:", b16)