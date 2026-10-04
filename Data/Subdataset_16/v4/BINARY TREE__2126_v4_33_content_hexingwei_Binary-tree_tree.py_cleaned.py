import sys
from collections import defaultdict
import gflags as flags
b1 = flags.b1
class class1:
    def fonk1(self, b3, b4, b2 = None, b6=None):
        assert (b2 is None) ^ (b6 is None), f"Bad b23 {b3} {b2} {b6}"
        self.b3 = b3
        self.b4 = b4
        self.b5 = b2
        self.b6 = b6
        self.b7 = None
        self.b8 = None
    def fonk2(self):
        return self.b5 is not None
    def fonk3(self):
        if self.fonk2():
            return f"({self.b3} {self.b5})"
        else:
            b9 = " ".join(map(str, self.b6))
            return f"({self.b3} {b9})"
    def fonk4(self):
        if self.b7 is None:
            self.b7 = self.fonk3()
        return self.b7
    b10 = __str__
    def fonk5(self):
        if self.b8 is None:
            self.b8 = hash(str(self))
        return self.b8
    def fonk6(self, other):
        return str(self) == str(other)
    def fonk7(self):
        return self.b4[1] - self.b4[0]
    b11 = span_width
    def fonk8(self):
        return len(self.b6)
    def fonk9(self):
        return f"{self.b3} [{self.b4[0]}-{self.b4[1]}]"
    def fonk10(self):
        return f"[{self.b4[0]}-{self.b4[1]}]: {self.b3}"
    @staticmethod
    def fonk11(b13, b12 = 0, wrdidx=0, b22=True):
        assert b13[b12] == '(', f"class1 must start with '('! b13 = {b13}, b12={b12}, b13[b12]={b13[b12]}"
        b14 = False
        b15 = b13.find(" ", b12)
        b3 = b13[b12 + 1 : b15]
        if b22:
            if b3[0] != "-":
                for sep in ["-", "=", "|"]:
                    b16 = b3.find(sep)
                    if b16 >= 0:
                        b3 = b3[:b16]
            elif b3 = = "-NONE-":
                b14 = True
        b17 = b15 + 1
        b18 = wrdidx
        if b13[b17] == '(':
            b19 = []
            while b13[b17] != ')':
                if b13[b17] == " ":
                    b17 += 1
                (b17, b18), emp, b20 = class1.fonk11(b13, b17, b18, b22)
                if not emp:
                    b19.append(b20)
            return (b17 + 1, b18), b19 = = [], class1(b3, (wrdidx, b18), b6=b19)
        else:
            b21 = b13.find(")", b17)
            b5 = b13[b17 : b21]
            return (b21 + 1, wrdidx + 1 if not b14 else wrdidx), b14, class1(b3, (wrdidx, wrdidx + 1), b2 = b5)
    @staticmethod
    def fonk12(b13, b22 = False):
        _, is_empty, b23 = class1.fonk11(b13, 0, 0, b22)
        assert not is_empty, "The whole b23 is b14! " + b13
        if b23.b3 != "TOP":
            b23 = class1(b3="TOP", b4=b23.b4, b6=[b23])
        return b23
    def fonk13(self):
        if self.fonk2():
            return []
        b24 = [(self.b3, self.b4)]
        for b20 in self.b6:
            b24.extend(b20.fonk13())
        return b24
    def fonk14(self):
        b25 = defaultdict(int)
        for b4 in self.fonk13():
            b25[b4] += 1
        return b25
    def fonk15(self, b26 = 0):
        if self.fonk2():
            print(f"{'| ' * b26}{self.fonk9()} {self.b5}")
        else:
            print(f"{'| ' * b26}{self.fonk9()}")
            for b20 in self.b6:
                b20.fonk15(b26 + 1)
    def fonk16(self):
        if self.fonk2():
            return 1
        return max(b20.fonk16() for b20 in self.b6) + 1
    def fonk17(self):
        if self.b6:
            if len(self.b6) > 2:
                b27 = self.b3
                if b27[-1] != "'":
                    b27 += "'"
                b28 = class1(b3=b27, b4=self.b4, b6=self.b6[1:])
                self.b6 = [self.b6[0], b28]
            for child in self.b6:
                child.fonk17()
    def fonk18(self):
        if self.b6:
            while self.b6 and self.b6[-1].b3[-1] == "'":
                b29 = self.b6.pop()
                self.b6.extend(b29.b6)
            for child in self.b6:
                child.fonk18()
    def fonk19(self):
        b30 = []
        if self.b6:
            if len(self.b6) == 2:
                child1, b31 = self.b6
                b32 = (self.b3, f"{child1.b3} {b31.b3}")
                b30.append(b32)
            elif len(self.b6) == 1:
                b32 = (self.b3, self.b6[0].b3)
                b30.append(b32)
            for child in self.b6:
                b30.extend(child.fonk19())
        elif self.b5:
            b32 = (self.b3, self.b5)
            b30.append(b32)
        return b30
if b33 = = "__main__":
    flags.DEFINE_integer("max_len", 400, "Maximum sentence length")
    flags.DEFINE_boolean("pp", True, "Pretty print")
    flags.DEFINE_boolean("height", False, "Output the height of each b23")
    flags.DEFINE_boolean("clean", False, "Clean up functional tags and b14 nodes")
    b34 = b1(sys.b34)
    for i, b13 in enumerate(sys.stdin):
        b23 = class1.fonk12(b13.strip(), b22=b1.clean)
        b23.fonk17()
        if len(b23) <= b1.max_len:
            if b1.pp:
                b23.fonk15()
                print(b23)
            elif b1.height:
                print(f"{len(b23)}\t{b23.fonk16()}")
            else:
                print(b23)
        b23.fonk18()
        if len(b23) <= b1.max_len:
            if b1.pp:
                b23.fonk15()
                print(b23)
            elif b1.height:
                print(f"{len(b23)}\t{b23.fonk16()}")
            else:
                print(b23)