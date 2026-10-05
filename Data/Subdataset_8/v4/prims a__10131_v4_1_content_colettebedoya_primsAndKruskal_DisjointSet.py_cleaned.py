class DisjointSet:
    def __init__(self, size):
        if size < 0:
            raise ValueError("Size must be >= 0")
        self.size = size
        self.set = [-1] * (size + 1)
    def union(self, root1, root2):
        if not (0 <= root1 <= self.size) or not (0 <= root2 <= self.size):
            raise ValueError("Illegal value")
        self.set[root2] = root1
    def find(self, root):
        if not (0 <= root <= self.size):
            raise ValueError("Illegal value")
        if self.set[root] < 0:
            return root
        else:
            return self.find(self.set[root])