class DisjointSet:
    def __init__(self, size):
        if size < 0:
            raise ValueError("Size must be >= 0")
        self.size = size
        self.parent = [-1] * (size + 1)
    def union(self, root1, root2):
        if root1 < 0 or root1 > self.size or root2 < 0 or root2 > self.size:
            raise ValueError("Illegal value")
        self.parent[root2] = root1
    def find(self, root):
        if root < 0 or root > self.size:
            raise ValueError("Illegal value")
        if self.parent[root] < 0:
            return root
        else:
            self.parent[root] = self.find(self.parent[root])
            return self.parent[root]