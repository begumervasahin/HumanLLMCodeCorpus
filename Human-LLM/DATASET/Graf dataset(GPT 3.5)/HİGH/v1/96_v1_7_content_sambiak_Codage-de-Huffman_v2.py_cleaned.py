import queue as Q
class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
    def fonk2(self, other):
        return int.fonk2(self.b2, other.b2)
    def fonk3(self, other):
        return int.fonk3(self.b2, other.b2)
    def fonk4(self, other):
        return int.fonk4(self.b2, other.b2) and self.b1 = = other.b1
    def fonk5(self, other):
        return int.fonk5(self.b2, other.b2)
    def fonk6(self, other):
        return int.fonk6(self.b2, other.b2)
    def fonk7(self):
        return "(" + self.b1.fonk15() + self.b2.fonk15() + ")"
    def fonk8(self):
        return self.fonk15()
class class2:
    def fonk9(self):
        self.b3 = []
    def fonk10(self):
        return len(self.b3)
    def fonk11(self):
        return self.b3.pop()
    def fonk12(self, elem):
        for i, el in enumerate(self.b3):
            if elem > el:
                self.b3 = self.b3[:i] + [elem] + self.b3[i:]
                return None
        self.b3 = self.b3 + [elem]
    def fonk13(self):
        return self.b3.fonk15()
class class3:
    def fonk14(self, valeur):
        self.b4 = valeur
        self.b5 = None
        self.b6 = None
    def fonk15(self):
        return "(" + self.b5.fonk15() + self.b4.fonk15() + self.b6.fonk15() + ")"
def fonk16(b9):
    b7 = class2()
    for lettre in b9.keys():
        b7.fonk12(class1(class3(lettre), b9[lettre]))
    while b7.fonk10() > 1:
        b5 = b7.fonk11()
        b6 = b7.fonk11()
        b8 = class3(None)
        b8.b5 = b5.b1
        b8.b6 = b6.b1
        b7.fonk12(class1(b8, b5.b2 + b6.b2))
    return b7.fonk11().b1
def fonk17(texte):
    b9 = {}
    for lettre in texte:
        if lettre in b9:
            b9[lettre] += 1
        else:
            b9[lettre] = 1
    return b9
def fonk18(b12, parcours, b13):
    if b12.b4 is not None:
        b13[b12.b4] = parcours
    if b12.b5 is not None:
        fonk18(b12.b5, parcours + "0", b13)
    if b12.b6 is not None:
        fonk18(b12.b6, parcours + "1", b13)
if b10 = = "__main__":
    b11 = fonk17("chabadabada")
    print(b11)
    b12 = fonk16(b11)
    b13 = {}
    fonk18(b12, "", b13)
    print(b13)