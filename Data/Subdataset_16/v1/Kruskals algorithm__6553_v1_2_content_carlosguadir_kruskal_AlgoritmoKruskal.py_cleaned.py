class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = []
    def fonk2(self, destino, b5):
        self.b2.append(class2(self.b1, destino, b5))
    def fonk3(self):
        return self.b1
    def fonk4(self):
        return self.b2
    def fonk5(self, destino):
        for enlace in self.b2:
            if enlace.getDestino() == destino:
                return enlace
        return -1
class class2:
    def fonk6(self, b3, b4, b5):
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
    def fonk7(self):
        return self.b3
    def fonk8(self):
        return self.b4
    def fonk9(self):
        return self.b5
    def fonk10(self, other):
        return self.b5 < other.b5
class class3:
    def fonk11(self):
        self.b6 = {}
        self.b7 = []
    def fonk12(self, b1):
        if b1 not in self.b6:
            self.b6[b1] = class1(b1)
    def fonk13(self, b3, b4, b5):
        if b3 in self.b6 and b4 in self.b6:
            self.b6[b3].fonk2(b4, b5)
            self.b6[b4].fonk2(b3, b5)
            self.b7.append(class2(b3, b4, b5))
    def fonk14(self):
        return list(self.b6.keys())
    def fonk15(self, b1):
        return self.b6[b1]
    def fonk16(self):
        return sorted(self.b7, b8 = lambda arco: arco.fonk9())
class class4:
    def fonk17(self, b13):
        b9 = class3()
        b6 = b13.fonk14()
        for n in b6:
            b9.fonk12(n)
        b7 = b13.fonk16()
        while b7:
            b10 = b7[0]
            if not self.fonk18(b9, b10, b9.fonk15(b10.fonk8()), b10.fonk8()):
                b9.fonk13(b10.fonk7(), b10.fonk8(), b10.fonk9())
            del b7[0]
        return b9
    def fonk18(self, b13, aVerificar, b4, m):
        b2 = b4.fonk4()
        if not b2:
            return False
        if b4.fonk5(aVerificar.fonk7()) != -1:
            return True
        for enlace in b2:
            b11 = enlace
            if b11.getDestino() != m:
                if self.fonk18(b13, aVerificar, b13.fonk15(b11.getDestino()), b4.fonk3()):
                    return True
        return False
if b12 = = "__main__":
    b13 = class3()
    b13.fonk12("A")
    b13.fonk12("B")
    b13.fonk12("C")
    b13.fonk12("D")
    b13.fonk13("A", "B", 1)
    b13.fonk13("A", "C", 3)
    b13.fonk13("B", "C", 1)
    b13.fonk13("B", "D", 4)
    b13.fonk13("C", "D", 2)
    b14 = class4()
    b15 = b14.fonk17(b13)
    print("Minimum Spanning Tree:")
    for b11 in b15.fonk14():
        b2 = b15.fonk15(b11).fonk4()
        for enlace in b2:
            print(f"{enlace.fonk7()} -- {enlace.fonk8()} == {enlace.fonk9()}")