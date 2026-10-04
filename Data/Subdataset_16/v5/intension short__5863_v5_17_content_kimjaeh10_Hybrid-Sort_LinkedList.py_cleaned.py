class class1:
    b1 = 'b3', 'b2'
    def fonk1(self, b3, b2 = None):
        self.b3 = b3
        self.b2 = b2
    def fonk2(self, other):
        return isinstance(other, class1) and self.b3 = = other.b3
    def fonk3(self):
        return str(self.b3)
def fonk4(insertion_sort):
    def fonk5(self, *args, **kwargs):
        if self.a2 > 1:
            class2.a1 += 1
        fonk15(self)
    return insertion_counter
class class2:
    a1 = 0
    def fonk6(self, b4 = None):
        self.b5 = None
        self.b6 = None
        self.a2 = 0
        if b4:
            for item in b4:
                self.fonk13(item)
    def fonk7(self):
        return self.a2
    def fonk8(self, other):
        if self.a2 != other.a2:
            return False
        node_self, b7 = self.b5, other.b5
        while node_self and b7:
            if node_self != b7:
                return False
            node_self, b7 = node_self.b2, b7.b2
        return node_self is None and b7 is None
    def fonk9(self):
        b8 = []
        b9 = self.b5
        while b9:
            b8.append(b9.b3)
            b9 = b9.b2
        return str(b8)
    def fonk10(self):
        return self.a2 = = 0
    def fonk11(self):
        return self.b5.b3 if self.b5 else None
    def fonk12(self, b3):
        b10 = class1(b3, self.b5)
        self.b5 = b10
        if self.a2 = = 0:
            self.b6 = b10
        self.a2 += 1
    def fonk13(self, b3):
        b10 = class1(b3)
        if self.fonk10():
            self.b5 = b10
        else:
            self.b6.b2 = b10
        self.b6 = b10
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
    @_insertion_wrapper
    def fonk15(self):
        if self.fonk10():
            return
        b11 = class2()
        b11.fonk13(self.fonk14())
        while self.b5:
            b12 = self.fonk14()
            if b12 <= b11.b5.b3:
                b11.fonk12(b12)
            elif b12 >= b11.b6.b3:
                b11.fonk13(b12)
            else:
                b9 = b11.b5
                while b9.b2 and b9.b2.b3 < b12:
                    b9 = b9.b2
                b10 = class1(b12, b9.b2)
                b9.b2 = b10
                b11.a2 += 1
        self.b5, self.b6, self.a2 = b11.b5, b11.b6, b11.a2
if b13 = = "__main__":
    b14 = class2([6, 2, 3, 1, 4, 5])
    print("Before sorting:", b14)
    b14.fonk15()
    print("After sorting: ", b14)