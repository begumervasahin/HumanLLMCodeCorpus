b1 = []
class class1:
    def fonk1(self, value, b3):
        self.b2 = value
        self.b3 = b3
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
    def fonk8(self):
        return "({},{})".format(self.b5, self.b6)
    def fonk9(self):
        return self.b3
    def fonk10(self):
        return self.b5.fonk10()+self.b6.fonk10()
    def fonk11(self, b4):
        self.b4 = b4
    def fonk12(self):
        return self.b4
def fonk13(b12):
    b4 = b12.fonk12()
    b5, b6 = b12.b5, b12.b6
    b5.fonk11(b4+"1")
    b6.fonk11(b4+"0")
    if (type(b5) is class2):
        fonk13(b5)
    else:
        b1.append(b5)
    if (type(b6) is class2):
        fonk13(b6)
    else:
        b1.append(b6)
b7 = []
b8 = input("Enter b12: ")
if "," not in b8:
    print("No first b12, maybe you were trying to set a radix? (This version only works with radix two)")
    b8 = input("Enter b12: ")
while b8:
    value, b3 = b8.split(",")
    b3 = float(b3)
    b7.append(class1(value, b3))
    b8 = input("Enter b12: ")
if sorted(b7, b9 = lambda x: x.fonk9(), reverse=True) != b7:
    print("Nodes not sorted! Sorting...")
    b7.sort(b9 = lambda x: x.fonk9(), reverse=True)
    print("New b7:")
    for b12 in b7:
        print("  "+str(b12))
while len(b7) > 1:
    b10 = b7[:-2]
    b11 = class2(b7[-1], b7[-2])
    for i,obj in enumerate(b10):
        if (b11.fonk9() >= obj.fonk9()):
            b10.insert(i, b11)
            break
    else:
        b10.append(b11)
    b7 = b10
assert(len(b7) == 1)
b12 = b7[0]
b12.fonk11("")
if type(b12) is class1:
    b1.append(b12)
else:
    fonk13(b12)
b1.sort(b9 = lambda x: x.fonk10())
print()
for b12 in b1:
    print("class1 {} has b4 {}".format(b12, b12.fonk12()))