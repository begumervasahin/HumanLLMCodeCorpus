class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
class class2:
    def fonk2(self, b3 = None):
        self.b3 = b3
    def fonk3(self, new_element):
        if self.b3:
            b4 = self.b3
            while b4.b2:
                b4 = b4.b2
            b4.b2 = new_element
        else:
            self.b3 = new_element
    def fonk4(self, b5):
        b4 = self.b3
        a1 = 1
        while b4 and a1 < b5:
            b4 = b4.b2
            a1 += 1
        return b4
    def fonk5(self, new_element, b5):
        if b5 = = 1:
            new_element.b2 = self.b3
            self.b3 = new_element
        else:
            b6 = self.fonk4(b5 - 1)
            if b6:
                new_element.b2 = b6.b2
                b6.b2 = new_element
    def fonk6(self, b1):
        b6 = None
        b4 = self.b3
        while b4:
            if b4.b1 = = b1:
                if b6:
                    b6.b2 = b4.b2
                else:
                    self.b3 = b4.b2
                break
            b6 = b4
            b4 = b4.b2
b7 = class1(1)
b8 = class1(2)
b9 = class1(3)
b10 = class1(4)
b11 = class2(b7)
b11.fonk3(b8)
b11.fonk3(b9)
print(b11.b3.b2.b2.b1)
print(b11.fonk4(3).b1)
b11.fonk5(b10, 3)
print(b11.fonk4(3).b1)
b11.fonk6(1)
print(b11.fonk4(1).b1)
print(b11.fonk4(2).b1)
print(b11.fonk4(3).b1)
