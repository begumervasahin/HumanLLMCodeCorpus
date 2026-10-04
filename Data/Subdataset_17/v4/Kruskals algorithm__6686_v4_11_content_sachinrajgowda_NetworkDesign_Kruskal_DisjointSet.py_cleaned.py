class DisjointSet:
    def __init__(self):
        self.parent = {}
    def add(self, item):
        self.parent[item] = item
    def find(self, item):
        root = item
        while self.parent[root] != root:
            root = self.parent[root]
        while item != root:
            parent = self.parent[item]
            self.parent[item] = root
            item = parent
        return root
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
        root_src = forest.find(src)
        root_dest = forest.find(dest)
        if root_src != root_dest:
            mst.append(edge)
            forest.union(src, dest)
            edges_needed -= 1
            if edges_needed == 0:
                break
    return mst