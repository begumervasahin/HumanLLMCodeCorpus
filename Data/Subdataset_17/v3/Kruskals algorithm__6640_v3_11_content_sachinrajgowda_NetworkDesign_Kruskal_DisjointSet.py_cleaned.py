class DisjointSet:
    def __init__(self):
        self.parent = {}
    def add(self, item):
        self.parent[item] = item
    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]
    def union(self, item1, item2):
        root1 = self.find(item1)
        root2 = self.find(item2)
        if root1 != root2:
            self.parent[root2] = root1
def kruskal(nodes, sorted_edges):
    disjoint_set = DisjointSet()
    mst = []
    for node in nodes:
        disjoint_set.add(node)
    edges_needed = len(nodes) - 1
    for src, dest, weight in sorted_edges:
        root_src = disjoint_set.find(src)
        root_dest = disjoint_set.find(dest)
        if root_src != root_dest:
            mst.append((src, dest, weight))
            disjoint_set.union(root_src, root_dest)
            edges_needed -= 1
            if edges_needed == 0:
                break
    return mst
nodes = ['A', 'B', 'C', 'D', 'E']
sorted_edges = [
    ('A', 'B', 1),
    ('B', 'C', 2),
    ('C', 'D', 3),
    ('D', 'E', 4),
    ('A', 'E', 5),
    ('B', 'D', 6)
]
mst = kruskal(nodes, sorted_edges)
print("Minimum Spanning Tree:", mst)