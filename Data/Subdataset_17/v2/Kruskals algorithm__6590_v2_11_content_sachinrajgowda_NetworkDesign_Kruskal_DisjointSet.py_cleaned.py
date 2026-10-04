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
    forest = DisjointSet()
    mst = []
    for node in nodes:
        forest.add(node)
    edges_needed = len(nodes) - 1
    for edge in sorted_edges:
        src, dest, weight = edge
        root1 = forest.find(src)
        root2 = forest.find(dest)
        if root1 != root2:
            mst.append(edge)
            forest.union(root1, root2)
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