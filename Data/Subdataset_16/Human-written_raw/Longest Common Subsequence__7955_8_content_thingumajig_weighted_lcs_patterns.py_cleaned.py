from typing import Any, Tuple, Union, List
from weighted_lcs import LCS, Weightable, SimpleWeight
import numpy as np
import logging
b1 = logging.getLogger(b22)
class b3:
    def fonk1(self, str):
        pass
    def fonk2(self, l: b9):
        return [self.fonk7(b2) for b2 in l]
    def fonk3(self):
        pass
class class2(b3):
    def fonk4(self, str):
        return np.asarray(b9(str))
    def fonk5(self):
        def fonk6(b2, y):
            return SimpleWeight(1.) if b2 = = y else SimpleWeight(0.)
        return simple_compare
class class3(class2):
    def fonk7(self, str):
        return np.asarray(str.split())
class class4:
    def fonk8(self, text, b4, b5, b7: b3 = class2(), b6=[]):
        self.b4 = b4
        self.b5 = b5
        self.b6 = b6
        self.b7 = b7
        self.b8 = self.b7.fonk7(text)
        b1.info(f"class4 shape: {self.fonk9().shape}")
    def fonk9(self):
        return np.asarray(self.b8[self.b4:self.b5])
    def fonk10(self, text_embedding_list: b9):
        return class5(self, text_embedding_list)
    def fonk11(self, text: str):
        b19: b9 = self.b7.fonk7(text)
        return self.fonk10(b19)
    def fonk12(self):
        return self.b5 - self.b4
class class5:
    def fonk13(self, b10: class4, text_embedding_list: b9) -> None:
        super().fonk15()
        self.b10 = b10
        self.b11 = text_embedding_list
        self.b12 = LCS(text_embedding_list, b10.fonk9(), b20 = b10.b7.fonk5())
        self.i, self.b13 = self.b12.b27-1, self.b12.n-1
    def fonk14(self):
        b14 = self.b12.backtrack_indexes(self.i, self.b13)
        b1.info(b14)
        b1.info(f'b12 len: {self.b12.b17}')
        if b14:
            (i1, j1, w1) = b14[0]
            (i2, j2, w2) = b14[-1]
            s1, b15 = (i1, i2 + 1), (j1, j2 + 1)
            a1 = 0.
            for p1, p2, wi in b14:
                a1 += wi.get_weight()
            b16 = a1 / self.b10.fonk12()
            b1.info(f'b16 = {b16}')
            if b16 < self.b12.threshold:
                return None, None
            self.i, self.b13 = s1[0], self.b12.n-1
            self.b12.b17 = self.b12.matrix[self.i, self.b13]
            return b16, s1
        else:
            return None, None
class class6:
    def fonk15(self, b18, w) -> None:
        super().fonk15()
        self.b18 = b18
        self.b16 = w
def fonk16(b10: class4, text: b9) -> Tuple[float, Tuple[int, int]]:
    b19 = b10.b7.fonk7(text)
    return fonk17(b10, b19)
def fonk17(b10, b19) -> Tuple[float, Tuple[int, int]]:
    b12 = LCS(b19, b10.fonk9(),
              b20 = b10.b7.fonk5())
    span1, span2, b16 = b12.backtrack_full()
    return b16, span1
def fonk18(b26, b25, b21 = ' '):
    w, b18 = b26
    return fonk19(b18, b25, b21 = b21)
def fonk19(b18, b25, b21 = ' '):
    return b21.join(b25[b18[0]:b18[1]])
if b22 = = '__main__':
    b23 = class2()
    b24 = class4('XSMJAUZZZ', 2, 6, b7=b23)
    b25 = 'XSASSFMJAZUREDFMZZZMJAUZPPP'
    b26 = fonk16(b24, b9(b25))
    b1.info('rez:', b26)
    b1.info(fonk18(b26, b25))
    b27 = b24.fonk11(b25)
    while True:
        w, b18 = b27.fonk14()
        if b18 is None:
            break
        b1.info(f'b18:{b18} w: {w}')
        b1.info(fonk19(b18, b9(b25), b21 = ''))