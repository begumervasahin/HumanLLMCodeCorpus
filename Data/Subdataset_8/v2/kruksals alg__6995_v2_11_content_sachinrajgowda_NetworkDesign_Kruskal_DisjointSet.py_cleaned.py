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
    mst = []
    for node in nodes:
        forest.add(node)
    no_edges = len(nodes) - 1
    for edge in sorted_edges:
        src, dest, _ = edge
        root_src = forest.find(src)
        root_dest = forest.find(dest)
        if root_src != root_dest:
            mst.append(edge)
            no_edges -= 1
            if no_edges == 0:
                return mst
            forest.union(root_src, root_dest)
    return mst
nodes = ['A', 'B', 'C', 'D', 'E']
sorted_edges = [('A', 'B', 1), ('A', 'C', 3), ('B', 'C', 2), ('B', 'D', 5), ('C', 'D', 4), ('C', 'E', 6), ('D', 'E', 7)]
minimum_spanning_tree = kruskal(nodes, sorted_edges)
print("Minimum Spanning Tree:", minimum_spanning_tree)