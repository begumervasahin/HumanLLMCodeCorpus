import random
class Graph:
    def __init__(self, is_undirected=False):
        self._adjacency_list = {}
        self._is_weighted = False
        self._is_undirected = is_undirected
    def vertices(self):
        return list(self._adjacency_list.keys())
    def edges(self):
        visited = set()
        edge_list = []
        for v in self.vertices():
            new_edges = [(v, u, self.weight((v, u))) for u in self.adjacent(v)]
            for edge in new_edges:
                u, v, weight = edge
                if (u, v) not in visited and (v, u) not in visited:
                    edge_list.append(edge)
                    visited.add((u, v))
        return edge_list
    def adjacent(self, vertex):
        return list(self._adjacency_list[vertex].keys())
    def is_adjacent(self, origin, vertex):
        return vertex in self._adjacency_list[origin]
    def add_vertex(self, vertex):
        if vertex not in self._adjacency_list:
            self._adjacency_list[vertex] = {}
    def add_edge(self, edge, weight=1):
        x, y = edge
        if x not in self._adjacency_list:
            self.add_vertex(x)
        if y not in self._adjacency_list:
            self.add_vertex(y)
        self._adjacency_list[x][y] = weight
        if self.is_undirected():
            self._adjacency_list[y][x] = weight
        self._is_weighted = self._is_weighted or weight != 1
    def weight(self, edge):
        x, y = edge
        return self._adjacency_list[x][y]
    def random_vertex(self):
        vertex_list = self.vertices()
        return vertex_list[random.randint(0, len(vertex_list) - 1)]
    def is_weighted(self):
        return self._is_weighted
    def is_undirected(self):
        return self._is_undirected
if __name__ == "__main__":
    graph = Graph(is_undirected=True)
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_edge(("A", "B"), 5)
    graph.add_edge(("B", "C"), 3)
    graph.add_edge(("C", "A"), 2)
    print("Vertices:", graph.vertices())
    print("Edges:", graph.edges())
    print("Is A adjacent to B?", graph.is_adjacent("A", "B"))
    print("Is A adjacent to C?", graph.is_adjacent("A", "C"))
    print("Random vertex:", graph.random_vertex())
    print("Is the graph weighted?", graph.is_weighted())
    print("Is the graph undirected?", graph.is_undirected())