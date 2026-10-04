class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []
    def add_edge(self, u, v, w):
        self.edges.append((u, v, w))
    def print_distances(self, dist):
        print("Vertex   Distance from Source")
        for i in range(self.V):
            print(f"{i}\t\t{dist[i]}")
    def bellman_ford(self, src):
        dist = [float('Inf')] * self.V
        dist[src] = 0
        for _ in range(self.V - 1):
            for u, v, w in self.edges:
                if dist[u] != float('Inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        for u, v, w in self.edges:
            if dist[u] != float('Inf') and dist[u] + w < dist[v]:
                print("Graph contains a negative weight cycle")
                return
        self.print_distances(dist)
def main():
    graph = Graph(5)
    edges = [
        (0, 1, -1),
        (0, 2, 4),
        (1, 2, 3),
        (1, 3, 2),
        (1, 4, 2),
        (3, 2, 5),
        (3, 1, 1),
        (4, 3, -3)
    ]
    for u, v, w in edges:
        graph.add_edge(u, v, w)
    graph.bellman_ford(0)
if __name__ == "__main__":
    main()