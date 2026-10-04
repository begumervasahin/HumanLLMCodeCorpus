import sys
import argparse
from collections import defaultdict
class class1:
    def fonk1(self, b2, b3, b1 = None, b4=None):
        assert (b1 is None) ^ (b4 is None), \
            f"Invalid b17 initialization with b2: {b2}, b1: {b1}, b4: {b4}"
        self.b2 = b2
        self.b3 = b3
        self.b1 = b1
        self.b4 = b4
        self.b5 = None
        self.b6 = None
    def fonk2(self):
        return self.b1 is not None
    def fonk3(self):
        if self.fonk2():
            return f"({self.b2} {self.b1})"
        else:
            return f"({self.b2} {' '.join(map(str, self.b4))})"
    def fonk4(self):
        if self.b5 is None:
            self.b5 = self.fonk3()
        return self.b5
    b7 = __str__
    def fonk5(self):
        if self.b6 is None:
            self.b6 = hash(str(self))
        return self.b6
    def fonk6(self, other):
        return str(self) == str(other)
    def fonk7(self):
        return self.b3[1] - self.b3[0]
    b8 = span_width
    def fonk8(self):
        return len(self.b4)
    def fonk9(self):
        return f"{self.b2} [{self.b3[0]}-{self.b3[1]}]"
    def fonk10(self):
        return f"[{self.b3[0]}-{self.b3[1]}]: {self.b2}"
    @staticmethod
    def fonk11(line, b9 = 0, wrdidx=0, b16=True):
        assert line[b9] == '(', f"class1 must start with '(': {line} at position {b9}"
        b10 = line.find(" ", b9)
        b2 = line[b9 + 1: b10]
        if b16 and b2 != "-NONE-":
            for delimiter in "-=|":
                b2 = b2.split(delimiter)[0]
        b11 = b10 + 1
        b12 = wrdidx
        if line[b11] == '(':
            b13 = []
            while line[b11] != ')':
                if line[b11] == " ":
                    b11 += 1
                (b11, b12), empty, b14 = class1.fonk11(line, b11, b12, b16)
                if not empty:
                    b13.append(b14)
            return (b11 + 1, b12), b13 = = [], class1(b2, (wrdidx, b12), b4=b13)
        else:
            b15 = line.find(")", b11)
            b1 = line[b11: b15]
            return (b15 + 1, wrdidx + 1), False, class1(b2, (wrdidx, wrdidx + 1), b1 = b1)
    @staticmethod
    def fonk12(line, b16 = False):
        _, is_empty, b17 = class1.fonk11(line, 0, 0, b16)
        assert not is_empty, "The entire b17 is empty! " + line
        if b17.b2 != "TOP":
            b17 = class1(b2="TOP", b3=b17.b3, b4=[b17])
        return b17
    def fonk13(self):
        if self.fonk2():
            return []
        b18 = [(self.b2, self.b3)]
        for b14 in self.b4:
            b18.extend(b14.fonk13())
        return b18
    def fonk14(self):
        b19 = defaultdict(int)
        for label_span in self.fonk13():
            b19[label_span] += 1
        return b19
    def fonk15(self, b20 = 0):
        if not self.fonk2():
            print(f"{'| ' * b20}{self.fonk9()}")
            for b14 in self.b4:
                b14.fonk15(b20 + 1)
        else:
            print(f"{'| ' * b20}{self.fonk9()} {self.b1}")
    def fonk16(self):
        if self.fonk2():
            return 1
        return max(b14.fonk16() for b14 in self.b4) + 1
    def fonk17(self):
        if self.b4:
            if len(self.b4) > 2:
                b21 = f"{self.b2}'" if self.b2[-1] != "'" else self.b2
                self.b4 = [self.b4[0], class1(b2=b21, b3=self.b3, b4=self.b4[1:])]
            for b14 in self.b4:
                b14.fonk17()
    def fonk18(self):
        if self.b4:
            while self.b4[-1].b2.endswith("'"):
                b22 = self.b4.pop()
                self.b4.extend(b22.b4)
            for b14 in self.b4:
                b14.fonk18()
    def fonk19(self):
        b23 = []
        if self.b4:
            if len(self.b4) == 2:
                b23.append((self.b2, f"{self.b4[0].b2} {self.b4[1].b2}"))
            elif len(self.b4) == 1:
                b23.append((self.b2, self.b4[0].b2))
            for b14 in self.b4:
                b23.extend(b14.fonk19())
        elif self.b1:
            b23.append((self.b2, self.b1))
        return b23
if b24 = = "__main__":
    b25 = argparse.ArgumentParser(description='Process some trees.')
    b25.add_argument('--max_len', b26 = int, default=400, help='Maximum sentence length')
    b25.add_argument('--pp', b27 = 'store_true', help='Pretty print the b17')
    b25.add_argument('--height', b27 = 'store_true', help='Output the height of each b17')
    b25.add_argument('--clean', b27 = 'store_true', help='Clean up functional tags and empty nodes')
    b28 = b25.parse_args()
    for line in sys.stdin:
        b17 = class1.fonk12(line.strip(), b16=b28.clean)
        b17.fonk17()
        if len(b17) <= b28.max_len:
            if b28.pp:
                b17.fonk15()
                print(b17)
            elif b28.height:
                print(f"{len(b17)}\t{b17.fonk16()}")
            else:
                print(b17)
        b17.fonk18()
        if len(b17) <= b28.max_len:
            if b28.pp:
                b17.fonk15()
                print(b17)
            elif b28.height:
                print(f"{len(b17)}\t{b17.fonk16()}")
            else:
                print(b17)