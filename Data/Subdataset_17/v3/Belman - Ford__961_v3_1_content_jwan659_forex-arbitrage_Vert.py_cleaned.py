from Edges import Edge
class Vertex:
    def __init__(self, id):
        self.id = id
        self.min_distance = float('inf')
        self.adjacencies = []
        self.prev_vertex = None
        self.visited = False
    def get_min_distance(self):
        return self.min_distance
    def set_min_distance(self, distance):
        self.min_distance = distance
    def get_previous_vertex(self):
        return self.prev_vertex
    def set_previous_vertex(self, prev_vertex):
        self.prev_vertex = prev_vertex
    def add_edge(self, edge):
        self.adjacencies.append(edge)
    def get_adjacencies(self):
        return self.adjacencies
    def is_visited(self):
        return self.visited
    def set_visited(self, visited):
        self.visited = visited
    def __str__(self):
        return self.id
def main():
    vertex_A = Vertex('A')
    vertex_B = Vertex('B')
    edge_AB = Edge(vertex_A, vertex_B, 10)
    vertex_A.add_edge(edge_AB)
    vertex_A.set_min_distance(0)
    vertex_B.set_min_distance(10)
    vertex_A.set_visited(True)
    print(f"Vertex A: {vertex_A}, Min Distance: {vertex_A.get_min_distance()}, Visited: {vertex_A.is_visited()}")
    print(f"Vertex B: {vertex_B}, Min Distance: {vertex_B.get_min_distance()}, Visited: {vertex_B.is_visited()}")
    print(f"Edges from Vertex A: {[str(edge.target) for edge in vertex_A.get_adjacencies()]}")
if __name__ == "__main__":
    main()