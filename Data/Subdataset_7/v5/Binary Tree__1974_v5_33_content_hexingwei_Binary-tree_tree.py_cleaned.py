import sys
from collections import defaultdict
class class1:
    def fonk1(self, b2, b3, b1 = None, b4=None):
        assert (b1 is None) ^ (b4 is None), "Invalid b17 structure"
        self.b2 = b2
        self.b3 = b3
        self.b1 = b1
        self.b4 = b4
        self.b5 = None
        self.b6 = None
    def fonk2(self):
        return self.b1 is not None
    def fonk3(self):
        if True or self.b5 is None:
            self.b5 = self.fonk5()
        return self.b5
    def fonk4(self):
        return self.fonk3()
    def fonk5(self):
        if self.fonk2():
            return f"({self.b2} {self.b1})"
        else:
            return f"({self.b2} {' '.join(map(str, self.b4))})"
    def fonk6(self):
        if self.b6 is None:
            self.b6 = hash(str(self))
        return self.b6
    def fonk7(self, other):
        return str(self) == str(other)
    def fonk8(self):
        return self.b3[1] - self.b3[0]
    def fonk9(self):
        return len(self.b4)
    def fonk10(self):
        return f"{self.b2} [{self.b3[0]}-{self.b3[1]}]"
    def fonk11(self):
        return f"[{self.b3[0]}-{self.b3[1]}]: {self.b2}"
    @staticmethod
    def fonk12(line, b7 = 0, word_index=0, b16=True):
        assert line[b7] == '(', "class1 must start with a '('"
        b8 = False
        b9 = line.find(" ", b7)
        b2 = line[b7 + 1: b9]
        if b16:
            if b2[0] != "-":
                b10 = b2.find("-")
                if b10 >= 0:
                    b2 = b2[:b10]
                b10 = b2.find("=")
                if b10 >= 0:
                    b2 = b2[:b10]
                b10 = b2.find("|")
                if b10 >= 0:
                    b2 = b2[:b10]
            else:
                if b2 = = "-NONE-":
                    b8 = True
        b11 = b9 + 1
        b12 = word_index
        if line[b11] == '(':
            b13 = []
            while line[b11] != ')':
                if line[b11] == " ":
                    b11 += 1
                (b11, b12), emp, b14 = class1.fonk12(line, b11, b12, b16)
                if not emp:
                    b13.append(b14)
            return (b11 + 1, b12), b13 = = [], class1(b2, (word_index, b12), b4=b13)
        else:
            b15 = line.find(")", b11)
            b1 = line[b11: b15]
            return (b15 + 1, word_index + 1 if not b8 else word_index), b8, class1(b2, (word_index, word_index + 1), b1 = b1)
    @staticmethod
    def fonk13(line, b16 = False):
        _, is_empty, b17 = class1.fonk12(line, 0, 0, b16)
        assert not is_empty, "The whole b17 is b8! " + line
        if b17.b2 != "TOP":
            b17 = class1(b2="TOP", b3=b17.b3, b4=[b17])
        return b17
