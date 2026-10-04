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
    for src, dest, weight in sorted_edges:
        root_src = forest.find(src)
        root_dest = forest.find(dest)
        if root_src != root_dest:
            mst.append((src, dest, weight))
            forest.union(src, dest)
            edges_needed -= 1
            if edges_needed == 0:
                break
    return mst