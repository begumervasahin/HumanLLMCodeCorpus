class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
class class2:
    def fonk2(self):
        self.b3 = None
        self.a1 = 0
        self.b4 = []
    def fonk3(self, b1):
        self.a1 += 1
        self.b4.append(b1)
        b5 = class1(b1)
        if not self.b3:
            self.b3 = b5
        else:
            b5.b2 = self.b3
            self.b3 = b5
    def fonk4(self):
        return self.a1
    def fonk5(self):
        b6 = self.b3
        a1 = 0
        while b6 is not None:
            a1 += 1
            b6 = b6.b2
        return a1
    def fonk6(self, b1):
        self.a1 += 1
        b5 = class1(b1)
        b6 = self.b3
        while b6.b2 is not None:
            b6 = b6.b2
        b6.b2 = b5
    def fonk7(self):
        b6 = self.b3
        while b6 is not None:
            print("%d\n" % b6.b1)
            b6 = b6.b2
    def fonk8(self, b1):
        if self.b3 is None:
            return
        if b1 not in self.b4:
            print('Data not in the linked list')
        self.a1 += 1
        b7 = self.b3
        b8 = None
        try:
            while b7.b1 != b1:
                b8 = b7
                b7 = b7.b2
            if b8 is None:
                self.b3 = b7.b2
            else:
                b8.b2 = b7.b2
        except AttributeError:
            pass
b9 = class2()
b9.fonk3(10)
b9.fonk3(35)
b9.fonk3(67)
b9.fonk3(89)
b9.fonk3(341)
print("The a1 of the list is " + str(b9.fonk5()))
print("The a1 of the list is " + str(b9.fonk5()))
b9.fonk6(671)
print("The a1 of the list is " + str(b9.fonk5()))
b9.fonk7()
b9.fonk8(20)
print("The a1 of the list is " + str(b9.fonk5()))
b9.fonk7()