import random
class BSTVectorBase:
    def set(self, index, value):
        pass
    def get(self, index):
        pass
    def sample(self):
        pass
    @property
    def norm2(self):
        return self._norm2
    def __repr__(self):
        return f"<BSTVector of dimension {self._dim}: {self.__str__()}>"
class BSTVectorLeaf(BSTVectorBase):
    def __init__(self):
        self.value = 0.0
        self._norm2 = 0.0
        self._dim = 1
    def set(self, index, value):
        self.value = float(value)
        self._update_norm2()
    def get(self, index):
        if index != 0:
            raise IndexError
        return self.value
    def sample(self):
        return 0
    def _update_norm2(self):
        self._norm2 = self.value ** 2
    def __str__(self):
        return str(self.value)
class BSTVectorNode(BSTVectorBase):
    def __init__(self, dim):
        self._dim = dim
        self._norm2 = 0.0
        self.left = None
        self.right = None
    def set(self, index, value):
        child_side = 'left' if index < self.cutoff else 'right'
        child_size = self.cutoff if child_side == 'left' else self._dim - self.cutoff
        child_index = index if child_side == 'left' else index - self.cutoff
        if getattr(self, child_side) is None:
            setattr(self, child_side, BSTVector(child_size))
        child = getattr(self, child_side)
        child.set(child_index, value)
        if child.norm2 == 0.0:
            setattr(self, child_side, None)
        self._update_norm2()
    def get(self, index):
        if index >= self._dim:
            raise IndexError
        child_side = 'left' if index < self.cutoff else 'right'
        child_index = index if child_side == 'left' else index - self.cutoff
        child = getattr(self, child_side)
        if child is None:
            return 0.0
        return child.get(child_index)
    def sample(self, seed=None):
        if self.norm2 == 0.0:
            raise ValueError("No nonzero entries")
        left_norm2 = self.left.norm2 if self.left is not None else 0.0
        if seed is not None:
            random.seed(seed)
        if random.uniform(0, self.norm2) < left_norm2:
            return self.left.sample()
        return self.cutoff + self.right.sample()
    def _update_norm2(self):
        self._norm2 = sum(child.norm2 for child in [self.left, self.right] if child is not None)
    @property
    def cutoff(self):
        return self._dim
    def __str__(self):
        left_str = "-" * self.cutoff if self.left is None else str(self.left)
        right_str = "-" * (self._dim - self.cutoff) if self.right is None else str(self.right)
        return f"({left_str} {right_str})"
def BSTVector(dim):
    if dim == 1:
        return BSTVectorLeaf()
    else:
        return BSTVectorNode(dim)