class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []
    def add_edge(self, start, end, weight):
        self.edges.append((start, end, weight))
    def print_distances(self, distances):
        print("Vertex   Distance from Source")
        for vertex, distance in enumerate(distances):
            print(f"{vertex} \t\t {distance}")
    def bellman_ford(self, source):
        distances = [float("inf")] * self.vertices
        distances[source] = 0
        for _ in range(self.vertices - 1):
            for start, end, weight in self.edges:
                if distances[start] != float("inf") and distances[start] + weight < distances[end]:
                    distances[end] = distances[start] + weight
        for start, end, weight in self.edges:
            if distances[start] != float("inf") and distances[start] + weight < distances[end]:
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