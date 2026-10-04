class class1:
    def fonk1(self, b1 = None, b2=None, b3=False):
        self.b1 = b1 if b1 is not None else []
        self.b2 = b2 if b2 is not None else []
        self.b3 = b3
        self.b4 = {b5.b8: [] for b5 in self.b1}
    def fonk2(self, b5):
        return self.b4[b5.b8]
    def fonk3(self, b8):
        b5 = class2(b8=b8)
        self.b1.append(b5)
        self.b4[b5.b8] = []
    def fonk4(self, b11, b12, b13):
        b6 = class3(b11, b12, b13)
        self.b4[b11.b8].append(b6)
        self.b2.append(b6)
        if not self.b3:
            b7 = class3(b12, b11, b13)
            self.b4[b12.b8].append(b7)
class class2:
    def fonk5(self, b8 = None, b9=None, b10=None):
        self.b8 = b8
        self.b9 = b9
        self.b10 = b10
class class3:
    def fonk6(self, b11 = None, b12=None, b13=None):
        self.b11 = b11
        self.b12 = b12
        self.b13 = b13
    def fonk7(self, other):
        return self.b11 = = other.b11 and self.b12 == other.b12
def fonk8():
    b14 = class1(b3=False)
    b14.fonk3(1)
    b14.fonk3(2)
    b14.fonk3(3)
    b15 = b14.b1[0]
    b16 = b14.b1[1]
    b17 = b14.b1[2]
    b14.fonk4(b15, b16, 10)
    b14.fonk4(b16, b17, 20)
    b14.fonk4(b17, b15, 30)
    print("Vertices in the b14:")
    for b5 in b14.b1:
        print(f"class2 {b5.b8}")
    print("\nEdges in the b14:")
    for b6 in b14.b2:
        print(f"class3 from {b6.b11.b8} to {b6.b12.b8} with b13 {b6.b13}")
if b18 = = "__main__":
    fonk8()