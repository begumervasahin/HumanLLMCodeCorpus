from collections import namedtuple
Element = namedtuple('Element', ['index', 'value'])
class DivisiblePairSums:
    def __init__(self, n, k, ar):
        self.n = n
        self.k = k
        self.ar = ar
        self.elements = [Element(index, value) for index, value in enumerate(ar)]
    def answer_question(self):
        if self._validate_data():
            pairs = [
                (x.value, y.value) for x in self.elements
                for y in self.elements
                if (x.value + y.value) % self.k == 0 and x.index < y.index
            ]
            return len(pairs)
        else:
            return "Error: invalid input"
    def _validate_data(self):
        if 2 <= self.n <= 100 and 1 <= self.k <= 100 and len(self.ar) <= 100:
            return True
        return False
if __name__ == "__main__":
    n = 6
    k = 3
    ar = [1, 3, 2, 6, 1, 2]
    dps = DivisiblePairSums(n, k, ar)
    result = dps.answer_question()
    print(result)
