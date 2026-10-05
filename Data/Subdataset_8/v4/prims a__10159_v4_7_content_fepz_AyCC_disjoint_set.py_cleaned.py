class DisjointSets:
    def __init__(self, elements):
        self.elements = list(elements)
        self.parent_sets = list(range(len(elements)))
        self.set_ranks = [1] * len(elements)
    def find(self, element):
        index = root_index = self.elements.index(element)
        while self.parent_sets[root_index] != root_index:
            root_index = self.parent_sets[root_index]
        while index != root_index:
            next_index = self.parent_sets[index]
            self.parent_sets[index] = root_index
            index = next_index
        return root_index
    def merge(self, set_a, set_b):
        if self.set_ranks[set_a] == self.set_ranks[set_b]:
            self.set_ranks[set_a] += 1
            self.parent_sets[set_b] = set_a
        else:
            if self.set_ranks[set_a] > self.set_ranks[set_b]:
                self.parent_sets[set_b] = set_a
            else:
                self.parent_sets[set_a] = set_b