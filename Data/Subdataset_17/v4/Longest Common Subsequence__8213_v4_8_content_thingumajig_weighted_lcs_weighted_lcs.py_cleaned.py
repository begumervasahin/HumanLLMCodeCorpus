import numpy as np
from typing import List, Tuple, Callable
from cachetools import cachedmethod, LRUCache
import operator
import logging
logger = logging.getLogger(__name__)
class Weightable:
    def get_weight(self):
        pass
class SimpleWeight(Weightable):
    def __init__(self, w: float) -> None:
        self.w = w
    def get_weight(self) -> float:
        return self.w
class LCS:
    def __init__(self,
                 x: List,
                 y: List,
                 threshold: float = 0.4,
                 compare: Callable = lambda x, y: SimpleWeight(1.) if x == y else SimpleWeight(0.),
                 orig_x: List = None,
                 orig_y: List = None) -> None:
        self.compare = compare
        self.m = len(x) + 1
        self.n = len(y) + 1
        self.x, self.y = x, y
        self.orig_x, self.orig_y = orig_x, orig_y
        self.threshold = threshold
        self.cache = LRUCache(maxsize=len(x) * len(y))
        self.matrix = np.zeros((self.m, self.n))
        for i in range(1, self.m):
            for j in range(1, self.n):
                wi = self.__compare(i - 1, j - 1)
                w = wi.get_weight()
                if w > self.threshold:
                    self.matrix[i, j] = self.matrix[i - 1, j - 1] + w
                else:
                    self.matrix[i, j] = max(self.matrix[i, j - 1], self.matrix[i - 1, j])
        self.print_matrix()
        self.lcs_length = self.matrix[self.m - 1, self.n - 1]
        logger.info(f"LCS length: {self.lcs_length}")
    def print_matrix(self) -> None:
        if self.orig_x is None and type(self.x[0]) != str:
            return
        mm = np.array(self.matrix, dtype=object)
        x = self.x if self.orig_x is None else self.orig_x
        y = self.y if self.orig_y is None else self.orig_y
        for i in range(len(self.x)):
            mm[i + 1, 0] = self.x[i]
        for i in range(len(self.y)):
            mm[0, i + 1] = self.y[i]
        logging.info(mm)
    @cachedmethod(operator.attrgetter("cache"))
    def __compare(self, i: int, j: int) -> Weightable:
        return self.compare(self.x[i], self.y[j])
    def backtrack_list(self) -> List:
        return self.__backtrack_list(self.m - 1, self.n - 1)
    def __backtrack_list(self, i: int, j: int) -> List:
        if i == 0 or j == 0:
            return []
        wi = self.__compare(i - 1, j - 1)
        w = wi.get_weight()
        if w > self.threshold:
            bck = self.__backtrack_list(i - 1, j - 1)
            bck.append(self.x[i - 1])
            return bck
        if self.matrix[i, j - 1] > self.matrix[i - 1, j]:
            return self.__backtrack_list(i, j - 1)
        return self.__backtrack_list(i - 1, j)
    def backtrack_indexes(self, i: int = None, j: int = None) -> List[Tuple[int, int, Weightable]]:
        if i is None:
            i = self.m - 1
        if j is None:
            j = self.n - 1
        if i == 0 or j == 0:
            return []
        wi = self.__compare(i - 1, j - 1)
        w = wi.get_weight()
        if w > self.threshold:
            bck = self.backtrack_indexes(i - 1, j - 1)
            bck.append((i - 1, j - 1, wi))
            return bck
        if self.matrix[i, j - 1] > self.matrix[i - 1, j]:
            return self.backtrack_indexes(i, j - 1)
        else:
            return self.backtrack_indexes(i - 1, j)
    def backtrack_full(self) -> Tuple[Tuple[int, int], Tuple[int, int], float]:
        indexes = self.backtrack_indexes()
        logger.info(indexes)
        return self.get_full_info(indexes)
    def __backtrack_all(self, i: int, j: int) -> List[List[Tuple[int, int]]]:
        if i == 0 or j == 0:
            return [[]]
        wi = self.__compare(i - 1, j - 1)
        w = wi.get_weight()
        if w > self.threshold:
            Zs = self.__backtrack_all(i - 1, j - 1)
            for z in Zs:
                z.append((i - 1, j - 1))
            return Zs
        R = []
        if self.matrix[i, j - 1] >= self.matrix[i - 1, j]:
            R.extend(self.__backtrack_all(i, j - 1))
        if self.matrix[i - 1, j] >= self.matrix[i, j - 1]:
            R.extend(self.__backtrack_all(i - 1, j))
        return R
    def backtrack_all_sequences(self) -> List[List[Tuple[int, int]]]:
        return self.__backtrack_all(self.m - 1, self.n - 1)
    def get_full_info(self, indexes: List[Tuple[int, int, Weightable]]) -> Tuple[Tuple[int, int], Tuple[int, int], float]:
        s1, s2 = get_spans(indexes)
        return s1, s2, self.lcs_length
def get_spans(indexes: List[Tuple[int, int, Weightable]]) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    (i1, j1, w1) = indexes[0]
    (i2, j2, w2) = indexes[-1]
    return (i1, i2 + 1), (j1, j2 + 1)
def gather_array(x: List[str], indexes: List[Tuple[int, int]], axis: int = 0, delimiter: str = '') -> str:
    return delimiter.join([x[j[axis]] for j in indexes])
def compile_arrays(x: List[str], y: List[str], indexes: List[Tuple[int, int]]) -> Tuple[List[str], List[str]]:
    (i1, j1) = indexes[0]
    (i2, j2) = indexes[-1]
    return x[i1:i2 + 1], y[j1:j2 + 1]
def get_list_span(indexes: List[Tuple[int, int]], axis: int = 0) -> Tuple[int, int]:
    start = indexes[0]
    ends = indexes[-1]
    return start[axis], ends[axis] + 1