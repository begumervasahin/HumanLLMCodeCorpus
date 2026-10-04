class Graph:
    def run_prim(self, edges, node_count):
        edges.sort(key=lambda edge: edge.weight)
        mst_edges = set()
        connected_vertices = set()
        smallest_edge = edges[0]
        mst_edges.add(smallest_edge)
        connected_vertices.update({smallest_edge.vertex1, smallest_edge.vertex2})
        while len(mst_edges) < node_count - 1:
            for edge in edges:
                if (edge.vertex1 in connected_vertices) != (edge.vertex2 in connected_vertices):
                    mst_edges.add(edge)
                    connected_vertices.update({edge.vertex1, edge.vertex2})
                    break
        return mst_edges
    @staticmethod
    def return_weight(edge):
        return edge.weight