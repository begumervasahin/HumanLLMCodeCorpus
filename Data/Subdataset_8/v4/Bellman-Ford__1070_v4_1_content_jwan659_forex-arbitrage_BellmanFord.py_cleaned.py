class BellmanFord:
    def __init__(self, vertex_list, edge_list):
        self.vertex_list = vertex_list
        self.edge_list = edge_list
        self.cycle_list = []
    def run_bellman_ford(self, source_vertex):
        source_vertex.set_min_distance(0)
        for _ in range(len(self.vertex_list) - 1):
            for edge in self.edge_list:
                if edge.get_start().get_min_distance() == float('inf'):
                    continue
                new_distance = edge.get_start().get_min_distance() + edge.get_weight()
                if new_distance < edge.get_target().get_min_distance():
                    edge.get_target().set_min_distance(new_distance)
                    edge.get_target().set_previous_vertex(edge.get_start())
        for edge in self.edge_list:
            if edge.get_start().get_min_distance() != float('inf'):
                if self.has_cycle(edge):
                    self.detect_cycle(edge)
                    return
    def has_cycle(self, edge):
        return edge.get_target().get_min_distance() > edge.get_start().get_min_distance() + edge.get_weight()
    def detect_cycle(self, edge):
        vertex = edge.get_start()
        while vertex != edge.get_target():
            self.cycle_list.append(vertex)
            vertex = vertex.get_previous_vertex()
        self.cycle_list.append(edge.get_target())
    def print_cycle_detection(self):
        if self.cycle_list:
            print("An arbitrage opportunity has been detected:")
            for vertex in self.cycle_list:
                print(vertex)
        else:
            print("No arbitrage opportunity!")
if __name__ == "__main__":
    vertex_a = Vertex('A')
    vertex_b = Vertex('B')
    vertex_c = Vertex('C')
    edge_ab = Edge(vertex_a, vertex_b, 10)
    edge_bc = Edge(vertex_b, vertex_c, 5)
    edge_ca = Edge(vertex_c, vertex_a, -15)
    vertices = [vertex_a, vertex_b, vertex_c]
    edges = [edge_ab, edge_bc, edge_ca]
    bellman_ford = BellmanFord(vertices, edges)
    bellman_ford.run_bellman_ford(vertex_a)
    bellman_ford.print_cycle_detection()