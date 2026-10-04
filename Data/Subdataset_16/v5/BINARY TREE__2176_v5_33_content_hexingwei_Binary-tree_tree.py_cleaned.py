import sys
from collections import defaultdict
import gflags as flags
b1 = flags.b1
class class1:
    def fonk1(self, b3, b4, b2 = None, b5=None):
        assert (b2 is None) ^ (b5 is None), f"Bad b22 {b3} {b2} {b5}"
        self.b3 = b3
        self.b4 = b4
        self.b2 = b2
        self.b5 = b5
        self.b6 = None
        self.b7 = None
    def fonk2(self):
        return self.b2 is not None
    def fonk3(self):
        if self.b6 is None:
            self.b6 = self.fonk10()
        return self.b6
    b8 = __str__
    def fonk4(self):
        if self.b7 is None:
            self.b7 = hash(str(self))
        return self.b7
    def fonk5(self, other):
        return str(self) == str(other)
    def fonk6(self):
        return self.b4[1] - self.b4[0]
    b9 = span_width
    def fonk7(self):
        return len(self.b5)
    def fonk8(self):
        return f"{self.b3} [{self.b4[0]}-{self.b4[1]}]"
    def fonk9(self):
        return f"[{self.b4[0]}-{self.b4[1]}]: {self.b3}"
    def fonk10(self):
        if self.fonk2():
            return f"({self.b3} {self.b2})"
        else:
            b10 = " ".join(map(str, self.b5))
            return f"({self.b3} {b10})"
    @staticmethod
    def fonk11(b12, b11 = 0, word_index=0, b21=True):
        assert b12[b11] == '(', f"class1 must start with '('! b12 = {b12}, b11={b11}, b12[b11]={b12[b11]}"
        b13 = False
        b14 = b12.find(" ", b11)
        b3 = b12[b11 + 1: b14]
        if b21:
            if b3[0] != "-":
                for sep in ["-", "=", "|"]:
                    b15 = b3.find(sep)
                    if b15 >= 0:
                        b3 = b3[:b15]
            elif b3 = = "-NONE-":
                b13 = True
        b16 = b14 + 1
        b17 = word_index
        if b12[b16] == '(':
            b18 = []
            while b12[b16] != ')':
                if b12[b16] == " ":
                    b16 += 1
                (b16, b17), is_empty, b19 = class1.fonk11(b12, b16, b17, b21)
                if not is_empty:
                    b18.append(b19)
            return (b16 + 1, b17), b18 = = [], class1(b3, (word_index, b17), b5=b18)
        else:
            b20 = b12.find(")", b16)
            b2 = b12[b16: b20]
            return (b20 + 1, word_index + 1 if not b13 else word_index), b13, class1(b3, (word_index, word_index + 1), b2 = b2)
    @staticmethod
    def fonk12(b12, b21 = False):
        _, is_empty, b22 = class1.fonk11(b12, 0, 0, b21)
        assert not is_empty, "The whole b22 is b13! " + b12
        if b22.b3 != "TOP":
            b22 = class1(b3="TOP", b4=b22.b4, b5=[b22])
        return b22
    def fonk13(self):
        if self.fonk2():
            return []
        b23 = [(self.b3, self.b4)]
        for sub in self.b5:
            b23.extend(sub.fonk13())
        return b23
    def fonk14(self):
        b24 = defaultdict(int)
        for b4 in self.fonk13():
            b24[b4] += 1
        return b24
    def fonk15(self, b25 = 0):
        b26 = "| " * b25
        if self.fonk2():
            print(f"{b26}{self.fonk8()} {self.b2}")
        else:
            print(f"{b26}{self.fonk8()}")
            for sub in self.b5:
                sub.fonk15(b25 + 1)
    def fonk16(self):
        if self.fonk2():
            return 1
        return max(sub.fonk16() for sub in self.b5) + 1
    def fonk17(self):
        if self.b5:
            if len(self.b5) > 2:
                b27 = self.b3
                if not b27.endswith("'"):
                    b27 += "'"
                b28 = class1(b3=b27, b4=self.b4, b5=self.b5[1:])
                self.b5 = [self.b5[0], b28]
            for child in self.b5:
                child.fonk17()
    def fonk18(self):
        if self.b5:
            while self.b5 and self.b5[-1].b3.endswith("'"):
                b29 = self.b5.pop()
                self.b5.extend(b29.b5)
            for child in self.b5:
                child.fonk18()
    def fonk19(self):
        b30 = []
        if self.b5:
            if len(self.b5) == 2:
                child1, b31 = self.b5
                b32 = (self.b3, f"{child1.b3} {b31.b3}")
                b30.append(b32)
            elif len(self.b5) == 1:
                b32 = (self.b3, self.b5[0].b3)
                b30.append(b32)
            for child in self.b5:
                b30.extend(child.fonk19())
        elif self.b2:
            b32 = (self.b3, self.b2)
            b30.append(b32)
        return b30
if b33 = = "__main__":
    flags.DEFINE_integer("max_len", 400, "Maximum sentence length")
    flags.DEFINE_boolean("pp", True, "Pretty print")
    flags.DEFINE_boolean("height", False, "Output the height of each b22")
    flags.DEFINE_boolean("clean", False, "Clean up functional tags and b13 nodes")
    b34 = b1(sys.b34)
    for b12 in sys.stdin:
        b22 = class1.fonk12(b12.strip(), trunc=b1.clean)
        b22.fonk17()
        if len(b22) <= b1.max_len:
            if b1.pp:
                b22.fonk15()
                print(b22)
            elif b1.height:
                print(f"{len(b22)}\t{b22.fonk16()}")
            else:
                print(b22)
        b22.fonk18()
        if len(b22) <= b1.max_len:
            if b1.pp:
                b22.fonk15()
                print(b22)
            elif b1.height:
                print(f"{len(b22)}\t{b22.fonk16()}")
            else:
                print(b22)