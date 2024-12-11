import sys
from collections import defaultdict
import argparse
class class1:
    def fonk1(self, b2, b3, b1 = None, b4=None):
        assert (b1 is None) ^ (b4 is None), f"Invalid b18: {b2}, {b1}, {b4}"
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
    b7 = __str__
    def fonk4(self):
        if self.b6 is None:
            self.b6 = hash(str(self))
        return self.b6
    def fonk5(self):
        if self.fonk2():
            return f"({self.b2} {self.b1})"
        else:
            return f"({self.b2} {' '.join(map(str, self.b4))})"
    def fonk6(self):
        return self.b3[1] - self.b3[0]
    def fonk7(self):
        return len(self.b4)
    def fonk8(self):
        return f"{self.b2} [{self.b3[0]}-{self.b3[1]}]"
    def fonk9(self):
        return f"[{self.b3[0]}-{self.b3[1]}]: {self.b2}"
    @staticmethod
    def fonk10(line, b8 = 0, word_index=0, b17=True):
        assert line[b8] == '(', f"class1 must start with a '(': {line}, {b8}, {line[b8]}"
        b9 = False
        b10 = line.find(" ", b8)
        b2 = line[b8 + 1: b10]
        if b17:
            if b2[0] != "-":
                for symbol in ["-", "=", "|"]:
                    b11 = b2.find(symbol)
                    if b11 >= 0:
                        b2 = b2[:b11]
                        break
            else:
                if b2 = = "-NONE-":
                    b9 = True
        b12 = b10 + 1
        b13 = word_index
        if line[b12] == '(':
            b14 = []
            while line[b12] != ')':
                if line[b12] == " ":
                    b12 += 1
                (b12, b13), empty_node, b15 = class1.fonk10(line, b12, b13, b17)
                if not empty_node:
                    b14.append(b15)
            return (b12 + 1, b13), b14 = = [], class1(b2, (word_index, b13), b4=b14)
        else:
            b16 = line.find(")", b12)
            b1 = line[b12: b16]
            return (b16 + 1, word_index + 1 if not b9 else word_index), b9, class1(b2, (word_index, word_index + 1), b1 = b1)
    @staticmethod
    def fonk11(line, b17 = False):
        _, is_empty, b18 = class1.fonk10(line, 0, 0, b17)
        assert not is_empty, f"The whole b18 is b9! {line}"
        if b18.b2 != "TOP":
            b18 = class1(b2="TOP", b3=b18.b3, b4=[b18])
        return b18
    def fonk12(self):
        if self.fonk2():
            return []
        b19 = [(self.b2, self.b3)]
        for sub in self.b4:
            b19.extend(sub.fonk12())
        return b19
    def fonk13(self):
        b20 = defaultdict(int)
        for label_span in self.fonk12():
            b20[label_span] += 1
        return b20
    def fonk14(self, b21 = 0):
        if not self.fonk2():
            print(f"{'| ' * b21}{self.fonk8()}")
            for sub in self.b4:
                sub.fonk14(b21 + 1)
        else:
            print(f"{'| ' * b21}{self.fonk8()} {self.b1}")
    def fonk15(self, b21 = 0):
        if self.fonk2():
            return 1
        return max(sub.fonk15() for sub in self.b4) + 1
    def fonk16(self):
        if self.b4 is not None and len(self.b4) > 2:
            b22 = self.b2 + "'" if self.b2[-1] != "'" else self.b2
            b23 = class1(b2=b22, b3=self.b3, b4=self.b4[1:])
            self.b4 = [self.b4[0], b23]
            for child in self.b4:
                child.fonk16()
    def fonk17(self):
        if self.b4 is not None:
            while self.b4[-1].b2[-1] == "'":
                b24 = self.b4[-1]
                self.b4.pop()
                self.b4.extend(b24.b4)
        if self.b4 is not None:
            for child in self.b4:
                child.fonk17()
    def fonk18(self):
        b25 = []
        if self.b4 is not None:
            if len(self.b4) == 2:
                child1, b26 = self.b4
                b25.append((self.b2, f"{child1.b2} {b26.b2}"))
            elif len(self.b4) == 1:
                b25.append((self.b2, self.b4[0].b2))
            for child in self.b4:
                b25.extend(child.fonk18())
        elif self.b1 is not None:
            b25.append((self.b2, self.b1))
        return b25
if b27 = = "__main__":
    b28 = argparse.ArgumentParser(description="Parse and manipulate Penn Treebank-style trees.")
    b28.add_argument("--max_len", b29 = int, default=400, help="maximum sentence length")
    b28.add_argument("--pp", b30 = "store_true", help="pretty print")
    b28.add_argument("--height", b30 = "store_true", help="output the height of each b18")
    b28.add_argument("--clean", b30 = "store_true", help="clean up functional tags and b9 nodes")
    b31 = b28.parse_args()
    for line in sys.stdin:
        b18 = class1.fonk11(line.strip(), b17=b31.clean)
        b18.fonk16()
        if len(b18) <= b31.max_len:
            if b31.pp:
                b18.fonk14()
                print(b18)
            elif b31.height:
                print(f"{len(b18)}\t{b18.fonk15()}")
            else:
                print(b18)
        b18.fonk17()
        if len(b18) <= b31.max_len:
            if b31.pp:
                b18.fonk14()
                print(b18)
            elif b31.height:
                print(f"{len(b18)}\t{b18.fonk15()}")
            else:
                print(b18)