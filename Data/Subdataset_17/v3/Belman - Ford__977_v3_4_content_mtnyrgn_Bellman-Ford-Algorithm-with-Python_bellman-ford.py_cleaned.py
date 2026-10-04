class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []
    def add_edge(self, source, destination, weight):
        self.edges.append([source, destination, weight])
    def print_distances(self, distances):
        print("Vertex Distance from Source")
        for vertex, distance in enumerate(distances):
            print(f"{vertex}\t\t{distance}")
    def bellman_ford(self, source):
        distances = [float("inf")] * self.vertices
        distances[source] = 0
        for _ in range(self.vertices - 1):
            for u, v, w in self.edges:
                if distances[u] != float("inf") and distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w
        for u, v, w in self.edges:
            if distances[u] != float("inf") and distances[u] + w < distances[v]:
                print("Graph contains a negative-weight cycle")
                return
        self.print_distances(distances)
def main():
    vertices = int(input("Enter the number of vertices: "))
    edges = int(input("Enter the number of edges: "))
    graph = Graph(vertices)
    for _ in range(edges):
        source = int(input("Enter the source vertex: "))
        destination = int(input("Enter the destination vertex: "))
        weight = int(input("Enter the weight of the edge: "))
        graph.add_edge(source, destination, weight)
    source_vertex = int(input("Enter the source vertex for the Bellman-Ford algorithm: "))
    graph.bellman_ford(source_vertex)
if __name__ == "__main__":
    main()