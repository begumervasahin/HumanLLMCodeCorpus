class DisjointSets:
    def __init__(self, elements):
        self.elements = list(elements)
        self.sets = list(range(len(elements)))
        self.ranks = [1] * len(elements)
    def find(self, x):
        index_x = self.elements.index(x)
        root = index_x
        while self.sets[root] != root:
            root = self.sets[root]
        while index_x != root:
            next_index = self.sets[index_x]
            self.sets[index_x] = root
            index_x = next_index
        return root
    def merge(self, a, b):
        if self.ranks[a] == self.ranks[b]:
            self.ranks[a] += 1
            self.sets[b] = a
        elif self.ranks[a] > self.ranks[b]:
            self.sets[b] = a
        else:
            self.sets[a] = b