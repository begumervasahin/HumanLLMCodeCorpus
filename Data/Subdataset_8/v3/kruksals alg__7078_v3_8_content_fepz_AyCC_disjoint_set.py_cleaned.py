class DisjointSets:
    def __init__(self, elements):
        self.elements = list(elements)
        self.set_labels = list(range(len(elements)))
        self.ranks = [1] * len(elements)
    def find(self, x):
        i = r = self.elements.index(x)
        while self.set_labels[r] != r:
            r = self.set_labels[r]
        while i != r:
            j = self.set_labels[i]
            self.set_labels[i] = r
            i = j
        return r
    def merge(self, a, b):
        if self.ranks[a] == self.ranks[b]:
            self.ranks[a] += 1
            self.set_labels[b] = a
        elif self.ranks[a] > self.ranks[b]:
            self.set_labels[b] = a
        else:
            self.set_labels[a] = b
elements = ['A', 'B', 'C', 'D', 'E']
disjoint_sets = DisjointSets(elements)
print("Initial sets:", disjoint_sets.set_labels)
print("Initial ranks:", disjoint_sets.ranks)
disjoint_sets.merge(disjoint_sets.find('A'), disjoint_sets.find('B'))
print("\nAfter merging sets containing 'A' and 'B':")
print("Sets:", disjoint_sets.set_labels)
print("Ranks:", disjoint_sets.ranks)
disjoint_sets.merge(disjoint_sets.find('C'), disjoint_sets.find('D'))
print("\nAfter merging sets containing 'C' and 'D':")
print("Sets:", disjoint_sets.set_labels)
print("Ranks:", disjoint_sets.ranks)