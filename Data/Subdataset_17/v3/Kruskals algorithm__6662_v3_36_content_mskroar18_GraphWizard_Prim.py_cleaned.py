class Edge:
    def __init__(self, vertex1, vertex2, weight):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.weight = weight
    def __repr__(self):
        return f"Edge({self.vertex1}, {self.vertex2}, {self.weight})"
def run_prim(edges, node_count):
    edges.sort(key=lambda edge: edge.weight)
    mst = []
    included_vertices = set()
    first_edge = edges[0]
    mst.append(first_edge)
    included_vertices.update([first_edge.vertex1, first_edge.vertex2])
    while len(mst) < node_count - 1:
        for edge in edges:
            if (edge.vertex1 in included_vertices) ^ (edge.vertex2 in included_vertices):
                mst.append(edge)
                included_vertices.update([edge.vertex1, edge.vertex2])
                break
    return mst
edges = [
    Edge('A', 'B', 1),
    Edge('A', 'C', 2),
    Edge('B', 'C', 3),
    Edge('B', 'D', 4),
    Edge('C', 'D', 5)
]
node_count = 4
mst = run_prim(edges, node_count)
for edge in mst:
    print(f"Edge: {edge.vertex1} - {edge.vertex2}, Weight: {edge.weight}")