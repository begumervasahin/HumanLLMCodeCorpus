class Edge:
    def __init__(self, vertex1, vertex2, weight):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.weight = weight
        self.selected = False
        self.extra = 1
def run_prim(edgelist, nodecount):
    edgelist.sort(key=lambda edge: edge.weight)
    mst_set = set()
    edgelist[0].selected = True
    mst_set.add(edgelist[0])
    edgelist[0].extra = 0
    edges_in_mst = 1
    while edges_in_mst < nodecount - 1:
        for edge in edgelist:
            if edge.extra == 1:
                found_first, found_second = False, False
                for selected_edge in mst_set:
                    if edge.vertex1 in (selected_edge.vertex1, selected_edge.vertex2):
                        found_first = True
                    if edge.vertex2 in (selected_edge.vertex1, selected_edge.vertex2):
                        found_second = True
                if found_first and found_second:
                    edge.extra = 0
                elif found_first or found_second:
                    mst_set.add(edge)
                    edge.selected = True
                    edge.extra = 0
                    edges_in_mst += 1
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