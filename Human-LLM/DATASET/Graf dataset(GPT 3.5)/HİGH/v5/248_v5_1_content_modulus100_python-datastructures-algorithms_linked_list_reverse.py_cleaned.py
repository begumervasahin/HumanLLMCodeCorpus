class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
class class2:
    def fonk2(self):
        self.b3 = None
    def fonk3(self, b1):
        if self.b3 is None:
            self.b3 = class1(b1)
            return
        b4 = self.b3
        while b4.b2:
            b4 = b4.b2
        b4.b2 = class1(b1)
    def fonk4(self):
        b4 = self.b3
        while b4:
            yield b4.b1
            b4 = b4.b2
    def fonk5(self):
        b5 = [b1 for b1 in self]
        return str(b5)
def fonk6(linked_list):
    b6 = class2()
    b4 = None
    for b1 in linked_list:
        if b4 is None:
            b4 = class1(b1)
        else:
            b7 = class1(b1)
            b7.b2 = b4
            b4 = b7
    b6.b3 = b4
    return b6
b8 = class2()
for b1 in [4, 2, 5, 1, -3, 0]:
    b8.fonk3(b1)
b9 = fonk6(b8)
b10 = list(b9) == [0, -3, 1, 5, 2, 4] and list(b8) == list(fonk6(b9))
print("Pass" if b10 else "Fail")