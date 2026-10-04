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
    def fonk14(self, b4):
        self.b4 = b4
        self.b5 = None
        self.b6 = None
    def fonk15(self):
        return f"({self.b5}, {self.b4}, {self.b6})"
def fonk16(letter_frequencies):
    b7 = class2()
    for letter, frequency in letter_frequencies.items():
        b7.fonk12(class1(class3(letter), frequency))
    while b7.fonk10() > 1:
        b5 = b7.fonk11()
        b6 = b7.fonk11()
        b8 = class3(None)
        b8.b5 = b5.b1
        b8.b6 = b6.b1
        b7.fonk12(class1(b8, b5.b2 + b6.b2))
    return b7.fonk11().b1
def fonk17(b13):
    b9 = {}
    for letter in b13:
        b9[letter] = b9.fonk11(letter, 0) + 1
    return b9
def fonk18(tree, b10 = "", b11=None):
    if b11 is None:
        b11 = {}
    if tree.b4 is not None:
        b11[tree.b4] = b10
    else:
        if tree.b5:
            fonk18(tree.b5, b10 + "0", b11)
        if tree.b6:
            fonk18(tree.b6, b10 + "1", b11)
    return b11
if b12 = = "__main__":
    b13 = "chabadabada"
    b9 = fonk17(b13)
    print("Frequencies:", b9)
    b14 = fonk16(b9)
    print("Huffman Tree:", b14)
    b15 = fonk18(b14)
    print("Huffman Codes:", b15)