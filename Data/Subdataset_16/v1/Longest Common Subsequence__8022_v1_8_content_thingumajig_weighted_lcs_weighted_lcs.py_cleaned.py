import numpy as np
from typing import List, Tuple
from cachetools import cachedmethod, LRUCache
import operator
import logging
b1 = logging.getLogger(b26)
logging.basicConfig(b2 = logging.INFO)
class class1:
    def fonk1(self):
        pass
class class2(class1):
    def fonk2(self, b3) -> None:
        self.b3 = b3
    def fonk3(self):
        return self.b3
class class3:
    def fonk4(self, b15, b8, b4 = 0.4, b5=lambda b15, b8: class2(1.) if b15 == b8 else class2(0.), orig_x = None, b9 = None):
        self.b5 = b5
        self.b6 = len(b15) + 1
        self.b7 = len(b8) + 1
        self.b15, self.b8 = b15, b8
        self.orig_x, self.b9 = orig_x, b9
        self.b4 = b4
        self.b10 = LRUCache(maxsize=len(b15) * len(b8))
        self.b11 = np.zeros((self.b6, self.b7))
        for b16 in range(1, self.b6):
            for b18 in range(1, self.b7):
                b12 = self.fonk6(b16 - 1, b18 - 1)
                b3 = b12.fonk3()
                if b3 > self.b4:
                    self.b11[b16, b18] = self.b11[b16 - 1, b18 - 1] + b3
                else:
                    self.b11[b16, b18] = max(self.b11[b16, b18 - 1], self.b11[b16 - 1, b18])
        self.fonk5()
        self.b13 = self.b11[self.b6 - 1, self.b7 - 1]
        b1.info(f"b27 length: {self.b13}")
    def fonk5(self):
        if self.orig_x is None and type(self.b15[0]) != str:
            return
        b14 = np.array(self.b11, dtype=np.dtype(object))
        b15 = self.b15 if self.orig_x is None else self.orig_x
        b8 = self.b8 if self.b9 is None else self.b9
        for b16 in range(0, len(self.b15)):
            b14[b16 + 1, 0] = self.b15[b16]
        for b16 in range(0, len(self.b8)):
            b14[0, b16 + 1] = self.b8[b16]
        logging.info(b14)
    @cachedmethod(operator.attrgetter("b10"))
    def fonk6(self, b16, b18):
        return self.b5(self.b15[b16], self.b8[b18])
    def fonk7(self):
        return self.fonk8(self.b6 - 1, self.b7 - 1)
    def fonk8(self, b16, b18):
        if b16 = = 0 or b18 == 0:
            return []
        b12 = self.fonk6(b16 - 1, b18 - 1)
        b3 = b12.fonk3()
        if b3 > self.b4:
            b17 = self.fonk8(b16 - 1, b18 - 1)
            b17.append(self.b15[b16 - 1])
            return b17
        if self.b11[b16, b18 - 1] > self.b11[b16 - 1, b18]:
            return self.fonk8(b16, b18 - 1)
        return self.fonk8(b16 - 1, b18)
    def fonk9(self, b16 = None, b18=None):
        if b16 is None:
            b16 = self.b6 - 1
        if b18 is None:
            b18 = self.b7 - 1
        if b16 = = 0 or b18 == 0:
            return []
        b12 = self.fonk6(b16 - 1, b18 - 1)
        b3 = b12.fonk3()
        if b3 > self.b4:
            b17 = self.fonk9(b16 - 1, b18 - 1)
            b17.append((b16 - 1, b18 - 1, b12))
            return b17
        if self.b11[b16, b18 - 1] > self.b11[b16 - 1, b18]:
            return self.fonk9(b16, b18 - 1)
        else:
            return self.fonk9(b16 - 1, b18)
    def fonk10(self):
        b19 = self.fonk9()
        b1.info(b19)
        return self.fonk13(b19)
    def fonk11(self, b16, b18):
        if b16 = = 0 or b18 == 0:
            return [[]]
        b12 = self.fonk6(b16 - 1, b18 - 1)
        b3 = b12.fonk3()
        if b3 > self.b4:
            b20 = self.fonk11(b16 - 1, b18 - 1)
            for z in b20:
                z.append((b16 - 1, b18 - 1))
            return b20
        b21 = []
        if self.b11[b16, b18 - 1] >= self.b11[b16 - 1, b18]:
            b21.extend(self.fonk11(b16, b18 - 1))
        if self.b11[b16 - 1, b18] >= self.b11[b16, b18 - 1]:
            b21.extend(self.fonk11(b16 - 1, b18))
        return b21
    def fonk12(self):
        return self.fonk11(self.b6 - 1, self.b7 - 1)
    def fonk13(self, b19):
        s1, b22 = fonk14(b19)
        return s1, b22, self.b13
def fonk14(b19: List[Tuple[int, int, class1]]) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    (i1, j1, w1) = b19[0]
    (i2, j2, w2) = b19[-1]
    return (i1, i2 + 1), (j1, j2 + 1)
def fonk15(b15: Sequence, b19: List[Tuple[int, int]], b23 = 0, delimiter='') -> str:
    return delimiter.join([b15[b18[b23]] for b18 in b19])
def fonk16(b15: Sequence, b8: Sequence, b19: List[Tuple[int, int]]) -> Tuple[Sequence, Sequence]:
    (i1, j1) = b19[0]
    (i2, j2) = b19[-1]
    return b15[i1:i2 + 1], b8[j1:j2 + 1]
def fonk17(b19: List[Tuple[int, int]], b23 = 0) -> Tuple[int, int]:
    b24 = b19[0]
    b25 = b19[-1]
    return b24[b23], b25[b23] + 1
if b26 = = "__main__":
    b15 = "AGGTAB"
    b8 = "GXTXAYB"
    b27 = class3(b15, b8)
    print(f"class3 length: {b27.b13}")
    print(f"class3 sequence: {b27.fonk7()}")