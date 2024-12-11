class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
class class2:
    def fonk2(self):
        self.b3 = None
        self.a1 = 0
    def fonk3(self, b1):
        self.a1 += 1
        b4 = class1(b1)
        b4.b2 = self.b3
        self.b3 = b4
    def fonk4(self):
        return self.a1
    def fonk5(self, b1):
        self.a1 += 1
        b4 = class1(b1)
        if not self.b3:
            self.b3 = b4
            return
        b5 = self.b3
        while b5.b2:
            b5 = b5.b2
        b5.b2 = b4
    def fonk6(self):
        b6 = self.b3
        while b6:
            print(b6.b1)
            b6 = b6.b2
    def fonk7(self, b1):
        if not self.b3:
            print('Linked list is empty')
            return
        self.a1 -= 1
        if self.b3.b1 = = b1:
            self.b3 = self.b3.b2
            return
        b7 = None
        b6 = self.b3
        while b6 and b6.b1 != b1:
            b7 = b6
            b6 = b6.b2
        if b6 is None:
            print('Data not found in the linked list')
            return
        b7.b2 = b6.b2
b8 = class2()
b8.fonk3(10)
b8.fonk3(35)
b8.fonk3(67)
b8.fonk3(89)
b8.fonk3(341)
print("The a1 of the list is:", b8.fonk4())
b8.fonk5(671)
print("The a1 of the list is:", b8.fonk4())
b8.fonk6()
b8.fonk7(20)
print("The a1 of the list is:", b8.fonk4())
b8.fonk6()