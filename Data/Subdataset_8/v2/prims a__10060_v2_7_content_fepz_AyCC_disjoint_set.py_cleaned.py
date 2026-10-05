class DisjointSets:
    def __init__(self, elements):
        self.elements = list(elements)
        self.sets = list(range(len(elements)))
        self.ranks = [1] * len(elements)
    def find(self, x):
        i = r = self.elements.index(x)
        while self.sets[r] != r:
            r = self.sets[r]
        while i != r:
            j = self.sets[i]
            self.sets[i] = r
            i = j
        return r
    def merge(self, a, b):
        if self.ranks[a] == self.ranks[b]:
            self.ranks[a] += 1
            self.sets[b] = a
        else:
            if self.ranks[a] > self.ranks[b]:
                self.sets[b] = a
            else:
                self.sets[a] = b
elements = ['A', 'B', 'C', 'D', 'E']
disjoint_sets = DisjointSets(elements)
print("Initial sets:", disjoint_sets.sets)
print("Find 'A':", disjoint_sets.find('A'))
disjoint_sets.merge(0, 1)
print("Sets after merging 'A' and 'B':", disjoint_sets.sets)
print("Find 'B':", disjoint_sets.find('B'))
disjoint_sets.merge(2, 3)
print("Sets after merging 'C' and 'D':", disjoint_sets.sets)
print("Find 'D':", disjoint_sets.find('D'))