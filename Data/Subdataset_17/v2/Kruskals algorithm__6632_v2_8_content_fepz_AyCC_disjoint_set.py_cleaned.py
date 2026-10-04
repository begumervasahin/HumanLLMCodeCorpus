class DisjointSet:
    def __init__(self, elements):
        self.elements = list(elements)
        self.parent = list(range(len(elements)))
        self.rank = [1] * len(elements)
    def find(self, element):
        index = self.elements.index(element)
        if self.parent[index] != index:
            self.parent[index] = self.find(self.elements[self.parent[index]])
        return self.parent[index]
    def union(self, element_a, element_b):
        root_a = self.find(element_a)
        root_b = self.find(element_b)
        if root_a != root_b:
            if self.rank[root_a] > self.rank[root_b]:
                self.parent[root_b] = root_a
            elif self.rank[root_a] < self.rank[root_b]:
                self.parent[root_a] = root_b
            else:
                self.parent[root_b] = root_a
                self.rank[root_a] += 1
    def __str__(self):
        return "\n".join(f"{element}: {self.find(element)}" for element in self.elements)
if __name__ == "__main__":
    elements = ['A', 'B', 'C', 'D', 'E']
    ds = DisjointSet(elements)
    print("Initial sets:")
    print(ds)
    ds.union('A', 'B')
    ds.union('B', 'C')
    print("\nSets after some unions:")
    print(ds)
    ds.union('D', 'E')
    ds.union('C', 'D')
    print("\nFinal sets after all unions:")
    print(ds)