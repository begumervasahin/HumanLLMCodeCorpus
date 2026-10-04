import sys
import argparse
from collections import defaultdict
class class1:
    def fonk1(self, b2, b3, b1 = None, b4=None):
        assert (b1 is None) ^ (b4 is None), \
               "Invalid b18 initialization with b2: {}, b1: {}, b4: {}".format(b2, b1, b4)
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
        return "{} [{}-{}]".format(self.b2, self.b3[0], self.b3[1])
    def fonk10(self):
        return "[{}-{}]: {}".format(self.b3[0], self.b3[1], self.b2)
    @staticmethod
    def fonk11(line, b9 = 0, wrdidx=0, b17=True):
        assert line[b9] == '(', f"class1 must start with '(': {line} at position {b9}"
        b10 = False
        b11 = line.find(" ", b9)
        b2 = line[b9 + 1: b11]
        if b17:
            if b2[0] != "-":
                for delimiter in "-=|":
                    b2 = b2.split(delimiter)[0]
            elif b2 = = "-NONE-":
                b10 = True
        b12 = b11 + 1
        b13 = wrdidx
        if line[b12] == '(':
            b14 = []
            while line[b12] != ')':
                if line[b12] == " ":
                    b12 += 1
                (b12, b13), emp, b15 = class1.fonk11(line, b12, b13, b17)
                if not emp:
                    b14.append(b15)
            return (b12 + 1, b13), b14 = = [], class1(b2, (wrdidx, b13), b4=b14)
        else:
            b16 = line.find(")", b12)
            b1 = line[b12: b16]
            return (b16 + 1, wrdidx + 1 if not b10 else wrdidx), b10, class1(b2, (wrdidx, wrdidx + 1), b1 = b1)
    @staticmethod
    def fonk12(line, b17 = False):
        _, is_empty, b18 = class1.fonk11(line, 0, 0, b17)
        assert not is_empty, "The entire b18 is b10! " + line
        if b18.b2 != "TOP":
            b18 = class1(b2="TOP", b3=b18.b3, b4=[b18])
        return b18
    def fonk13(self):
        if self.fonk2():
            return []
        b19 = [(self.b2, self.b3)]
        for b15 in self.b4:
            b19.extend(b15.fonk13())
        return b19
    def fonk14(self):
        b20 = defaultdict(int)
        for label_span in self.fonk13():
            b20[label_span] += 1
        return b20
    def fonk15(self, b21 = 0):
        if not self.fonk2():
            print("{}{}".format("| " * b21, self.fonk9()))
            for b15 in self.b4:
                b15.fonk15(b21 + 1)
        else:
            print("{}{} {}".format("| " * b21, self.fonk9(), self.b1))
    def fonk16(self):
        if self.fonk2():
            return 1
        return max(b15.fonk16() for b15 in self.b4) + 1
    def fonk17(self):
        if self.b4:
            if len(self.b4) > 2:
                b22 = self.b2 + "'" if self.b2[-1] != "'" else self.b2
                self.b4 = [self.b4[0], class1(b2=b22, b3=self.b3, b4=self.b4[1:])]
            for b15 in self.b4:
                b15.fonk17()
    def fonk18(self):
        if self.b4:
            while self.b4[-1].b2.endswith("'"):
                b23 = self.b4.pop()
                self.b4.extend(b23.b4)
            for b15 in self.b4:
                b15.fonk18()
    def fonk19(self):
        b24 = []
        if self.b4:
            if len(self.b4) == 2:
                b25 = (self.b2, "{} {}".format(self.b4[0].b2, self.b4[1].b2))
                b24.append(b25)
            elif len(self.b4) == 1:
                b25 = (self.b2, self.b4[0].b2)
                b24.append(b25)
            for b15 in self.b4:
                b24.extend(b15.fonk19())
        elif self.b1:
            b24.append((self.b2, self.b1))
        return b24
if b26 = = "__main__":
    b27 = argparse.ArgumentParser(description='Process some trees.')
    b27.add_argument('--max_len', b28 = int, default=400, help='Maximum sentence length')
    b27.add_argument('--pp', b29 = 'store_true', help='Pretty print the b18')
    b27.add_argument('--height', b29 = 'store_true', help='Output the height of each b18')
    b27.add_argument('--clean', b29 = 'store_true', help='Clean up functional tags and b10 nodes')
    b30 = b27.parse_args()
    for i, line in enumerate(sys.stdin):
        b18 = class1.fonk12(line.strip(), b17=b30.clean)
        b18.fonk17()
        if len(b18) <= b30.max_len:
            if b30.pp:
                b18.fonk15()
                print(b18)
            elif b30.height:
                print("{}\t{}".format(len(b18), b18.fonk16()))
            else:
                print(b18)
        b18.fonk18()
        if len(b18) <= b30.max_len:
            if b30.pp:
                b18.fonk15()
                print(b18)
            elif b30.height:
                print("{}\t{}".format(len(b18), b18.fonk16()))
            else:
                print(b18)