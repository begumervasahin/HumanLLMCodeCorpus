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
        while b6.b2 is not None:
            b6 = b6.b2
        b7 = class1(b1)
        b6.b2 = b7
        b7.b3 = b6
        self.b5 = b7
    def fonk4(self, b1, new_value):
        if self.b5.b1 = = b1:
            self.fonk3(new_value)
        elif self.b4.b1 = = b1:
            b7 = class1(new_value)
            b7.b2 = self.b4.b2
            b7.b3 = self.b4
            b7.b2.b3 = b7
            self.b4.b2 = b7
        else:
            b6 = self.b4.b2
            while b6.b1 != b1:
                b6 = b6.b2
            b7 = class1(new_value)
            b7.b2 = b6.b2
            b7.b2.b3 = b7
            b7.b3 = b6
            b6.b2 = b7
    def fonk5(self, b1):
        if self.b4.b1 = = b1:
            self.b4 = self.b4.b2
            self.b4.b3 = None
        elif self.b5.b1 = = b1:
            self.b5 = self.b5.b3
            self.b5.b2 = None
        else:
            b6 = self.b4.b2
            while b6.b1 != b1:
                b6 = b6.b2
            b6.b3.b2 = b6.b2
            b6.b2.b3 = b6.b3
    def fonk6(self):
        b6 = self.b5
        while b6 is not None:
            print(b6.b1)
            b6 = b6.b3
    def fonk7(self):
        b6 = self.b4
        while b6 is not None:
            print(b6.b1)
            b6 = b6.b2
b8 = class2(10)
b8.fonk3(20)
b8.fonk3(30)
b8.fonk3(40)
b8.fonk5(40)
print("Doubly Linked List:")
b8.fonk7()
print("\nDoubly Linked List in Reverse:")
b8.fonk6()