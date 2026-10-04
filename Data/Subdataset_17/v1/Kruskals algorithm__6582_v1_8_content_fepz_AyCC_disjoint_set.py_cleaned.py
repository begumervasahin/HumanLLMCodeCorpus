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
        root_a = self.find(self.elems[a])
        root_b = self.find(self.elems[b])
        if root_a != root_b:
            if self.ranks[root_a] > self.ranks[root_b]:
                self.sets[root_b] = root_a
            elif self.ranks[root_a] < self.ranks[root_b]:
                self.sets[root_a] = root_b
            else:
                self.sets[root_b] = root_a
                self.ranks[root_a] += 1
if __name__ == "__main__":
    elements = ['A', 'B', 'C', 'D', 'E']
    ds = DisjointSets(elements)
    print("Initial sets:")
    for e in elements:
        print(f"{e}: {ds.find(e)}")
    ds.merge(0, 1)
    ds.merge(1, 2)
    print("\nSets after some merges:")
    for e in elements:
        print(f"{e}: {ds.find(e)}")
    ds.merge(3, 4)
    ds.merge(2, 3)
    print("\nFinal sets after all merges:")
    for e in elements:
        print(f"{e}: {ds.find(e)}")