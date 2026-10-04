class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])
    def print_distances(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print(f"{i}\t\t{dist[i]}")
    def bellman_ford(self, src):
        dist = [float("inf")] * self.V
        dist[src] = 0
        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        for u, v, w in self.graph:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                print("Graph contains a negative-weight cycle")
                return
        self.print_distances(dist)
def main():
    vertices = int(input("Enter the number of vertices: "))
    edges = int(input("Enter the number of edges: "))
    graph = Graph(vertices)
    for _ in range(edges):
        u = int(input("Enter the source vertex: "))
        v = int(input("Enter the destination vertex: "))
        w = int(input("Enter the weight of the edge: "))
        graph.add_edge(u, v, w)
    src = int(input("Enter the source vertex for Bellman-Ford algorithm: "))
    graph.bellman_ford(src)
if __name__ == "__main__":
    main()