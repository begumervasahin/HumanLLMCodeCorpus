class DisjointSet:
    def __init__(self, size):
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = size
        self.set = [-1] * (size + 1)
    def union(self, root1, root2):
        if root1 < 0 or root1 > self.size or root2 < 0 or root2 > self.size:
            raise ValueError("Illegal value")
        self.set[root2] = root1
    def find(self, root):
        if root < 0 or root > self.size:
            raise ValueError("Illegal value")
        if self.set[root] < 0:
            return root
        else:
            return self.find(self.set[root])
if __name__ == "__main__":
    dj = DisjointSet(10)
    dj.union(1, 2)
    dj.union(3, 4)
    print(dj.find(2))
    print(dj.find(4))
    dj.union(1, 3)
    print(dj.find(4))
