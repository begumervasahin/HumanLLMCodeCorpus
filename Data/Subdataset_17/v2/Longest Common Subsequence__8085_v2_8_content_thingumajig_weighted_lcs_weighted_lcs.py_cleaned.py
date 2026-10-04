import numpy as np
from typing import List, Tuple, Sequence
from cachetools import cachedmethod, LRUCache
import operator
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
class Weightable:
    def get_weight(self):
        pass
class SimpleWeight(Weightable):
    def __init__(self, weight: float) -> None:
        self.weight = weight
    def get_weight(self):
        return self.weight
class LCS:
    def __init__(self, x: Sequence, y: Sequence, threshold=0.4, compare=lambda x, y: SimpleWeight(1.0) if x == y else SimpleWeight(0.0), orig_x: Sequence = None, orig_y: Sequence = None):
        self.compare = compare
        self.m = len(x) + 1
        self.n = len(y) + 1
        self.x, self.y = x, y
        self.orig_x, self.orig_y = orig_x, orig_y
        self.threshold = threshold
        self.cache = LRUCache(maxsize=len(x) * len(y))
        self.matrix = np.zeros((self.m, self.n))
        self._calculate_matrix()
        self.lcs_length = self.matrix[self.m - 1, self.n - 1]
        logger.info(f"LCS length: {self.lcs_length}")
    def _calculate_matrix(self):
        for i in range(1, self.m):
            for j in range(1, self.n):
                weight_info = self._compare(i - 1, j - 1)
                weight = weight_info.get_weight()
                if weight > self.threshold:
                    self.matrix[i, j] = self.matrix[i - 1, j - 1] + weight
                else:
                    self.matrix[i, j] = max(self.matrix[i, j - 1], self.matrix[i - 1, j])
        self._print_matrix()
    def _print_matrix(self):
        if self.orig_x is None and not isinstance(self.x[0], str):
            return
        matrix_display = np.array(self.matrix, dtype=object)
        x_labels = self.x if self.orig_x is None else self.orig_x
        y_labels = self.y if self.orig_y is None else self.orig_y
        for i in range(len(self.x)):
            matrix_display[i + 1, 0] = self.x[i]
        for i in range(len(self.y)):
            matrix_display[0, i + 1] = self.y[i]
        logger.info(matrix_display)
    @cachedmethod(operator.attrgetter("cache"))
    def _compare(self, i, j):
        return self.compare(self.x[i], self.y[j])
    def backtrack_list(self) -> List:
        return self._backtrack_list(self.m - 1, self.n - 1)
    def _backtrack_list(self, i, j) -> List:
        if i == 0 or j == 0:
            return []
        weight_info = self._compare(i - 1, j - 1)
        weight = weight_info.get_weight()
        if weight > self.threshold:
            result = self._backtrack_list(i - 1, j - 1)
            result.append(self.x[i - 1])
            return result
        if self.matrix[i, j - 1] > self.matrix[i - 1, j]:
            return self._backtrack_list(i, j - 1)
        return self._backtrack_list(i - 1, j)
    def backtrack_indexes(self, i=None, j=None) -> List[Tuple[int, int, Weightable]]:
        if i is None:
            i = self.m - 1
        if j is None:
            j = self.n - 1
        if i == 0 or j == 0:
            return []
        weight_info = self._compare(i - 1, j - 1)
        weight = weight_info.get_weight()
        if weight > self.threshold:
            result = self.backtrack_indexes(i - 1, j - 1)
            result.append((i - 1, j - 1, weight_info))
            return result
        if self.matrix[i, j - 1] > self.matrix[i - 1, j]:
            return self.backtrack_indexes(i, j - 1)
        return self.backtrack_indexes(i - 1, j)
    def backtrack_full(self) -> Tuple[Tuple[int, int], Tuple[int, int], float]:
        indexes = self.backtrack_indexes()
        logger.info(indexes)
        return self._get_full_info(indexes)
    def _backtrack_all(self, i, j) -> List[List[Tuple[int, int]]]:
        if i == 0 or j == 0:
            return [[]]
        weight_info = self._compare(i - 1, j - 1)
        weight = weight_info.get_weight()
        if weight > self.threshold:
            sequences = self._backtrack_all(i - 1, j - 1)
            for sequence in sequences:
                sequence.append((i - 1, j - 1))
            return sequences
        results = []
        if self.matrix[i, j - 1] >= self.matrix[i - 1, j]:
            results.extend(self._backtrack_all(i, j - 1))
        if self.matrix[i - 1, j] >= self.matrix[i, j - 1]:
            results.extend(self._backtrack_all(i - 1, j))
        return results
    def backtrack_all_sequences(self) -> List[List[Tuple[int, int]]]:
        return self._backtrack_all(self.m - 1, self.n - 1)
    def _get_full_info(self, indexes: List[Tuple[int, int, Weightable]]) -> Tuple[Tuple[int, int], Tuple[int, int], float]:
        span_x, span_y = get_spans(indexes)
        return span_x, span_y, self.lcs_length
def get_spans(indexes: List[Tuple[int, int, Weightable]]) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    start_index_x, start_index_y, _ = indexes[0]
    end_index_x, end_index_y, _ = indexes[-1]
    return (start_index_x, end_index_x + 1), (start_index_y, end_index_y + 1)
def gather_array(x: Sequence, indexes: List[Tuple[int, int]], axis=0, delimiter='') -> str:
    return delimiter.join([x[idx[axis]] for idx in indexes])
def compile_arrays(x: Sequence, y: Sequence, indexes: List[Tuple[int, int]]) -> Tuple[Sequence, Sequence]:
    start_x, start_y = indexes[0]
    end_x, end_y = indexes[-1]
    return x[start_x:end_x + 1], y[start_y:end_y + 1]
def get_list_span(indexes: List[Tuple[int, int]], axis=0) -> Tuple[int, int]:
    start_index = indexes[0]
    end_index = indexes[-1]
    return start_index[axis], end_index[axis] + 1
if __name__ == "__main__":
    x = "AGGTAB"
    y = "GXTXAYB"
    lcs = LCS(x, y)
    print(f"LCS length: {lcs.lcs_length}")
    print(f"LCS sequence: {lcs.backtrack_list()}")