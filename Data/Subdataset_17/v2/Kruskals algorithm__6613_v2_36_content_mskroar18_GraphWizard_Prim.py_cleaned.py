class Edge:
    def __init__(self, vertex1, vertex2, weight):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.weight = weight
        self.selected = False
    def __repr__(self):
        return f"Edge({self.vertex1}, {self.vertex2}, {self.weight})"
def run_prim(edgelist, nodecount):
    edgelist.sort(key=lambda edge: edge.weight)
    mst_set = set()
    included_vertices = set()
    first_edge = edgelist[0]
    first_edge.selected = True
    mst_set.add(first_edge)
    included_vertices.update([first_edge.vertex1, first_edge.vertex2])
    while len(mst_set) < nodecount - 1:
        for edge in edgelist:
            if (edge.vertex1 in included_vertices) ^ (edge.vertex2 in included_vertices):
                edge.selected = True
                mst_set.add(edge)
                included_vertices.update([edge.vertex1, edge.vertex2])
                break
    return mst_set
edges = [
    Edge('A', 'B', 1),
    Edge('A', 'C', 2),
    Edge('B', 'C', 3),
    Edge('B', 'D', 4),
    Edge('C', 'D', 5)
]
nodecount = 4
mst = run_prim(edges, nodecount)
for edge in mst:
    print(f"Edge: {edge.vertex1} - {edge.vertex2}, Weight: {edge.weight}")