import sys
from collections import defaultdict
class class1:
    def fonk1(self, b2, b3, b1 = None, b5=None):
        assert (b1 is None) ^ (b5 is None), \
               "Invalid b18 structure"
        self.b2 = b2
        self.b3 = b3
        self.b4 = b1
        self.b5 = b5
        self.b6 = None
        self.b7 = None
    def fonk2(self):
        return self.b4 is not None
    def fonk3(self):
        if True or self.b6 is None:
            self.b6 = self.fonk5()
        return self.b6
    def fonk4(self):
        return self.fonk3()
    def fonk5(self):
        if self.fonk2():
            return f"({self.b2} {self.b4})"
        else:
            return f"({self.b2} {' '.join(map(str, self.b5))})"
    def fonk6(self):
        if self.b7 is None:
            self.b7 = hash(str(self))
        return self.b7
    def fonk7(self, other):
        return str(self) == str(other)
    def fonk8(self):
        return self.b3[1] - self.b3[0]
    def fonk9(self):
        return len(self.b5)
    def fonk10(self):
        return f"{self.b2} [{self.b3[0]}-{self.b3[1]}]"
    def fonk11(self):
        return f"[{self.b3[0]}-{self.b3[1]}]: {self.b2}"
    @staticmethod
    def fonk12(line, b8 = 0, wrdidx=0, b17=True):
        assert line[b8] == '(', "class1 must start with b19 '('"
        b9 = False
        b10 = line.find(" ", b8)
        b2 = line[b8 + 1 : b10]
        if b17:
            if b2[0] != "-":
                b11 = b2.find("-")
                if b11 >= 0:
                    b2 = b2[:b11]
                b11 = b2.find("=")
                if b11 >= 0:
                    b2 = b2[:b11]
                b11 = b2.find("|")
                if b11 >= 0:
                    b2 = b2[:b11]
            else:
                if b2 = = "-NONE-":
                    b9 = True
        b12 = b10 + 1
        b13 = wrdidx
        if line[b12] == '(':
            b14 = []
            while line[b12] != ')':
                if line[b12] == " ":
                    b12 += 1
                (b12, b13), emp, b15 = class1.fonk12(line, b12, b13, b17)
                if not emp:
                    b14.append(b15)
            return (b12 + 1, b13), b14 = = [], class1(b2, (wrdidx, b13), b5=b14)
        else:
            b16 = line.find(")", b12)
            b4 = line[b12 : b16]
            return (b16 + 1, wrdidx + 1 if not b9 else wrdidx), b9, class1(b2, (wrdidx, wrdidx+1), b1 = b4)
    @staticmethod
    def fonk13(line, b17 = False):
        _, is_empty, b18 = class1.fonk12(line, 0, 0, b17)
        assert not is_empty, "The whole b18 is b9! " + line
        if b18.b2 != "TOP":
            b18 = class1(b2="TOP", b3=b18.b3, b5=[b18])
        return b18
    def fonk14(self):
        if self.fonk2():
            return []
        b19 = [(self.b2, self.b3)]
        for b15 in self.b5:
            b19.extend(b15.fonk14())
        return b19
    def fonk15(self):
        b20 = defaultdict(int)
        for b19 in self.fonk14():
            b20[b19] += 1
        return b20
    def fonk16(self, b21 = 0):
        if not self.fonk2():
            print("| " * b21, self.fonk10())
            for b15 in self.b5:
                b15.fonk16(b21+1)
        else:
            print("| " * b21, self.fonk10(), self.b4)
    def fonk17(self, b21 = 0):
        if self.fonk2():
            return 1
        return max([b15.fonk17() for b15 in self.b5]) + 1
    def fonk18(self):
        if self.b5 is not None:
            if len(self.b5) > 2:
                b22 = self.b2
                if b22[-1] != "'":
                    b22 += "'"
                b23 = class1(b2=b22, b3=self.b3, b5=self.b5[1:])
                self.b5 = [self.b5[0], b23]
            for child in self.b5:
                child.fonk18()
    def fonk19(self):
        if self.b5 is not None:
            while self.b5[-1].b2[-1] == "'":
                b24 = self.b5[-1]
                b25 = b24.b2
                if b25[-1] == "'":
                    self.b5.pop()
                    self.b5.extend(b24.b5)
        if self.b5 is not None:
            for child in self.b5:
                child.fonk19()
    def fonk20(self):
        b26 = []
        if self.b5 is not None:
            if len(self.b5) == 2:
                b27 = self.b5[0]
                b28 = self.b5[1]
                b29 = (self.b2, f"{b27.b2} {b28.b2}")
                b26.append(b29)
            elif len(self.b5) == 1:
                b29 = (self.b2, self.b5[0].b2)
                b26.append(b29)
            for child in self.b5:
                b30 = child.fonk20()
                b26.extend(b30)
        elif self.b4 is not None:
            b29 = (self.b2, self.b4)
            b26.append(b29)
        return b26
if b31 = = "__main__":
    a1 = 400
    b32 = True
    b33 = False
    b34 = False
    for i, line in enumerate(sys.stdin):
        b35 = class1.fonk13(line.strip(), b17=b34)
        b35.fonk18()
        if len(b35) <= a1:
            if b32:
                b35.fonk16()
                print(b35)
            elif b33:
                print(f"{len(b35)}\b35{b35.fonk17()}")
            else:
                print(b35)
        b35.fonk19()
        if len(b35) <= a1:
            if b32:
                b35.fonk16()
                print(b35)
            elif b33:
                print(f"{len(b35)}\b35{b35.fonk17()}")
            else:
                print(b35)