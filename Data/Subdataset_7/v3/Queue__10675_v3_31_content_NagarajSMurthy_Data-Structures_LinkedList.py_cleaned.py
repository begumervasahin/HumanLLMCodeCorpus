class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
class class2:
    def fonk2(self):
        self.b3 = None
        self.a1 = 0
    def fonk3(self, b1):
        b4 = class1(b1)
        b4.b2 = self.b3
        self.b3 = b4
        self.a1 += 1
    def fonk4(self):
        return self.a1
    def fonk5(self):
        b5 = self.b3
        a1 = 0
        while b5 is not None:
            a1 += 1
            b5 = b5.b2
        return a1
    def fonk6(self, b1):
        b4 = class1(b1)
        if self.b3 is None:
            self.b3 = b4
            return
        b5 = self.b3
        while b5.b2 is not None:
            b5 = b5.b2
        b5.b2 = b4
        self.a1 += 1
    def fonk7(self):
        b5 = self.b3
        while b5 is not None:
            print(b5.b1)
            b5 = b5.b2
    def fonk8(self, b1):
        if self.b3 is None:
            return
        b5 = self.b3
        b6 = None
        while b5 is not None:
            if b5.b1 = = b1:
                if b6 is None:
                    self.b3 = b5.b2
                else:
                    b6.b2 = b5.b2
                self.a1 -= 1
                return
            b6 = b5
            b5 = b5.b2
        print('Data not in the linked list')
b7 = class2()
b7.fonk3(10)
b7.fonk3(35)
b7.fonk3(67)
b7.fonk3(89)
b7.fonk3(341)
print("The a1 of the list is " + str(b7.fonk4()))
print("The a1 of the list is " + str(b7.fonk5()))
b7.fonk6(671)
print("The a1 of the list is " + str(b7.fonk5()))
b7.fonk7()
b7.fonk8(35)
print("The a1 of the list is " + str(b7.fonk5()))
b7.fonk7()