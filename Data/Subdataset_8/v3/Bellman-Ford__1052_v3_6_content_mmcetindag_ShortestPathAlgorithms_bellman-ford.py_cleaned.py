class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.edges = []
    def add_edge(self, source, destination, weight):
        self.edges.append((source, destination, weight))
    def print_distances(self, distances):
        print("Vertex   Distance from Source")
        for i, distance in enumerate(distances):
            print("%d \t\t %d" % (i, distance))
    def bellman_ford(self, source):
        distances = [float("inf")] * self.num_vertices
        distances[source] = 0
        for _ in range(self.num_vertices - 1):
            for u, v, weight in self.edges:
                if distances[u] != float("inf") and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
        for u, v, weight in self.edges:
            if distances[u] != float("inf") and distances[u] + weight < distances[v]:
                print("Graph contains negative weight cycle")
                return
        self.print_distances(distances)
graph = Graph(5)
graph.add_edge(0, 1, -1)
graph.add_edge(0, 2, 4)
graph.add_edge(1, 2, 3)
graph.add_edge(1, 3, 2)
graph.add_edge(1, 4, 2)
graph.add_edge(3, 2, 5)
graph.add_edge(3, 1, 1)
graph.add_edge(4, 3, -3)
graph.bellman_ford(0)