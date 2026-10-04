class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])
    def print_graph(self, dist):
        print("Distance from source to each vertex:")
        for i in range(self.V):
            print(f"{i} \t\t {dist[i]}")
    def bellman_ford(self, src):
        dist = [float("Inf")] * self.V
        dist[src] = 0
        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains a negative-weight cycle")
                return
        self.print_graph(dist)
def main():
    vertices = int(input("Enter number of vertices:\n"))
    edges = int(input("Enter number of edges:\n"))
    g = Graph(vertices)
    for i in range(edges):
        u = int(input("Source vertex:\n"))
        v = int(input("Destination vertex:\n"))
        w = int(input("Weight of edge:\n"))
        g.add_edge(u, v, w)
    src = int(input("Enter the source vertex:\n"))
    g.bellman_ford(src)
if __name__ == "__main__":
    main()