from typing import Any, Tuple, List
import numpy as np
import logging
b1 = logging.getLogger(b27)
logging.basicConfig(b2 = logging.INFO)
class class1:
    def fonk1(self):
        pass
class class2(class1):
    def fonk2(self, b3: float):
        self.b3 = b3
    def fonk3(self) -> float:
        return self.b3
class class3:
    def fonk4(self, b4, b5, b6):
        self.b4 = b4
        self.b5 = b5
        self.b6 = b6
        self.b7 = len(b4)
        self.b8 = len(b5)
        self.b9 = np.zeros((self.b7+1, self.b8+1), dtype=float)
        self.a1 = 0
        self.a2 = 0.5
        self.fonk5()
    def fonk5(self):
        for i in range(1, self.b7 + 1):
            for b11 in range(1, self.b8 + 1):
                if self.b6(self.b4[i-1], self.b5[b11-1]).fonk3() > 0:
                    self.b9[i][b11] = self.b9[i-1][b11-1] + 1
                else:
                    self.b9[i][b11] = max(self.b9[i-1][b11], self.b9[i][b11-1])
        self.a1 = self.b9[self.b7][self.b8]
    def fonk6(self, i, b11):
        b10 = []
        while i > 0 and b11 > 0:
            if self.b6(self.b4[i-1], self.b5[b11-1]).fonk3() > 0:
                b10.append((i-1, b11-1, self.b6(self.b4[i-1], self.b5[b11-1])))
                i -= 1
                b11 -= 1
            elif self.b9[i-1][b11] >= self.b9[i][b11-1]:
                i -= 1
            else:
                b11 -= 1
        b10.reverse()
        return b10
    def fonk7(self):
        i, b11 = self.b7, self.b8
        b10 = self.fonk6(i, b11)
        if b10:
            (i1, j1, w1) = b10[0]
            (i2, j2, w2) = b10[-1]
            s1, b12 = (i1, i2 + 1), (j1, j2 + 1)
            b13 = sum(wi.fonk3() for _, _, wi in b10)
            b3 = b13 / self.a1
            if b3 < self.a2:
                return None, None, 0
            return s1, b12, b3
        return None, None, 0
class b15:
    def fonk8(self, text: str):
        pass
    def fonk9(self, l: list):
        return [self.fonk14(b14) for b14 in l]
    def fonk10(self):
        pass
class class5(b15):
    def fonk11(self, text: str):
        return np.asarray(list(text))
    def fonk12(self):
        def fonk13(b14, y):
            return class2(1.) if b14 = = y else class2(0.)
        return simple_compare
class class6(class5):
    def fonk14(self, text: str):
        return np.asarray(text.split())
class class7:
    def fonk15(self, text: str, b16: int, b17: int, b19: b15 = class5(), b18=[]):
        self.b16 = b16
        self.b17 = b17
        self.b18 = b18
        self.b19 = b19
        self.b20 = self.b19.fonk14(text)
        b1.info(f"class7 shape: {self.fonk16().shape}")
    def fonk16(self):
        return np.asarray(self.b20[self.b16:self.b17])
    def fonk17(self, text_embedding_list: list):
        return class8(self, text_embedding_list)
    def fonk18(self, text: str):
        b21 = self.b19.fonk14(text)
        return self.fonk17(b21)
    def fonk19(self):
        return self.b17 - self.b16
class class8:
    def fonk20(self, b22: class7, text_embedding_list: list) -> None:
        self.b22 = b22
        self.b23 = text_embedding_list
        self.b24 = class3(text_embedding_list, b22.fonk16(), b6=b22.b19.fonk12())
        self.i, self.b11 = self.b24.b7-1, self.b24.b8-1
    def fonk21(self):
        b10 = self.b24.fonk6(self.i, self.b11)
        b1.info(b10)
        b1.info(f'b24 len: {self.b24.a1}')
        if b10:
            (i1, j1, w1) = b10[0]
            (i2, j2, w2) = b10[-1]
            s1, b12 = (i1, i2 + 1), (j1, j2 + 1)
            b13 = sum(wi.fonk3() for _, _, wi in b10)
            b3 = b13 / self.b22.fonk19()
            b1.info(f'b3 = {b3}')
            if b3 < self.b24.a2:
                return None, None
            self.i, self.b11 = s1[0], self.b24.b8-1
            self.b24.a1 = self.b24.b9[self.i, self.b11]
            return b3, s1
        else:
            return None, None
class class9:
    def fonk22(self, b25, w) -> None:
        self.b25 = b25
        self.b3 = w
def fonk23(b22: class7, text: str) -> Tuple[float, Tuple[int, int]]:
    b21 = b22.b19.fonk14(text)
    return fonk24(b22, b21)
def fonk24(b22: class7, b21: list) -> Tuple[float, Tuple[int, int]]:
    b24 = class3(b21, b22.fonk16(), b6=b22.b19.fonk12())
    span1, span2, b3 = b24.fonk7()
    return b3, span1
def fonk25(b31, b30, b26 = ' '):
    w, b25 = b31
    return fonk26(b25, b30, b26 = b26)
def fonk26(b25, b30, b26 = ' '):
    return b26.join(b30[b25[0]:b25[1]])
if b27 = = '__main__':
    b28 = class5()
    b29 = class7('XSMJAUZZZ', 2, 6, b19=b28)
    b30 = 'XSASSFMJAZUREDFMZZZMJAUZPPP'
    b31 = fonk23(b29, list(b30))
    b1.info('rez:', b31)
    b1.info(fonk25(b31, b30))
    b7 = b29.fonk18(b30)
    while True:
        w, b25 = b7.fonk21()
        if b25 is None:
            break
        b1.info(f'b25:{b25} w: {w}')
        b1.info(fonk26(b25, list(b30), b26 = ''))