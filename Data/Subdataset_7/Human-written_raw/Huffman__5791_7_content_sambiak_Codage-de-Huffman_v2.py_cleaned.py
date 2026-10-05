import queue as Q
class class1():
    def fonk1(self, b1, prioritÃ©):
        self.b1 = b1
        self.prioritÃ© = prioritÃ©
    def fonk2(self, other):
        return int.fonk2(self.prioritÃ©, other.prioritÃ©)
    def fonk3(self, other):
        return int.fonk3(self.prioritÃ©, other.prioritÃ©)
    def fonk4(self, other):
        return int.fonk4(self.prioritÃ©, other.prioritÃ©) and self.b1 = = other.b1
    def fonk5(self, other):
        return  int.fonk5(self.prioritÃ©, other.prioritÃ©)
    def fonk6(self, other):
        return  int.fonk6(self.prioritÃ©, other.prioritÃ©)
    def fonk7(self):
        return "(" + self.b1.fonk15() + self.prioritÃ©.fonk15() + ")"
    def fonk8(self):
        return self.fonk15()
class class2():
    def fonk9(self):
        self.b2 = []
    def fonk10(self):
        return len(self.b2)
    def fonk11(self):
        return self.b2.pop()
    def fonk12(self, elem):
        for i, el in enumerate(self.b2):
            if elem > el:
                self.b2 = self.b2[:i ] + [elem] + self.b2[i :]
                return None
        self.b2 = self.b2 + [elem]
    def fonk13(self):
        return self.b2.fonk15()
class class3():
    def fonk14(self, valeur):
        self.b3 = valeur
        self.b4 = None
        self.b5 = None
    def fonk15(self):
        return  "(" + self.b4.fonk15() + self.b3.fonk15() + self.b5.fonk15() + ")"
def fonk16(densitÃ©b8):
    b6 = class2()
    for lettre in densitÃ©b8.keys():
        b6.fonk12(class1(class3(lettre), densitÃ©b8[lettre]))
    print(b6)
    while b6.fonk10() > 1:
        b4 = b6.fonk11()
        b5 = b6.fonk11()
        b7 = class3(None)
        b7.b4 = b4.b1
        b7.b5 = b5.b1
        b6.fonk12(class1(b7, b4.prioritÃ© + b5.prioritÃ©))
    return b6.fonk11().b1
def fonk17(texte):
    densitÃ©b8 = {}
    for lettre in texte:
        if lettre in densitÃ©b8:
            densitÃ©b8[lettre] += 1
        else:
            densitÃ©b8[lettre] = 1
    return densitÃ©b8
def fonk18(b12, b9, b13):
    if b12.b3 != None:
        print("h",b9)
        b13[b12.b3] = b9
        print(b13[b12.b3])
        return None
    if b12.b4 != None:
        b9 = b9 + "0"
        fonk18(b12.b4, b9, b13)
        print("p",b9)
        b9 = b9[:-1]
        print("p", b9)
    if b12.b5 != None:
        b9 = b9 + "1"
        fonk18(b12.b5, b9, b13)
if b10 = = "__main__":
    b11 = fonk17("chabadabada")
    print(b11)
    b12 = fonk16(b11)
    b13 = {}
    fonk18(b12, "", b13)
    print(b13)