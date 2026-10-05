from collections import namedtuple
Element = namedtuple('Element', ['index', 'value'])
class DivisiblePairSums:
    def __init__(self, n, k, ar):
        self.n = n
        self.k = k
        self.ar = ar
        self.ints = [Element(index=index, value=value) for index, value in enumerate(ar)]
    def count_divisible_pairs(self):
        if self.validate_input():
            pairs_count = len([(x.value, y.value) for x in self.ints
                               for y in self.ints if (x.value + y.value) % self.k == 0 and x.index < y.index])
            return pairs_count
        else:
            return "Error: Invalid input data."
    def validate_input(self):
        if not (2 <= self.n <= 100 and 1 <= self.k <= 100 and 1 <= len(self.ar) <= 100):
            return False
        return True
n = 5
k = 3
ar = [1, 3, 2, 6, 1]
divisible_pair_sums = DivisiblePairSums(n, k, ar)
result = divisible_pair_sums.count_divisible_pairs()
print(result)