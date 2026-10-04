import numpy as np
from typing import Dict, List, Tuple, Sequence
from cachetools import cachedmethod, LRUCache
import operator
import logging
b1 = logging.getLogger(__name__)
class class1:
    def fonk1(self):
        pass
class class2(class1):
    def fonk2(self, b2) -> None:
        self.b2 = b2
    def fonk3(self):
        return self.b2
class class3:
    def fonk4(self, b14, b7, b3 = 0.4, b4=lambda b14, b7: class2(1.) if b14 == b7 else class2(0.), orig_x = None, b8 = None):
        self.b4 = b4
        self.b5 = len(b14) + 1
        self.b6 = len(b7) + 1
        self.b14, self.b7 = b14, b7
        self.orig_x, self.b8 = orig_x, b8
        self.b3 = b3
        self.b9 = LRUCache(maxsize=len(b14) * len(b7))
        self.b10 = np.zeros((self.b5, self.b6))
        for b15 in range(1, self.b5):
            for b17 in range(1, self.b6):
                b11 = self.fonk6(b15 - 1, b17 - 1)
                b2 = b11.fonk3()
                if b2 > self.b3:
                    self.b10[b15, b17] = self.b10[b15 - 1, b17 - 1] + b2
                else:
                    self.b10[b15, b17] = max(self.b10[b15, b17 - 1], self.b10[b15 - 1, b17])
        self.fonk5()
        self.b12 = self.b10[self.b5 - 1, self.b6 - 1]
        b1.info(f"lcs length: {self.b12}")
    def fonk5(self):
        if self.orig_x is None and type(self.b14[0])!=str:
            return
        b13 = np.array(self.b10, dtype=np.dtype(object))
        b14 = self.b14 if self.orig_x is None else self.orig_x
        b7 = self.b7 if self.b8 is None else self.b8
        for b15 in range(0, len(self.b14)):
            b13[b15+1, 0] = self.b14[b15]
        for b15 in range(0, len(self.b7)):
            b13[0, b15+1] = self.b7[b15]
        logging.info(b13)
    @cachedmethod(operator.attrgetter("b9"))
    def fonk6(self, b15, b17):
        return self.b4(self.b14[b15], self.b7[b17])
    def fonk7(self):
        return self.fonk8(self.b5 - 1, self.b6 - 1)
    def fonk8(self, b15, b17):
        if b15 = = 0 or b17 == 0:
            return []
        b11 = self.fonk6(b15 - 1, b17 - 1)
        b2 = b11.fonk3()
        if b2 > self.b3:
            b16 = self.fonk8(b15 - 1, b17 - 1)
            b16.append(self.b14[b15 - 1])
            return b16
        if self.b10[b15, b17 - 1] > self.b10[b15 - 1, b17]:
            return self.fonk8(b15, b17 - 1)
        return self.fonk8(b15 - 1, b17)
    def fonk9(self, b15 = None, b17=None):
        if b15 is None:
            b15 = self.b5 - 1
        if b17 is None:
            b17 = self.b6 - 1
        if b15 = = 0 or b17 == 0:
            return []
        b11 = self.fonk6(b15 - 1, b17 - 1)
        b2 = b11.fonk3()
        if b2 > self.b3:
            b16 = self.fonk9(b15 - 1, b17 - 1)
            b16.append((b15 - 1, b17 - 1, b11))
            return b16
        if self.b10[b15, b17 - 1] > self.b10[b15 - 1, b17]:
            return self.fonk9(b15, b17 - 1)
        else:
            return self.fonk9(b15 - 1, b17)
    def fonk10(self):
        b18 = self.fonk9()
        b1.info(b18)
        return self.fonk13(b18)
    def fonk11(self, b15, b17):
        if b15 = = 0 or b17 == 0:
            return [[]]
        b11 = self.fonk6(b15 - 1, b17 - 1)
        b2 = b11.fonk3()
        if b2 > self.b3:
            b19 = self.fonk11(b15 - 1, b17 - 1)
            for z in b19:
                z.append((b15 - 1, b17 - 1))
            return b19
        b20 = []
        if self.b10[b15, b17 - 1] >= self.b10[b15 - 1, b17]:
            b20.extend(self.fonk11(b15, b17 - 1))
        if self.b10[b15 - 1, b17] >= self.b10[b15, b17 - 1]:
            b20.extend(self.fonk11(b15 - 1, b17))
        return b20
    def fonk12(self):
        return self.fonk11(self.b5 - 1, self.b6 - 1)
    def fonk13(self, b18):
        s1, b21 = fonk14(b18)
        return s1, b21, self.b12
def fonk14(b18: list):
    (i1, j1, w1) = b18[0]
    (i2, j2, w2) = b18[-1]
    return (i1, i2 + 1), (j1, j2 + 1)
def fonk15(b14, b18, b22 = 0, delimiter=''):
    return delimiter.join([b14[b17[b22]] for b17 in b18])
def fonk16(b14, b7, b18):
    (i1, j1) = b18[0]
    (i2, j2) = b18[-1]
    return b14[i1:i2 + 1], b7[j1:j2 + 1]
def fonk17(b18, b22 = 0):
    b23 = b18[0]
    b24 = b18[-1]
    return b23[b22], b24[b22] + 1