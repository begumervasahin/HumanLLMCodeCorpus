import numpy as np
from typing import b5, Tuple, b4
from cachetools import cachedmethod, LRUCache
import operator
import logging
b1 = logging.getLogger(__name__)
class class1:
    def fonk1(self):
        pass
class class2(class1):
    def fonk2(self, b2: b3) -> None:
        self.b2 = b2
    def fonk3(self) -> b3:
        return self.b2
class class3:
    def fonk4(self,
                 b17: b5,
                 b9: b5,
                 b11: b3 = 0.4,
                 b6: b4 = lambda b17, b9: class2(1.) if b17 == b9 else class2(0.),
                 orig_x: b5 = None,
                 b10: b5 = None) -> None:
        self.b6 = b6
        self.b7 = len(b17) + 1
        self.b8 = len(b9) + 1
        self.b17, self.b9 = b17, b9
        self.orig_x, self.b10 = orig_x, b10
        self.b11 = b11
        self.b12 = LRUCache(maxsize=len(b17) * len(b9))
        self.b13 = np.zeros((self.b7, self.b8))
        for b18 in range(1, self.b7):
            for b21 in range(1, self.b8):
                b14 = self.fonk6(b18 - 1, b21 - 1)
                b2 = b14.fonk3()
                if b2 > self.b11:
                    self.b13[b18, b21] = self.b13[b18 - 1, b21 - 1] + b2
                else:
                    self.b13[b18, b21] = max(self.b13[b18, b21 - 1], self.b13[b18 - 1, b21])
        self.fonk5()
        self.b15 = self.b13[self.b7 - 1, self.b8 - 1]
        b1.info(f"class3 length: {self.b15}")
    def fonk5(self) -> None:
        if self.orig_x is None and type(self.b17[0]) != str:
            return
        b16 = np.array(self.b13, dtype=object)
        b17 = self.b17 if self.orig_x is None else self.orig_x
        b9 = self.b9 if self.b10 is None else self.b10
        for b18 in range(len(self.b17)):
            b16[b18 + 1, 0] = self.b17[b18]
        for b18 in range(len(self.b9)):
            b16[0, b18 + 1] = self.b9[b18]
        logging.info(b16)
    @cachedmethod(operator.attrgetter("b12"))
    def fonk6(self, b18: b20, b21: b20) -> class1:
        return self.b6(self.b17[b18], self.b9[b21])
    def fonk7(self) -> b5:
        return self.fonk8(self.b7 - 1, self.b8 - 1)
    def fonk8(self, b18: b20, b21: b20) -> b5:
        if b18 = = 0 or b21 == 0:
            return []
        b14 = self.fonk6(b18 - 1, b21 - 1)
        b2 = b14.fonk3()
        if b2 > self.b11:
            b19 = self.fonk8(b18 - 1, b21 - 1)
            b19.append(self.b17[b18 - 1])
            return b19
        if self.b13[b18, b21 - 1] > self.b13[b18 - 1, b21]:
            return self.fonk8(b18, b21 - 1)
        return self.fonk8(b18 - 1, b21)
    def fonk9(self, b18: b20 = None, b21: b20 = None) -> b5[Tuple[b20, b20, class1]]:
        if b18 is None:
            b18 = self.b7 - 1
        if b21 is None:
            b21 = self.b8 - 1
        if b18 = = 0 or b21 == 0:
            return []
        b14 = self.fonk6(b18 - 1, b21 - 1)
        b2 = b14.fonk3()
        if b2 > self.b11:
            b19 = self.fonk9(b18 - 1, b21 - 1)
            b19.append((b18 - 1, b21 - 1, b14))
            return b19
        if self.b13[b18, b21 - 1] > self.b13[b18 - 1, b21]:
            return self.fonk9(b18, b21 - 1)
        else:
            return self.fonk9(b18 - 1, b21)
    def fonk10(self) -> Tuple[Tuple[b20, b20], Tuple[b20, b20], b3]:
        b22 = self.fonk9()
        b1.info(b22)
        return self.fonk13(b22)
    def fonk11(self, b18: b20, b21: b20) -> b5[b5[Tuple[b20, b20]]]:
        if b18 = = 0 or b21 == 0:
            return [[]]
        b14 = self.fonk6(b18 - 1, b21 - 1)
        b2 = b14.fonk3()
        if b2 > self.b11:
            b23 = self.fonk11(b18 - 1, b21 - 1)
            for z in b23:
                z.append((b18 - 1, b21 - 1))
            return b23
        b24 = []
        if self.b13[b18, b21 - 1] >= self.b13[b18 - 1, b21]:
            b24.extend(self.fonk11(b18, b21 - 1))
        if self.b13[b18 - 1, b21] >= self.b13[b18, b21 - 1]:
            b24.extend(self.fonk11(b18 - 1, b21))
        return b24
    def fonk12(self) -> b5[b5[Tuple[b20, b20]]]:
        return self.fonk11(self.b7 - 1, self.b8 - 1)
    def fonk13(self, b22: b5[Tuple[b20, b20, class1]]) -> Tuple[Tuple[b20, b20], Tuple[b20, b20], b3]:
        s1, b25 = fonk14(b22)
        return s1, b25, self.b15
def fonk14(b22: b5[Tuple[b20, b20, class1]]) -> Tuple[Tuple[b20, b20], Tuple[b20, b20]]:
    (i1, j1, w1) = b22[0]
    (i2, j2, w2) = b22[-1]
    return (i1, i2 + 1), (j1, j2 + 1)
def fonk15(b17: b5[str], b22: b5[Tuple[b20, b20]], axis: b20 = 0, delimiter: str = '') -> str:
    return delimiter.join([b17[b21[axis]] for b21 in b22])
def fonk16(b17: b5[str], b9: b5[str], b22: b5[Tuple[b20, b20]]) -> Tuple[b5[str], b5[str]]:
    (i1, j1) = b22[0]
    (i2, j2) = b22[-1]
    return b17[i1:i2 + 1], b9[j1:j2 + 1]
def fonk17(b22: b5[Tuple[b20, b20]], axis: b20 = 0) -> Tuple[b20, b20]:
    b26 = b22[0]
    b27 = b22[-1]
    return b26[axis], b27[axis] + 1