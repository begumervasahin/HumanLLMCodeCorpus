import numpy as np
import logging
from typing import Any, Tuple, Union, List
from weighted_lcs import LCS, Weightable, SimpleWeight
logger = logging.getLogger(__name__)
class EmbeddingContext:
    def get_embedding_tensor(self, text: str):
        raise NotImplementedError
    def get_embedding_tensors(self, texts: List[str]) -> List[np.ndarray]:
        return [self.get_embedding_tensor(text) for text in texts]
    def get_compare_func(self):
        raise NotImplementedError
class CharEmbeddingContext(EmbeddingContext):
    def get_embedding_tensor(self, text: str) -> np.ndarray:
        return np.asarray(list(text))
    def get_compare_func(self):
        def simple_compare(x, y):
            return SimpleWeight(1.0) if x == y else SimpleWeight(0.0)
        return simple_compare
class SimpleTokenEmbeddingContext(CharEmbeddingContext):
    def get_embedding_tensor(self, text: str) -> np.ndarray:
        return np.asarray(text.split())
class Pattern:
    def __init__(self, text: str, start: int, stop: int, embedding_context: EmbeddingContext = CharEmbeddingContext(), var_positions: List[int] = []):
        self.start = start
        self.stop = stop
        self.var_positions = var_positions
        self.embedding_context = embedding_context
        self.embedding = self.embedding_context.get_embedding_tensor(text)
        logger.info(f"Pattern shape: {self.get_pattern_embedding().shape}")
    def get_pattern_embedding(self) -> np.ndarray:
        return np.asarray(self.embedding[self.start:self.stop])
    def get_matcher(self, text_embedding_list: List[np.ndarray]):
        return Matcher(self, text_embedding_list)
    def get_matcher_str(self, text: str):
        text_emb_list = self.embedding_context.get_embedding_tensor(text)
        return self.get_matcher(text_emb_list)
    def get_pattern_len(self) -> int:
        return self.stop - self.start
class Matcher:
    def __init__(self, pattern: Pattern, text_embedding_list: List[np.ndarray]) -> None:
        self.pattern = pattern
        self.text_emb = text_embedding_list
        self.lcs = LCS(text_embedding_list, pattern.get_pattern_embedding(), compare=pattern.embedding_context.get_compare_func())
        self.i, self.j = self.lcs.m - 1, self.lcs.n - 1
    def find(self) -> Union[Tuple[float, Tuple[int, int]], Tuple[None, None]]:
        indexes = self.lcs.backtrack_indexes(self.i, self.j)
        logger.info(indexes)
        logger.info(f'LCS length: {self.lcs.lcs_length}')
        if indexes:
            (i1, j1, w1) = indexes[0]
            (i2, j2, w2) = indexes[-1]
            s1, s2 = (i1, i2 + 1), (j1, j2 + 1)
            sw = sum(wi.get_weight() for _, _, wi in indexes)
            weight = sw / self.pattern.get_pattern_len()
            logger.info(f'Weight = {weight}')
            if weight < self.lcs.threshold:
                return None, None
            self.i, self.j = s1[0], self.lcs.n - 1
            self.lcs.lcs_length = self.lcs.matrix[self.i, self.j]
            return weight, s1
        return None, None
class Match:
    def __init__(self, span: Tuple[int, int], weight: float) -> None:
        self.span = span
        self.weight = weight
def find_fuzzy_pattern(pattern: Pattern, text: List[str]) -> Tuple[float, Tuple[int, int]]:
    text_emb_list = pattern.embedding_context.get_embedding_tensor(text)
    return find_fuzzy_pattern_emb(pattern, text_emb_list)
def find_fuzzy_pattern_emb(pattern: Pattern, text_emb_list: List[np.ndarray]) -> Tuple[float, Tuple[int, int]]:
    lcs = LCS(text_emb_list, pattern.get_pattern_embedding(), compare=pattern.embedding_context.get_compare_func())
    span1, span2, weight = lcs.backtrack_full()
    return weight, span1
def get_string_from_tuple(res: Tuple[float, Tuple[int, int]], s: str, delimiter: str = ' ') -> str:
    weight, span = res
    return get_string_from_span(span, s, delimiter=delimiter)
def get_string_from_span(span: Tuple[int, int], s: str, delimiter: str = ' ') -> str:
    return delimiter.join(s[span[0]:span[1]])
if __name__ == '__main__':
    ec = CharEmbeddingContext()
    pattern = Pattern('XSMJAUZZZ', 2, 6, embedding_context=ec)
    text = 'XSASSFMJAZUREDFMZZZMJAUZPPP'
    result = find_fuzzy_pattern(pattern, list(text))
    logger.info(f'Result: {result}')
    logger.info(get_string_from_tuple(result, text))
    matcher = pattern.get_matcher_str(text)
    while True:
        weight, span = matcher.find()
        if span is None:
            break
        logger.info(f'Span: {span}, Weight: {weight}')
        logger.info(get_string_from_span(span, list(text), delimiter=''))