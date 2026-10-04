class DisjointSets:
    def __init__(self, elements):
        self.elems = list(elements)
        self.sets = list(range(len(elements)))
        self.ranks = [1] * len(elements)
    def find(self, x):
        i = r = self.elems.index(x)
        while self.sets[r] != r:
            r = self.sets[r]
        while i != r:
            j = self.sets[i]
            self.sets[i] = r
            i = j
        return r
    def merge(self, a, b):
        if self.ranks[a] == self.ranks[b]:
            self.ranks[a] = self.ranks[a] + 1
            self.sets[b] = a
        else:
            if self.ranks[a] > self.ranks[b]:
                self.sets[b] = a
            else:
                self.sets[a] = b