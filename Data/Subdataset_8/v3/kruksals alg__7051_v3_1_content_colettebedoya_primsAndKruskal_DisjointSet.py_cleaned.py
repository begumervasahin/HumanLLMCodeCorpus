class DisjointSet:
    def __init__(self, size):
        if size < 0:
            raise ValueError("Size must be >= 0")
        self.size = size
        self.parent = [-1] * (size + 1)
    def union(self, x, y):
        if not (0 < x <= self.size and 0 < y <= self.size):
            raise ValueError("Elements out of range")
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_y] = root_x
    def find(self, x):
        if not (0 < x <= self.size):
            raise ValueError("Element out of range")
        if self.parent[x] < 0:
            return x
        else:
            return self.find(self.parent[x])
if __name__ == "__main__":
    dj = DisjointSet(10)
    dj.union(1, 2)
    dj.union(3, 4)
    dj.union(4, 5)
    print(dj.find(5))
