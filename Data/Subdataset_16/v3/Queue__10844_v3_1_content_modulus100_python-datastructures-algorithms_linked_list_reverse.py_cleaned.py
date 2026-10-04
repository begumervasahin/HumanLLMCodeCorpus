class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
class class2:
    def fonk2(self):
        self.b3 = None
    def fonk3(self, b1):
        b4 = class1(b1)
        if not self.b3:
            self.b3 = b4
        else:
            b5 = self.b3
            while b5.b2:
                b5 = b5.b2
            b5.b2 = b4
    def fonk4(self):
        b5 = self.b3
        while b5:
            yield b5.b1
            b5 = b5.b2
    def fonk5(self):
        return str([b1 for b1 in self])
def fonk6(linked_list):
    b6 = class2()
    b5 = None
    for b1 in linked_list:
        b4 = class1(b1)
        b4.b2 = b5
        b5 = b4
    b6.b3 = b5
    return b6
b7 = class2()
b8 = [4, 2, 5, 1, -3, 0]
for b1 in b8:
    b7.fonk3(b1)
b6 = fonk6(b7)
b9 = list(b6) == list(reversed(b8)) and list(b7) == b8
print("Pass" if b9 else "Fail")