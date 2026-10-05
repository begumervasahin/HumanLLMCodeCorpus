class DisjointSet(dict):
    def add(self, item):
        self[item] = item
    def find(self, item):
        parent = self[item]
        while self[parent] != parent:
            parent = self[parent]
        self[item] = parent
        return parent
    def union(self, item1, item2):
        self[item2] = self[item1]
def kruskal(nodes, sorted_edges):
    forest = DisjointSet()
    minimum_spanning_tree = []
    for node in nodes:
        forest.add(node)
    num_edges_needed = len(nodes) - 1
    for edge in sorted_edges:
        src, dest, _ = edge
        tree1 = forest.find(src)
        tree2 = forest.find(dest)
        if tree1 != tree2:
            minimum_spanning_tree.append(edge)
            num_edges_needed -= 1
            if num_edges_needed == 0:
                return minimum_spanning_tree
            forest.union(tree1, tree2)
nodes = [1, 2, 3, 4]
edges = [(1, 2, 1), (1, 3, 2), (2, 3, 3), (2, 4, 4), (3, 4, 5)]
sorted_edges = sorted(edges, key=lambda x: x[2])
mst = kruskal(nodes, sorted_edges)
print(mst)