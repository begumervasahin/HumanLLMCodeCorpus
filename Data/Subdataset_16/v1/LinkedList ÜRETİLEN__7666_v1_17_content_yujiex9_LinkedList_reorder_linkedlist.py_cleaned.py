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
            return
        b5 = self.b3
        while b5.b2:
            b5 = b5.b2
        b5.b2 = b4
    def fonk4(self):
        b6 = self.b3
        while b6:
            print(b6.b1, b7 = " -> " if b6.b2 else "\n")
            b6 = b6.b2
def fonk5(b16):
    b10, b8 = b16.b3, b16.b3
    b9 = None
    while b8 and b8.b2:
        b9 = b10
        b10 = b10.b2
        b8 = b8.b2.b2
    b9.b2 = None
    return b10
def fonk6(b17):
    b10 = b17
    b11 = b10.b2
    b10.b2 = None
    b9 = b10
    b10 = b11
    while b10.b2:
        b11 = b10.b2
        b10.b2 = b9
        b9 = b10
        b10 = b11
    b10.b2 = b9
    return b10
def fonk7(b16, b18):
    b12 = b16.b3
    b13 = b18
    while b12.b2:
        b14 = b12.b2
        b12.b2 = b13
        b12 = b14
        b14 = b13.b2
        b13.b2 = b12
        b13 = b14
    b12.b2 = b13
if b15 = = "__main__":
    b16 = class2()
    for i in range(1, 10):
        b16.fonk3(i)
    print("Original List:")
    b16.fonk4()
    b17 = fonk5(b16)
    print("Middle class1:", b17.b1)
    b18 = fonk6(b17)
    print("Second Half Reversed:")
    b19 = class2()
    b19.b3 = b18
    b19.fonk4()
    fonk7(b16, b18)
    print("Reordered List:")
    b16.fonk4()