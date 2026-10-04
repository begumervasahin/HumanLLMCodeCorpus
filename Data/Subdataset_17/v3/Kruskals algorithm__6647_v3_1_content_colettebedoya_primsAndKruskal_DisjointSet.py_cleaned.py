class DisjointSet:
    def __init__(self, size):
        if size < 0:
            raise ValueError("Size must be >= 0")
        self.size = size
        self.parent = [-1] * (size + 1)
    def find(self, element):
        self._validate_element(element)
        if self.parent[element] < 0:
            return element
        else:
            self.parent[element] = self.find(self.parent[element])
            return self.parent[element]
    def union(self, element1, element2):
        self._validate_element(element1)
        self._validate_element(element2)
        root1 = self.find(element1)
        root2 = self.find(element2)
        if root1 != root2:
            self.parent[root2] = root1
    def _validate_element(self, element):
        if element < 0 or element > self.size:
            raise ValueError(f"Element {element} is out of bounds")
if __name__ == "__main__":
    ds = DisjointSet(10)
    ds.union(1, 2)
    ds.union(3, 4)
    ds.union(2, 3)
    print("Root of 1:", ds.find(1))
    print("Root of 2:", ds.find(2))
    print("Root of 3:", ds.find(3))
    print("Root of 4:", ds.find(4))
    try:
        print(ds.find(11))
    except ValueError as e:
        print("Error:", e)