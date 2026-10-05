class Graph:
    def __init__(self, vertices):
        self.num_vertices = vertices
        self.edges = []
    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))
    def print_distances(self, distances):
        print("Vertex   Distance from Source")
        for i in range(self.num_vertices):
            print("%d \t\t %d" % (i, distances[i]))
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
g = Graph(5)
g.add_edge(0, 1, -1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, -3)
g.bellman_ford(0)