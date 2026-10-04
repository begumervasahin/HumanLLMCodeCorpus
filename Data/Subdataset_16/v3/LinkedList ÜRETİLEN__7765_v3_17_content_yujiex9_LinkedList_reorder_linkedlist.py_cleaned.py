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
def fonk5(b17):
    b8 = b17.b3
    b9 = b17.b3
    b10 = None
    while b9 and b9.b2:
        b10 = b8
        b8 = b8.b2
        b9 = b9.b2.b2
    if b10:
        b10.b2 = None
    return b8
def fonk6(b3):
    b11 = None
    b6 = b3
    while b6:
        b2 = b6.b2
        b6.b2 = b11
        b11 = b6
        b6 = b2
    return b11
def fonk7(first_half, second_half):
    b12 = first_half.b3
    b13 = second_half
    while b12 and b13:
        b14 = b12.b2
        b15 = b13.b2
        b12.b2 = b13
        if b14:
            b13.b2 = b14
        b12 = b14
        b13 = b15
if b16 = = "__main__":
    b17 = class2()
    for i in range(1, 10):
        b17.fonk3(i)
    print("Original List:")
    b17.fonk4()
    b18 = fonk5(b17)
    print("Middle class1:", b18.b1)
    b19 = fonk6(b18)
    print("Second Half Reversed:")
    b20 = class2()
    b20.b3 = b19
    b20.fonk4()
    fonk7(b17, b19)
    print("Reordered List:")
    b17.fonk4()