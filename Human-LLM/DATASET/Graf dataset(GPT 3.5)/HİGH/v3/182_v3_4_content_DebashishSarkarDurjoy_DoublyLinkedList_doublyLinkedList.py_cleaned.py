class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
class class2:
    def fonk2(self, b1):
        self.b4 = class1(b1)
        self.b5 = self.b4
    def fonk3(self, b1):
        b6 = self.b4
        while b6.b2:
            b6 = b6.b2
        b7 = class1(b1)
        b6.b2 = b7
        b7.b3 = b6
        self.b5 = b7
    def fonk4(self, target_value, new_value):
        if self.b5.b1 = = target_value:
            self.fonk3(new_value)
        else:
            b6 = self.b4.b2
            while b6.b1 != target_value:
                b6 = b6.b2
            b7 = class1(new_value)
            b7.b2 = b6.b2
            b7.b2.b3 = b7
            b7.b3 = b6
            b6.b2 = b7
    def fonk5(self, target_value):
        if self.b4.b1 = = target_value:
            self.b4 = self.b4.b2
            self.b4.b3 = None
        elif self.b5.b1 = = target_value:
            self.b5 = self.b5.b3
            self.b5.b2 = None
        else:
            b6 = self.b4.b2
            while b6.b1 != target_value:
                b6 = b6.b2
            b6.b3.b2 = b6.b2
            b6.b2.b3 = b6.b3
    def fonk6(self):
        b6 = self.b5
        while b6:
            print(b6.b1)
            b6 = b6.b3
    def fonk7(self):
        b6 = self.b4
        while b6:
            print(b6.b1)
            b6 = b6.b2
if b8 = = "__main__":
    b9 = class2(10)
    b9.fonk3(20)
    b9.fonk3(30)
    b9.fonk3(40)
    b9.fonk5(40)
    b9.fonk7()
    b9.fonk6()