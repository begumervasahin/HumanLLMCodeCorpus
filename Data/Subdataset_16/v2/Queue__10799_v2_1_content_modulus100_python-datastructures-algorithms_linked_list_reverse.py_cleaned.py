class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
class class2:
    def fonk2(self):
        self.b3 = None
    def fonk3(self, b1):
        if not self.b3:
            self.b3 = class1(b1)
        else:
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
        return str([b1 for b1 in self])
def fonk6(linked_list):
    b5 = class2()
    b4 = None
    for b1 in linked_list:
        b6 = class1(b1)
        b6.b2 = b4
        b4 = b6
    b5.b3 = b4
    return b5
b7 = class2()
for b1 in [4, 2, 5, 1, -3, 0]:
    b7.fonk3(b1)
b5 = fonk6(b7)
b8 = list(b5) == [0, -3, 1, 5, 2, 4] and list(b7) == list(fonk6(b5))
print("Pass" if b8 else "Fail")