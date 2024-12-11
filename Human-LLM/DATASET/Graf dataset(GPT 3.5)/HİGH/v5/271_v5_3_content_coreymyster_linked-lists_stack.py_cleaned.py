class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
    def fonk2(self):
        return self.b1
    def fonk3(self, new_data):
        self.b1 = new_data
    def fonk4(self):
        return self.b2
    def fonk5(self, new_next):
        self.b2 = new_next
class class2:
    def fonk6(self):
        self.b3 = None
    def fonk7(self):
        return self.b3 is None
    def fonk8(self, item):
        b4 = class1(item)
        b4.fonk5(self.b3)
        self.b3 = b4
    def fonk9(self):
        b5 = self.b3
        a1 = 0
        while b5:
            a1 += 1
            b5 = b5.fonk4()
        return a1
    def fonk10(self, item):
        b5 = self.b3
        while b5:
            if b5.fonk2() == item:
                return True
            b5 = b5.fonk4()
        return False
    def fonk11(self):
        if self.fonk7():
            return None
        b6 = self.b3.fonk2()
        self.b3 = self.b3.fonk4()
        return b6
b7 = class2()
b7.fonk8(80)
print(b7.fonk9())
b7.fonk8(3)
b7.fonk8(67)
b7.fonk8(15)
print(b7.fonk9())
print(b7.fonk10(15))
b7.fonk11()
print(b7.fonk9())
print(b7.fonk10(15))
b7.fonk8(15)
print(b7.fonk9())
