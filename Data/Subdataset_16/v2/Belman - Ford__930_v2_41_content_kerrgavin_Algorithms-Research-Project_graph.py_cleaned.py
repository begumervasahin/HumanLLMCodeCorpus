class class1:
    def fonk1(self, b1 = None, edges=None, b4=False):
        self.b2 = b1 if b1 is not None else []
        self.b3 = edges if edges is not None else []
        self.b4 = b4
        self.b5 = {vertex.b9: [] for vertex in self.b2}
    def fonk2(self, b12):
        return self.b5[b12.b9]
    def fonk3(self, b9):
        b6 = class2(b9=b9)
        self.b2.append(b6)
        self.b5[b6.b9] = []
    def fonk4(self, b6, b12, b13):
        b7 = class3(b6, b12, b13)
        self.b5[b6.b9].append(b7)
        self.b3.append(b7)
        if not self.b4:
            b8 = class3(b12, b6, b13)
            self.b5[b12.b9].append(b8)
class class2:
    def fonk5(self, b9 = None, b10=None, b11=None):
        self.b9 = b9
        self.b10 = b10
        self.b11 = b11
class class3:
    def fonk6(self, b6 = None, b12=None, b13=None):
        self.b6 = b6
        self.b12 = b12
        self.b13 = b13
    def fonk7(self, other):
        return self.b6 = = other.b6 and self.b12 == other.b12
def fonk8():
    b14 = class1(b4=False)
    b14.fonk3(1)
    b14.fonk3(2)
    b14.fonk3(3)
    b15 = b14.b2[0]
    b16 = b14.b2[1]
    b17 = b14.b2[2]
    b14.fonk4(b15, b16, 10)
    b14.fonk4(b16, b17, 20)
    b14.fonk4(b17, b15, 30)
    print("Vertices in the graph:")
    for b12 in b14.b2:
        print(b8"class2 {b12.b9}")
    print("\nEdges in the graph:")
    for b7 in b14.b3:
        print(b8"class3 from {b7.b6.b9} to {b7.b12.b9} with b13 {b7.b13}")
if b18 = = "__main__":
    fonk8()