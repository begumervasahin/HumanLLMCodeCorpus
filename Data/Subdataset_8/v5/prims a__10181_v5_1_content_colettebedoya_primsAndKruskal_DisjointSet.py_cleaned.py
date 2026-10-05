class DisjointSet:
    def __init__(self, size):
        if size < 0:
            raise ValueError("Size must be non-negative")
        self.size = size
        self.parent = [-1] * (size + 1)
    def union(self, root1, root2):
        if not self._is_valid_root(root1) or not self._is_valid_root(root2):
            raise ValueError("Root value out of bounds")
        self.parent[root2] = root1
    def find(self, element):
        if not self._is_valid_element(element):
            raise ValueError("Element value out of bounds")
        if self.parent[element] < 0:
            return element
        else:
            return self.find(self.parent[element])
    def _is_valid_root(self, root):
        return 0 <= root <= self.size
    def _is_valid_element(self, element):
        return 0 <= element <= self.size