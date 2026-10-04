import numpy as np
from typing import List, Tuple, Sequence
from cachetools import cachedmethod, LRUCache
import operator
import logging
b1 = logging.getLogger(b30)
logging.basicConfig(b2 = logging.INFO)
class class1:
    def fonk1(self):
        pass
class class2(class1):
    def fonk2(self, b3: float) -> None:
        self.b3 = b3
    def fonk3(self):
        return self.b3
class class3:
    def fonk4(self, b31: Sequence, b8: Sequence, b4 = 0.4, b5=lambda b31, b8: class2(1.0) if b31 == b8 else class2(0.0), orig_x: Sequence = None, b9: Sequence = None):
        self.b5 = b5
        self.b6 = len(b31) + 1
        self.b7 = len(b8) + 1
        self.b31, self.b8 = b31, b8
        self.orig_x, self.b9 = orig_x, b9
        self.b4 = b4
        self.b10 = LRUCache(maxsize=len(b31) * len(b8))
        self.b11 = np.zeros((self.b6, self.b7))
        self.fonk5()
        self.b12 = self.b11[self.b6 - 1, self.b7 - 1]
        b1.info(f"class3 length: {self.b12}")
    def fonk5(self):
        for b17 in range(1, self.b6):
            for b19 in range(1, self.b7):
                b13 = self.fonk7(b17 - 1, b19 - 1)
                b3 = b13.fonk3()
                if b3 > self.b4:
                    self.b11[b17, b19] = self.b11[b17 - 1, b19 - 1] + b3
                else:
                    self.b11[b17, b19] = max(self.b11[b17, b19 - 1], self.b11[b17 - 1, b19])
        self.fonk6()
    def fonk6(self):
        if self.orig_x is None and not isinstance(self.b31[0], str):
            return
        b14 = np.array(self.b11, dtype=object)
        b15 = self.b31 if self.orig_x is None else self.orig_x
        b16 = self.b8 if self.b9 is None else self.b9
        for b17 in range(len(self.b31)):
            b14[b17 + 1, 0] = self.b31[b17]
        for b17 in range(len(self.b8)):
            b14[0, b17 + 1] = self.b8[b17]
        b1.info(b14)
    @cachedmethod(operator.attrgetter("b10"))
    def fonk7(self, b17, b19):
        return self.b5(self.b31[b17], self.b8[b19])
    def fonk8(self) -> List:
        return self.fonk9(self.b6 - 1, self.b7 - 1)
    def fonk9(self, b17, b19) -> List:
        if b17 = = 0 or b19 == 0:
            return []
        b13 = self.fonk7(b17 - 1, b19 - 1)
        b3 = b13.fonk3()
        if b3 > self.b4:
            b18 = self.fonk9(b17 - 1, b19 - 1)
            b18.append(self.b31[b17 - 1])
            return b18
        if self.b11[b17, b19 - 1] > self.b11[b17 - 1, b19]:
            return self.fonk9(b17, b19 - 1)
        return self.fonk9(b17 - 1, b19)
    def fonk10(self, b17 = None, b19=None) -> List[Tuple[int, int, class1]]:
        if b17 is None:
            b17 = self.b6 - 1
        if b19 is None:
            b19 = self.b7 - 1
        if b17 = = 0 or b19 == 0:
            return []
        b13 = self.fonk7(b17 - 1, b19 - 1)
        b3 = b13.fonk3()
        if b3 > self.b4:
            b18 = self.fonk10(b17 - 1, b19 - 1)
            b18.append((b17 - 1, b19 - 1, b13))
            return b18
        if self.b11[b17, b19 - 1] > self.b11[b17 - 1, b19]:
            return self.fonk10(b17, b19 - 1)
        return self.fonk10(b17 - 1, b19)
    def fonk11(self) -> Tuple[Tuple[int, int], Tuple[int, int], float]:
        b20 = self.fonk10()
        b1.info(b20)
        return self.fonk14(b20)
    def fonk12(self, b17, b19) -> List[List[Tuple[int, int]]]:
        if b17 = = 0 or b19 == 0:
            return [[]]
        b13 = self.fonk7(b17 - 1, b19 - 1)
        b3 = b13.fonk3()
        if b3 > self.b4:
            b21 = self.fonk12(b17 - 1, b19 - 1)
            for sequence in b21:
                sequence.append((b17 - 1, b19 - 1))
            return b21
        b22 = []
        if self.b11[b17, b19 - 1] >= self.b11[b17 - 1, b19]:
            b22.extend(self.fonk12(b17, b19 - 1))
        if self.b11[b17 - 1, b19] >= self.b11[b17, b19 - 1]:
            b22.extend(self.fonk12(b17 - 1, b19))
        return b22
    def fonk13(self) -> List[List[Tuple[int, int]]]:
        return self.fonk12(self.b6 - 1, self.b7 - 1)
    def fonk14(self, b20: List[Tuple[int, int, class1]]) -> Tuple[Tuple[int, int], Tuple[int, int], float]:
        span_x, b23 = fonk15(b20)
        return span_x, b23, self.b12
def fonk15(b20: List[Tuple[int, int, class1]]) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    start_index_x, start_index_y, b24 = b20[0]
    end_index_x, end_index_y, b24 = b20[-1]
    return (start_index_x, end_index_x + 1), (start_index_y, end_index_y + 1)
def fonk16(b31: Sequence, b20: List[Tuple[int, int]], b25 = 0, delimiter='') -> str:
    return delimiter.join([b31[idx[b25]] for idx in b20])
def fonk17(b31: Sequence, b8: Sequence, b20: List[Tuple[int, int]]) -> Tuple[Sequence, Sequence]:
    start_x, b26 = b20[0]
    end_x, b27 = b20[-1]
    return b31[start_x:end_x + 1], b8[b26:b27 + 1]
def fonk18(b20: List[Tuple[int, int]], b25 = 0) -> Tuple[int, int]:
    b28 = b20[0]
    b29 = b20[-1]
    return b28[b25], b29[b25] + 1
if b30 = = "__main__":
    b31 = "AGGTAB"
    b8 = "GXTXAYB"
    b32 = class3(b31, b8)
    print(f"class3 length: {b32.b12}")
    print(f"class3 sequence: {b32.fonk8()}")