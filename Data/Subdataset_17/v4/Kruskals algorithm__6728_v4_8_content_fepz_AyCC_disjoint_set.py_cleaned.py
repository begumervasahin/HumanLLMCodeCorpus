class DisjointSets:
    def __init__(self, elements):
        self.elements = list(elements)
        self.parent = list(range(len(elements)))
        self.rank = [1] * len(elements)
    def find(self, x):
        idx = root = self.elements.index(x)
        while self.parent[root] != root:
            root = self.parent[root]
        while idx != root:
            next_idx = self.parent[idx]
            self.parent[idx] = root
            idx = next_idx
        return root
    def merge(self, set_a, set_b):
        if self.rank[set_a] == self.rank[set_b]:
            self.rank[set_a] += 1
            self.parent[set_b] = set_a
        elif self.rank[set_a] > self.rank[set_b]:
            self.parent[set_b] = set_a
        else:
            self.parent[set_a] = set_b
