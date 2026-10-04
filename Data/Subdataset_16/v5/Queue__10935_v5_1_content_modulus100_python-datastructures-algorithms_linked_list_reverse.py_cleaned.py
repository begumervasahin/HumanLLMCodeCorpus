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
    b6 = None
    for b1 in linked_list:
        b7 = class1(b1)
        b7.b2 = b6
        b6 = b7
    b5.b3 = b6
    return b5
if b8 = = "__main__":
    b9 = class2()
    for b1 in [4, 2, 5, 1, -3, 0]:
        b9.fonk3(b1)
    b10 = fonk6(b9)
    b11 = list(b10) == [0, -3, 1, 5, 2, 4] and list(b9) == list(fonk6(b10))
    print("Pass" if b11 else "Fail")