class DisjointSet:
    def __init__(self, size):
        if size < 0:
            raise ValueError("Size must be >= 0")
        self.size = size
        self.parent = [-1] * (size + 1)
    def union(self, root1, root2):
        self._validate_element(root1)
        self._validate_element(root2)
        self.parent[root2] = root1
    def find(self, element):
        self._validate_element(element)
        if self.parent[element] < 0:
            return element
        else:
            self.parent[element] = self.find(self.parent[element])
            return self.parent[element]
    def _validate_element(self, element):
        if not (0 <= element <= self.size):
            raise ValueError(f"Element {element} is out of bounds.")