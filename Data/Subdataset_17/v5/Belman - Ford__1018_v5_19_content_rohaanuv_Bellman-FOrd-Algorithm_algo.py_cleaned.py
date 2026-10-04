class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []
    def add_edge(self, u, v, w):
        self.edges.append((u, v, w))
    def print_distances(self, distances):
        print("Vertex   Distance from Source")
        for vertex in range(self.vertices):
            print(f"{vertex}\t\t{distances[vertex]}")
    def bellman_ford(self, src):
        distances = [float("Inf")] * self.vertices
        distances[src] = 0
        for _ in range(self.vertices - 1):
            for u, v, w in self.edges:
                if distances[u] != float("Inf") and distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w
        for u, v, w in self.edges:
            if distances[u] != float("Inf") and distances[u] + w < distances[v]:
                print("Graph contains a negative weight cycle")
                return
        self.print_distances(distances)
if __name__ == "__main__":
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