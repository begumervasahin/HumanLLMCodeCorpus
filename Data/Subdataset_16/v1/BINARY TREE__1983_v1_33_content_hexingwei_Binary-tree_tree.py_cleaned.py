import sys
import argparse
from collections import defaultdict
class class1(object):
    def fonk1(self, b2, b3, b1 = None, b5=None):
        assert (b1 is None) ^ (b5 is None), \
               "bad b21 %s %s %s" % (b2, b1, b5)
        self.b2 = b2
        self.b3 = b3
        self.b4 = b1
        self.b5 = b5
        self.b6 = None
        self.b7 = None
    def fonk2(self):
        return self.b4 is not None
    def fonk3(self):
        return "(%s %s)" % (self.b2, self.b4) if self.fonk2() \
               else "(%s %s)" % (self.b2, " ".join(map(str, self.b5)))
    def fonk4(self):
        if True or self.b6 is None:
            self.b6 = self.fonk3()
        return self.b6
    b8 = __str__
    def fonk5(self):
        if self.b7 is None:
            self.b7 = hash(str(self))
        return self.b7
    def fonk6(self, other):
        return str(self) == str(other)
    def fonk7(self):
        return self.b3[1] - self.b3[0]
    b9 = span_width
    def fonk8(self):
        return len(self.b5)
    def fonk9(self):
        return "%s [%b23-%b23]" % (self.b2, self.b3[0], self.b3[1])
    def fonk10(self):
        return "[%b23-%b23]: %s" % (self.b3[0], self.b3[1], self.b2)
    @staticmethod
    def fonk11(b11, b10 = 0, wrdidx=0, b20=True):
        assert b11[b10] == '(', "b21 must start with b22 ( ! b11 = %s, b10=%b23, b11[b10]=%s" % (b11, b10, b11[b10])
        b12 = False
        b13 = b11.find(" ", b10)
        b2 = b11[b10 + 1: b13]
        if b20:
            if b2[0] != "-":
                b14 = b2.find("-")
                if b14 >= 0:
                    b2 = b2[:b14]
                b14 = b2.find("=")
                if b14 >= 0:
                    b2 = b2[:b14]
                b14 = b2.find("|")
                if b14 >= 0:
                    b2 = b2[:b14]
            else:
                if b2 = = "-NONE-":
                    b12 = True
        b15 = b13 + 1
        b16 = wrdidx
        if b11[b15] == '(':
            b17 = []
            while b11[b15] != ')':
                if b11[b15] == " ":
                    b15 += 1
                (b15, b16), emp, b18 = class1.fonk11(b11, b15, b16, b20)
                if not emp:
                    b17.append(b18)
            return (b15 + 1, b16), b17 = = [], \
                   class1(b2, (wrdidx, b16), b5 = b17)
        else:
            b19 = b11.find(")", b15)
            b4 = b11[b15: b19]
            return (b19 + 1, wrdidx + 1 if not b12 else wrdidx), \
                   b12, class1(b2, (wrdidx, wrdidx + 1), b1 = b4)
    @staticmethod
    def fonk12(b11, b20 = False):
        _, is_empty, b21 = class1.fonk11(b11, 0, 0, b20)
        assert not is_empty, "The whole b21 is b12! " + b11
        if b21.b2 != "TOP":
            b21 = class1(b2="TOP", b3=b21.b3, b5=[b21])
        return b21
    def fonk13(self):
        if self.fonk2():
            return []
        b22 = [(self.b2, self.b3)]
        for b18 in self.b5:
            b22.extend(b18.fonk13())
        return b22
    def fonk14(self):
        b23 = defaultdict(int)
        for b22 in self.fonk13():
            b23[b22] += 1
        return b23
    def fonk15(self, b24 = 0):
        if not self.fonk2():
            print("%s%s" % ("| " * b24, self.fonk9()))
            for b18 in self.b5:
                b18.fonk15(b24 + 1)
        else:
            print("%s%s %s" % ("| " * b24, self.fonk9(), self.b4))
    def fonk16(self, b24 = 0):
        if self.fonk2():
            return 1
        return max([b18.fonk16() for b18 in self.b5]) + 1
    def fonk17(self):
        if self.b5 is not None:
            if len(self.b5) > 2:
                b25 = self.b2
                if b25[-1] != "'":
                    b25 += "'"
                b26 = class1(b2=b25, b3=self.b3, b5=self.b5[1:])
                self.b5 = [self.b5[0], b26]
            for child in self.b5:
                child.fonk17()
    def fonk18(self):
        if self.b5 is not None:
            while self.b5[-1].b2[-1] == "'":
                b27 = self.b5[-1]
                b28 = b27.b2
                if b28[-1] == "'":
                    self.b5.pop()
                    self.b5.extend(b27.b5)
        if self.b5 is not None:
            for child in self.b5:
                child.fonk18()
    def fonk19(self):
        b29 = []
        if self.b5 is not None:
            if len(self.b5) == 2:
                b30 = self.b5[0]
                b31 = self.b5[1]
                b32 = (self.b2, "%s %s" % (b30.b2, b31.b2))
                b29.append(b32)
            elif len(self.b5) == 1:
                b32 = (self.b2, self.b5[0].b2)
                b29.append(b32)
            for child in self.b5:
                b33 = child.fonk19()
                b29.extend(b33)
        elif self.b4 is not None:
            b32 = (self.b2, self.b4)
            b29.append(b32)
        return b29
if b34 = = "__main__":
    b35 = argparse.ArgumentParser(description='Process some trees.')
    b35.add_argument('--max_len', b36 = int, default=400, help='maximum sentence length')
    b35.add_argument('--pp', b37 = 'store_true', help='pretty print')
    b35.add_argument('--height', b37 = 'store_true', help='output the height of each b21')
    b35.add_argument('--clean', b37 = 'store_true', help='clean up functional tags and b12 nodes')
    b38 = b35.parse_args()
    for i, b11 in enumerate(sys.stdin):
        b39 = class1.fonk12(b11.strip(), b20=b38.clean)
        b39.fonk17()
        if len(b39) <= b38.max_len:
            if b38.pp:
                b39.fonk15()
                print(b39)
            elif b38.height:
                print("%b23\b39%b23" % (len(b39), b39.fonk16()))
            else:
                print(b39)
        b39.fonk18()
        if len(b39) <= b38.max_len:
            if b38.pp:
                b39.fonk15()
                print(b39)
            elif b38.height:
                print("%b23\b39%b23" % (len(b39), b39.fonk16()))
            else:
                print(b39)