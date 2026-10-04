b1 = []
class class1:
    def fonk1(self, value, b3):
        self.b2 = value
        self.b3 = b3
        self.b4 = ""
    def fonk2(self):
        return "({})".format(self.b2)
    def fonk3(self):
        return self.b3
    def fonk4(self):
        return self.b2
    def fonk5(self, b4):
        self.b4 = b4
    def fonk6(self):
        return self.b4
class class2:
    def fonk7(self, b5, b6):
        self.b5 = b5
        self.b6 = b6
        self.b3 = b5.fonk9() + b6.fonk9()
        self.b4 = ""
    def fonk8(self):
        return "({},{})".format(self.b5, self.b6)
    def fonk9(self):
        return self.b3
    def fonk10(self):
        return self.b5.fonk10() + self.b6.fonk10()
    def fonk11(self, b4):
        self.b4 = b4
    def fonk12(self):
        return self.b4
def fonk13(b13):
    b4 = b13.fonk12()
    b5, b6 = b13.b5, b13.b6
    b5.fonk11(b4 + "1")
    b6.fonk11(b4 + "0")
    if isinstance(b5, class2):
        fonk13(b5)
    else:
        b1.append(b5)
    if isinstance(b6, class2):
        fonk13(b6)
    else:
        b1.append(b6)
def fonk14():
    b7 = []
    b8 = input("Enter b13 (or leave blank to stop): ")
    if "," not in b8:
        print("No valid input, maybe you were trying to set a radix? (This version only works with radix two)")
        b8 = input("Enter b13 (or leave blank to stop): ")
    while b8:
        value, b3 = b8.split(",")
        b3 = float(b3)
        b7.append(class1(value, b3))
        b8 = input("Enter b13 (or leave blank to stop): ")
    if sorted(b7, b9 = lambda x: x.fonk9(), reverse=True) != b7:
        print("Nodes not sorted! Sorting...")
        b7.sort(b9 = lambda x: x.fonk9(), reverse=True)
        print("New b7:")
        for b13 in b7:
            print("  " + str(b13))
    while len(b7) > 1:
        b10 = b7[:-2]
        b11 = class2(b7[-1], b7[-2])
        b12 = False
        for i, obj in enumerate(b10):
            if b11.fonk9() >= obj.fonk9():
                b10.insert(i, b11)
                b12 = True
                break
        if not b12:
            b10.append(b11)
        b7 = b10
    assert(len(b7) == 1)
    b13 = b7[0]
    b13.fonk11("")
    if isinstance(b13, class1):
        b1.append(b13)
    else:
        fonk13(b13)
    b1.sort(b9 = lambda x: x.fonk10())
    print()
    for b13 in b1:
        print("class1 {} has b4 {}".format(b13, b13.fonk12()))
if b14 = = "__main__":
    fonk14()