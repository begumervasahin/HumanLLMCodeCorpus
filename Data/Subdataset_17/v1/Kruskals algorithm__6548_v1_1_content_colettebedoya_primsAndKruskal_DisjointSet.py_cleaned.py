class DisjointSet:
    def __init__(self, size):
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = size
        self.set = [-1] * (size + 1)
    def union(self, root1, root2):
        if root1 < 0 or root1 > self.size or root2 < 0 or root2 > self.size:
            raise ValueError("Illegal value")
        root1_set = self.find(root1)
        root2_set = self.find(root2)
        if root1_set != root2_set:
            self.set[root2_set] = root1_set
    def find(self, root):
        if root < 0 or root > self.size:
            raise ValueError("Illegal value")
        if self.set[root] < 0:
            return root
        else:
            self.set[root] = self.find(self.set[root])
            return self.set[root]
if __name__ == "__main__":
    dj = DisjointSet(10)
    dj.union(1, 2)
    dj.union(3, 4)
    dj.union(2, 3)
    print("Root of 1:", dj.find(1))
    print("Root of 2:", dj.find(2))
    print("Root of 3:", dj.find(3))
    print("Root of 4:", dj.find(4))
    try:
        print(dj.find(11))
    except ValueError as e:
        print(e)