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
            pairs_count = sum(1 for x in self.ints for y in self.ints
                              if (x.value + y.value) % self.k == 0 and x.index < y.index)
            return pairs_count
        else:
            return "Error: Invalid input"
    def validate_input(self):
        valid_range = lambda x, low, high: low <= x <= high
        return valid_range(self.n, 2, 100) and valid_range(self.k, 1, 100) and valid_range(len(self.ar), 1, 100)
n = 5
k = 3
ar = [1, 3, 2, 6, 1]
divisible_pair_sums = DivisiblePairSums(n, k, ar)
result = divisible_pair_sums.count_divisible_pairs()
print(result)