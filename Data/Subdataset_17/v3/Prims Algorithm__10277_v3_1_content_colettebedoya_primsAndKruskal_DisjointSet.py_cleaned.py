class DisjointSet:
    def __init__(self, size):
        if size < 0:
            raise ValueError("Size must be >= 0")
        self.size = size
        self.parent = [-1] * (size + 1)
    def union(self, element1, element2):
        if not self._is_valid_element(element1) or not self._is_valid_element(element2):
            raise ValueError("Element value out of range")
        self.parent[element2] = element1
    def find(self, element):
        if not self._is_valid_element(element):
            raise ValueError("Element value out of range")
        if self.parent[element] < 0:
            return element
        else:
            return self.find(self.parent[element])
    def _is_valid_element(self, element):
        return 0 <= element <= self.size
if __name__ == "__main__":
    ds = DisjointSet(10)
    ds.union(1, 2)
    ds.union(3, 4)
    print(ds.find(2))
    print(ds.find(4))
    ds.union(1, 3)
    print(ds.find(4))
