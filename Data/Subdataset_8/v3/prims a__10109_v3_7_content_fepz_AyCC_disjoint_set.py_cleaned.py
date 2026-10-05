class DisjointSets:
    def __init__(self, elements):
        self.elements = list(elements)
        self.sets = list(range(len(elements)))
        self.ranks = [1] * len(elements)
    def find(self, x):
        current_index = root_index = self.elements.index(x)
        while self.sets[root_index] != root_index:
            root_index = self.sets[root_index]
        while current_index != root_index:
            next_index = self.sets[current_index]
            self.sets[current_index] = root_index
            current_index = next_index
        return root_index
    def merge(self, set_a, set_b):
        if self.ranks[set_a] == self.ranks[set_b]:
            self.ranks[set_a] += 1
            self.sets[set_b] = set_a
        else:
            if self.ranks[set_a] > self.ranks[set_b]:
                self.sets[set_b] = set_a
            else:
                self.sets[set_a] = set_b
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