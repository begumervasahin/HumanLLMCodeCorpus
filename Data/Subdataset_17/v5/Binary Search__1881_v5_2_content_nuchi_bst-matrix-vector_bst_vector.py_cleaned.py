import random
class BSTVectorBase:
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
        return f"<BSTVector of dimension {self._dim}: {self}>"
class BSTVectorLeaf(BSTVectorBase):
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
class BSTVectorNode(BSTVectorBase):
    def __init__(self, dim):
        self._dim = dim
        self._norm2 = 0.0
        self.left = None
        self.right = None
    def set(self, index, value):
        child_side, child_index = self._get_child_side_and_index(index)
        if getattr(self, child_side) is None:
            setattr(self, child_side, BSTVector(self._get_child_dim(child_side)))
        child = getattr(self, child_side)
        child.set(child_index, value)
        if child.norm2 == 0.0:
            setattr(self, child_side, None)
        self._update_norm2()
    def get(self, index):
        if index >= self._dim:
            raise IndexError("Index out of bounds for BSTVector.")
        child_side, child_index = self._get_child_side_and_index(index)
        child = getattr(self, child_side)
        return 0.0 if child is None else child.get(child_index)
    def sample(self, seed=None):
        if self.norm2 == 0.0:
            raise ValueError("No nonzero entries to sample.")
        left_norm2 = self.left.norm2 if self.left is not None else 0.0
        if seed is not None:
            random.seed(seed)
        if random.uniform(0, self.norm2) < left_norm2:
            return self.left.sample()
        return self.cutoff + self.right.sample()
    def _update_norm2(self):
        self._norm2 = sum(
            child.norm2 for child in [self.left, self.right] if child is not None
        )
    def _get_child_side_and_index(self, index):
        if index < self.cutoff:
            return 'left', index
        return 'right', index - self.cutoff
    def _get_child_dim(self, child_side):
        return self.cutoff if child_side == 'left' else self._dim - self.cutoff
    @property
    def cutoff(self):
        return self._dim
    def __str__(self):
        left_str = str(self.left) if self.left is not None else "-" * self.cutoff
        right_str = str(self.right) if self.right is not None else "-" * (self._dim - self.cutoff)
        return f"({left_str} {right_str})"
def BSTVector(dim):
    if dim == 1:
        return BSTVectorLeaf()
    return BSTVectorNode(dim)