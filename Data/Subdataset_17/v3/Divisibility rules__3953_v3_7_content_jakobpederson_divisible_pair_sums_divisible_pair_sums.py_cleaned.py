from collections import namedtuple
Element = namedtuple('Element', ['index', 'value'])
class DivisiblePairSums:
    def __init__(self, n, k, ar):
        self.n = n
        self.k = k
        self.ar = ar
        self.elements = [Element(index, value) for index, value in enumerate(ar)]
    def answer_question(self):
        if not self._validate_data():
            return "Error: invalid input"
        pair_count = 0
        for i in range(len(self.elements)):
            for j in range(i + 1, len(self.elements)):
                if (self.elements[i].value + self.elements[j].value) % self.k == 0:
                    pair_count += 1
        return pair_count
    def _validate_data(self):
        return 2 <= self.n <= 100 and 1 <= self.k <= 100 and len(self.ar) <= 100
if __name__ == "__main__":
    n = 6
    k = 3
    ar = [1, 3, 2, 6, 1, 2]
    dps = DivisiblePairSums(n, k, ar)
    result = dps.answer_question()
    print(result)
