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
        if self.b3 is None:
            self.b3 = class1(b1)
            return
        b4 = self.b3
        while b4.b2 is not None:
            b4 = b4.b2
        b4.b2 = class1(b1)
def fonk5(list1, list2):
    b5 = class2()
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    b6 = list1.b3
    b7 = list2.b3
    while b6 is not None or b7 is not None:
        if b6 is None:
            b5.fonk4(b7)
            b7 = b7.b2
        elif b7 is None:
            b5.fonk4(b6)
            b6 = b6.b2
        elif b6.b1 <= b7.b1:
            b5.fonk4(b6)
            b6 = b6.b2
        else:
            b5.fonk4(b7)
            b7 = b7.b2
    return b5
class class3(class2):
    def fonk6(self):
        return self.fonk7(self.b3)
    def fonk7(self, b4):
        if b4.b2 is None:
            return fonk5(b4.b1, None)
        return fonk5(b4.b1, self.fonk7(b4.b2))
b8 = class2(class1(1))
b8.fonk4(3)
b8.fonk4(5)
b9 = class3(class1(b8))
b10 = class2(class1(2))
b10.fonk4(4)
b9.fonk4(class1(b10))
b5 = fonk5(b8, b10)
b4 = b5.b3
while b4 is not None:
    print(b4.b1)
    b4 = b4.b2
b5 = fonk5(None, b8)
b4 = b5.b3
print("None, Linked")
while b4 is not None:
    print(b4.b1)
    b4 = b4.b2
b9 = class3(class1(b8))
b9.fonk4(b10)
b11 = b9.fonk6()
b4 = b11.b3
print("Flattened")
while b4 is not None:
    print(b4.b1)
    b4 = b4.b2