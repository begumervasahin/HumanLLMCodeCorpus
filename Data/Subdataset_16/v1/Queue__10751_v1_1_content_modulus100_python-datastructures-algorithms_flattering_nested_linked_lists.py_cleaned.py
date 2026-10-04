class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
    def fonk2(self):
        return str(self.b1)
class class2:
    def fonk3(self, b3 = None):
        self.b3 = b3
    def fonk4(self, b1):
        b4 = class1(b1)
        if self.b3 is None:
            self.b3 = b4
            return
        b5 = self.b3
        while b5.b2 is not None:
            b5 = b5.b2
        b5.b2 = b4
def fonk5(list1, list2):
    b6 = class2()
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    b7 = list1.b3
    b8 = list2.b3
    while b7 is not None or b8 is not None:
        if b7 is None:
            b6.fonk4(b8.b1)
            b8 = b8.b2
        elif b8 is None:
            b6.fonk4(b7.b1)
            b7 = b7.b2
        elif b7.b1 <= b8.b1:
            b6.fonk4(b7.b1)
            b7 = b7.b2
        else:
            b6.fonk4(b8.b1)
            b8 = b8.b2
    return b6
class class3(class2):
    def fonk6(self):
        return self.fonk7(self.b3)
    def fonk7(self, b5):
        if b5.b2 is None:
            return fonk5(b5.b1, None)
        return fonk5(b5.b1, self.fonk7(b5.b2))
b9 = class2(class1(1))
b9.fonk4(3)
b9.fonk4(5)
b10 = class2(class1(2))
b10.fonk4(4)
b6 = fonk5(b9, b10)
b5 = b6.b3
while b5 is not None:
    print(b5.b1)
    b5 = b5.b2
b6 = fonk5(None, b9)
b5 = b6.b3
print("none, linked")
while b5 is not None:
    print(b5.b1)
    b5 = b5.b2
b11 = class3(class1(b9))
b11.fonk4(b10)
b12 = b11.fonk6()
b5 = b12.b3
print("b12")
while b5 is not None:
    print(b5.b1)
    b5 = b5.b2