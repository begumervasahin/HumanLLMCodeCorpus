class Vertex:
    def __init__(self, name):
        self.name = name
        self.min_distance = float('inf')
        self.previous_vertex = None
    def set_min_distance(self, distance):
        self.min_distance = distance
    def get_min_distance(self):
        return self.min_distance
    def set_previous_vertex(self, vertex):
        self.previous_vertex = vertex
    def __str__(self):
        return self.name
class Edge:
    def __init__(self, start, target, weight):
        self.start = start
        self.target = target
        self.weight = weight
    def get_start(self):
        return self.start
    def get_target(self):
        return self.target
    def get_weight(self):
        return self.weight
class BellmanFord:
    def __init__(self, vertex_list, edge_list):
        self.vertex_list = vertex_list
        self.edge_list = edge_list
        self.cycle_list = []
    def bellman_ford(self, src_name):
        src_vertex = None
        for vertex in self.vertex_list:
            if vertex.name == src_name:
                src_vertex = vertex
                break
        if not src_vertex:
            print("Source vertex not found!")
            return
        src_vertex.set_min_distance(0)
        for _ in range(len(self.vertex_list) - 1):
            for edge in self.edge_list:
                if edge.get_start().get_min_distance() == float('inf'):
                    continue
                dist = edge.get_start().get_min_distance() + edge.get_weight()
                if dist < edge.get_target().get_min_distance():
                    edge.get_target().set_min_distance(dist)
                    edge.get_target().set_previous_vertex(edge.get_start())
        for edge in self.edge_list:
            if edge.get_start().get_min_distance() != float('inf'):
                if self.has_cycle(edge):
                    vertex = edge.get_start()
                    while vertex != edge.get_target():
                        self.cycle_list.append(vertex)
                        vertex = vertex.get_previous_vertex()
                    self.cycle_list.append(edge.get_target())
                    return
    def has_cycle(self, edge):
        return edge.get_target().get_min_distance() > edge.get_start().get_min_distance() + edge.get_weight()
    def print_cycle(self):
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
    bellman_ford.bellman_ford('A')
    bellman_ford.print_cycle()