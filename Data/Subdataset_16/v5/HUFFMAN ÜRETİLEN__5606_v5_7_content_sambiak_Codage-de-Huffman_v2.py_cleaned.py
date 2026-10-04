import queue as Q
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
                self.b3.insert(i, elem)
                return
        self.b3.append(elem)
    def fonk13(self):
        return str(self.b3)
class class3:
    def fonk14(self, b4 = None):
        self.b5 = b4
        self.b6 = None
        self.b7 = None
    def fonk15(self):
        return f"({self.b6}, {self.b5}, {self.b7})"
def fonk16(b10):
    b8 = class2()
    for letter, frequency in b10.items():
        b8.fonk12(class1(class3(letter), frequency))
    while b8.fonk10() > 1:
        b6 = b8.fonk11()
        b7 = b8.fonk11()
        b9 = class3()
        b9.b6 = b6.b1
        b9.b7 = b7.b1
        b8.fonk12(class1(b9, b6.b2 + b7.b2))
    return b8.fonk11().b1
def fonk17(b14):
    b10 = {}
    for letter in b14:
        b10[letter] = b10.fonk11(letter, 0) + 1
    return b10
def fonk18(tree, b11 = "", b12=None):
    if b12 is None:
        b12 = {}
    if tree.b5 is not None:
        b12[tree.b5] = b11
        return b12
    if tree.b6 is not None:
        fonk18(tree.b6, b11 + "0", b12)
    if tree.b7 is not None:
        fonk18(tree.b7, b11 + "1", b12)
    return b12
if b13 = = "__main__":
    b14 = "chabadabada"
    b10 = fonk17(b14)
    print("Frequency Dictionary:", b10)
    b15 = fonk16(b10)
    print("Huffman class3:", b15)
    b12 = fonk18(b15)
    print("Code Dictionary:", b12)