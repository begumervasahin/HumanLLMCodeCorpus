class Graph:
    def __init__(self, vertices):
        self.num_vertices = vertices
        self.edges = []
    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))
    def print_distances(self, distances):
        print("Distances:")
        for i, distance in enumerate(distances):
            print(f"{i}\t\t{distance}")
    def bellman_ford(self, source):
        distances = [float("inf")] * self.num_vertices
        distances[source] = 0
        for _ in range(self.num_vertices - 1):
            for u, v, weight in self.edges:
                if distances[u] != float("inf") and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
        for u, v, weight in self.edges:
            if distances[u] != float("inf") and distances[u] + weight < distances[v]:
                print("Graph contains negative cycle!!")
                return
        self.print_distances(distances)
num_vertices = int(input("Enter number of vertices: "))
num_edges = int(input("Enter number of edges: "))
graph = Graph(num_vertices)
for _ in range(num_edges):
    source_vertex = int(input("Source vertex: "))
    destination_vertex = int(input("Destination vertex: "))
    edge_weight = int(input("Weight of Edge: "))
    graph.add_edge(source_vertex, destination_vertex, edge_weight)
graph.bellman_ford(0)