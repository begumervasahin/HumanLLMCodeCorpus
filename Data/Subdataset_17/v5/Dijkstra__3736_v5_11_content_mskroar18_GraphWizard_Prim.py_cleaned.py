class Edge:
    def __init__(self, vertex1, vertex2, weight):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.weight = weight
        self.selected = False
        self.extra = 1
def get_weight(edge):
    return edge.weight
class Graph:
    def __init__(self, edges, node_count):
        self.edges = edges
        self.node_count = node_count
    def run_prim(self):
        self.edges.sort(key=get_weight)
        mst_edges = set()
        first_edge = self.edges[0]
        first_edge.selected = True
        first_edge.extra = 0
        mst_edges.add(first_edge)
        selected_edges_count = 1
        while selected_edges_count < self.node_count - 1:
            edge_added = False
            for current_edge in self.edges:
                if current_edge.extra == 1:
                    found_first = any(
                        current_edge.vertex1 in (edge.vertex1, edge.vertex2) for edge in mst_edges
                    )
                    found_second = any(
                        current_edge.vertex2 in (edge.vertex1, edge.vertex2) for edge in mst_edges
                    )
                    if found_first and found_second:
                        current_edge.extra = 0
                    elif found_first or found_second:
                        mst_edges.add(current_edge)
                        current_edge.selected = True
                        current_edge.extra = 0
                        edge_added = True
                        selected_edges_count += 1
                        break
        return mst_edges
if __name__ == "__main__":
    edges = [
        Edge('A', 'B', 1),
        Edge('A', 'C', 3),
        Edge('B', 'C', 1),
        Edge('B', 'D', 6),
        Edge('C', 'D', 5),
    ]
    node_count = 4
    graph = Graph(edges, node_count)
    mst = graph.run_prim()
    print("Edges in the Minimum Spanning Tree:")
    for edge in mst:
        print(f"{edge.vertex1} - {edge.vertex2}: {edge.weight}")