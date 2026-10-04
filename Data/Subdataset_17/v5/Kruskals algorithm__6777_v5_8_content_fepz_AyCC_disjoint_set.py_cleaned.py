class DisjointSets:
    def __init__(self, elements):
        self.elements = list(elements)
        self.parent = {element: element for element in elements}
        self.rank = {element: 1 for element in elements}
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def merge(self, set_a, set_b):
        root_a = self.find(set_a)
        root_b = self.find(set_b)
        if root_a != root_b:
            if self.rank[root_a] > self.rank[root_b]:
                self.parent[root_b] = root_a
            elif self.rank[root_a] < self.rank[root_b]:
                self.parent[root_a] = root_b
            else:
                self.parent[root_b] = root_a
                self.rank[root_a] += 1
