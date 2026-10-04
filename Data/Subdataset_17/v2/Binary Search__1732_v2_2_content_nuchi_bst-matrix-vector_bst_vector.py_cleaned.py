import random
class _BSTVectorBase:
    def set(self, index, value):
        raise NotImplementedError
    def get(self, index):
        raise NotImplementedError
    def sample(self):
        raise NotImplementedError
    @property
    def norm2(self):
        return self._norm2
    def __repr__(self):
        return f"<BSTVector of dimension {self._dim}: {self.__str__()}>"
class _BSTVectorLeaf(_BSTVectorBase):
    def __init__(self):
        self.value = 0.0
        self._norm2 = 0.0
        self._dim = 1
    def set(self, index, value):
        if index != 0:
            raise IndexError("Index out of bounds for leaf node.")
        self.value = float(value)
        self._update_norm2()
    def get(self, index):
        if index != 0:
            raise IndexError("Index out of bounds for leaf node.")
        return self.value
    def sample(self):
        return 0
    def _update_norm2(self):
        self._norm2 = self.value ** 2
    def __str__(self):
        return str(self.value)
class _BSTVectorNode(_BSTVectorBase):
    def __init__(self, dim):
        self._dim = dim
        self._norm2 = 0.0
        self.left = None
        self.right = None
    def set(self, index, value):
        if index < self.cutoff:
            if self.left is None:
                self.left = BSTVector(self.cutoff)
            self.left.set(index, value)
        else:
            if self.right is None:
                self.right = BSTVector(self._dim - self.cutoff)
            self.right.set(index - self.cutoff, value)
        self._update_norm2()
    def get(self, index):
        if index >= self._dim:
            raise IndexError("Index out of bounds.")
        if index < self.cutoff:
            return self.left.get(index) if self.left else 0.0
        else:
            return self.right.get(index - self.cutoff) if self.right else 0.0
    def sample(self, seed=None):
        if self.norm2 == 0.0:
            raise ValueError("No nonzero entries")
        left_norm2 = self.left.norm2 if self.left else 0.0
        if seed is not None:
            random.seed(seed)
        if random.uniform(0, self.norm2) < left_norm2:
            return self.left.sample()
        else:
            return self.cutoff + self.right.sample()
    def _update_norm2(self):
        self._norm2 = sum(child.norm2 for child in [self.left, self.right] if child)
    @property
    def cutoff(self):
        return self._dim
    def __str__(self):
        left_str = str(self.left) if self.left else "-" * self.cutoff
        right_str = str(self.right) if self.right else "-" * (self._dim - self.cutoff)
        return f"({left_str} {right_str})"
def BSTVector(dim):
    return _BSTVectorLeaf() if dim == 1 else _BSTVectorNode(dim)
if __name__ == "__main__":
    vec = BSTVector(4)
    vec.set(0, 3)
    vec.set(1, 4)
    vec.set(2, 5)
    vec.set(3, 6)
    print(vec)
    print("Norm2:", vec.norm2)
    print("Sampled index:", vec.sample())
    print("Value at index 2:", vec.get(2))