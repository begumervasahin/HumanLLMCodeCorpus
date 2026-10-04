class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
    def fonk2(self, other):
        return self.b2 < other.b2
    def fonk3(self, other):
        return self.b2 > other.b2
    def fonk4(self, other):
        return self.b2 = = other.b2 and self.b1 == other.b1
    def fonk5(self, other):
        return self.b2 <= other.b2
    def fonk6(self, other):
        return self.b2 >= other.b2
    def fonk7(self):
        return f"({self.b1}, {self.b2})"
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
                return
        self.b3.append(elem)
    def fonk13(self):
        return str(self.b3)
class class3:
    def fonk14(self, valeur):
        self.b4 = valeur
        self.b5 = None
        self.b6 = None
    def fonk15(self):
        return f"({self.b5}, {self.b4}, {self.b6})"
def fonk16(b9):
    b7 = class2()
    for lettre, b12 in b9.items():
        b7.fonk12(class1(class3(lettre), b12))
    while b7.fonk10() > 1:
        b5 = b7.fonk11()
        b6 = b7.fonk11()
        b8 = class3(None)
        b8.b5 = b5.b1
        b8.b6 = b6.b1
        b7.fonk12(class1(b8, b5.b2 + b6.b2))
    return b7.fonk11().b1
def fonk17(b11):
    b9 = {}
    for lettre in b11:
        if lettre in b9:
            b9[lettre] += 1
        else:
            b9[lettre] = 1
    return b9
def fonk18(b13, parcours, b14):
    if b13.b4 is not None:
        b14[b13.b4] = parcours
        return
    if b13.b5 is not None:
        fonk18(b13.b5, parcours + "0", b14)
    if b13.b6 is not None:
        fonk18(b13.b6, parcours + "1", b14)
if b10 = = "__main__":
    b11 = "chabadabada"
    b12 = fonk17(b11)
    print("Densité:", b12)
    b13 = fonk16(b12)
    print("class3:", b13)
    b14 = {}
    fonk18(b13, "", b14)
    print("Dictionnaire des codes:", b14)