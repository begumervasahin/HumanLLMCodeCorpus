class DisjointSet:
    def __init__(self, size):
        if size < 0:
            raise ValueError("Size must be >= 0")
        self.size = size
        self.parent = [-1] * (size + 1)
    def union(self, root1, root2):
        if not (0 <= root1 <= self.size) or not (0 <= root2 <= self.size):
            raise ValueError("Illegal value")
        self.parent[root2] = root1
    def find(self, root):
        if not (0 <= root <= self.size):
            raise ValueError("Illegal value")
        if self.parent[root] < 0:
            return root
        else:
            self.parent[root] = self.find(self.parent[root])
            return self.parent[root]