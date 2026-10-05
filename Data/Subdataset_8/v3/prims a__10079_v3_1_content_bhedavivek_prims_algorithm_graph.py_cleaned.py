class Vertex:
    def __init__(self, id, parent_id, distance, position=0):
        self.id = id
        self.parent_id = parent_id
        self.distance = distance
        self.position = position
class Graph:
    def __init__(self, num_vertices):
        self.adjacency_list = [[] for _ in range(num_vertices)]
    def insert_edge(self, source_vertex, target_vertex, weight):
        new_vertex = Vertex(target_vertex, source_vertex, weight)
        self.adjacency_list[source_vertex - 1].append(new_vertex)
if __name__ == "__main__":
    graph = Graph(5)
    graph.insert_edge(1, 2, 10)
    graph.insert_edge(1, 3, 15)
    graph.insert_edge(2, 4, 20)
    graph.insert_edge(3, 5, 25)
    print(graph.adjacency_list)