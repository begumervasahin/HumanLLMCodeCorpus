import numpy as np
import logging
from typing import Any, Tuple, Union, List
from weighted_lcs import LCS, Weightable, SimpleWeight
b1 = logging.getLogger(b23)
class b3:
    def fonk1(self, b25: b21):
        raise NotImplementedError
    def fonk2(self, texts: List[b21]) -> List[np.ndarray]:
        return [self.fonk7(b25) for b25 in texts]
    def fonk3(self):
        raise NotImplementedError
class class2(b3):
    def fonk4(self, b25: b21) -> np.ndarray:
        return np.asarray(list(b25))
    def fonk5(self):
        def fonk6(b2, y):
            return SimpleWeight(1.0) if b2 = = y else SimpleWeight(0.0)
        return simple_compare
class class3(class2):
    def fonk7(self, b25: b21) -> np.ndarray:
        return np.asarray(b25.split())
class class4:
    def fonk8(self, b25: b21, b4: int, b5: int, b7: b3 = class2(), b6: List[int] = []):
        self.b4 = b4
        self.b5 = b5
        self.b6 = b6
        self.b7 = b7
        self.b8 = self.b7.fonk7(b25)
        b1.info(f"class4 shape: {self.fonk9().shape}")
    def fonk9(self) -> np.ndarray:
        return np.asarray(self.b8[self.b4:self.b5])
    def fonk10(self, text_embedding_list: List[np.ndarray]):
        return class5(self, text_embedding_list)
    def fonk11(self, b25: b21):
        b9 = self.b7.fonk7(b25)
        return self.fonk10(b9)
    def fonk12(self) -> int:
        return self.b5 - self.b4
class class5:
    def fonk13(self, b10: class4, text_embedding_list: List[np.ndarray]) -> None:
        self.b10 = b10
        self.b11 = text_embedding_list
        self.b12 = LCS(text_embedding_list, b10.fonk9(), compare=b10.b7.fonk5())
        self.i, self.b13 = self.b12.m - 1, self.b12.n - 1
    def fonk14(self) -> Union[Tuple[float, Tuple[int, int]], Tuple[None, None]]:
        b14 = self.b12.backtrack_indexes(self.i, self.b13)
        b1.info(b14)
        b1.info(f'LCS length: {self.b12.b19}')
        if b14:
            (i1, j1, w1) = b14[0]
            (i2, j2, w2) = b14[-1]
            s1, b15 = (i1, i2 + 1), (j1, j2 + 1)
            b16 = sum(wi.get_weight() for _, _, wi in b14)
            b17 = b16 / self.b10.fonk12()
            b1.info(f'b18 = {b17}')
            if b17 < self.b12.threshold:
                return None, None
            self.i, self.b13 = s1[0], self.b12.n - 1
            self.b12.b19 = self.b12.matrix[self.i, self.b13]
            return b17, s1
        return None, None
class class6:
    def fonk15(self, b20: Tuple[int, int], b17: float) -> None:
        self.b20 = b20
        self.b17 = b17
def fonk16(b10: class4, b25: List[b21]) -> Tuple[float, Tuple[int, int]]:
    b9 = b10.b7.fonk7(b25)
    return fonk17(b10, b9)
def fonk17(b10: class4, b9: List[np.ndarray]) -> Tuple[float, Tuple[int, int]]:
    b12 = LCS(b9, b10.fonk9(), compare=b10.b7.fonk5())
    span1, span2, b17 = b12.backtrack_full()
    return b17, span1
def fonk18(res: Tuple[float, Tuple[int, int]], s: b21, b22: b21 = ' ') -> b21:
    b17, b20 = res
    return fonk19(b20, s, b22 = b22)
def fonk19(b20: Tuple[int, int], s: b21, b22: b21 = ' ') -> b21:
    return b22.join(s[b20[0]:b20[1]])
if b23 = = '__main__':
    b24 = class2()
    b10 = class4('XSMJAUZZZ', 2, 6, b7=b24)
    b25 = 'XSASSFMJAZUREDFMZZZMJAUZPPP'
    b26 = fonk16(b10, list(b25))
    b1.info(f'Result: {b26}')
    b1.info(fonk18(b26, b25))
    b27 = b10.fonk11(b25)
    while True:
        b17, b20 = b27.fonk14()
        if b20 is None:
            break
        b1.info(f'Span: {b20}, b18: {b17}')
        b1.info(fonk19(b20, list(b25), b22 = ''))