class Graph:
    def __init__(self):
        self.vertices = {}
    def add_directed_edge(self, start, end, weight):
        if start not in self.vertices:
            self.vertices[start] = {}
        self.vertices[start][end] = weight
        if end not in self.vertices:
            self.vertices[end] = {}
def prim(graph, start_vertex):
    visited = {vertex: False for vertex in graph.vertices}
    parent = {vertex: None for vertex in graph.vertices}
    key = {vertex: float('inf') for vertex in graph.vertices}
    key[start_vertex] = 0
    while False in visited.values():
        u = min(filter(lambda x: not visited[x], key), key=key.get)
        visited[u] = True
        for v, weight in graph.vertices[u].items():
            if not visited[v] and weight < key[v]:
                parent[v] = u
                key[v] = weight
    tree = Graph()
    for v in parent:
        if parent[v] is not None:
            tree.add_directed_edge(parent[v], v, graph.vertices[parent[v]][v])
    return tree
def test_prim_algorithm():
    my_graph = Graph()
    my_graph.add_directed_edge('a', 'b', 4)
    my_graph.add_directed_edge('a', 'h', 8)
    my_graph.add_directed_edge('b', 'c', 8)
    my_graph.add_directed_edge('c', 'd', 7)
    my_graph.add_directed_edge('b', 'h', 11)
    my_graph.add_directed_edge('h', 'i', 7)
    my_graph.add_directed_edge('i', 'c', 2)
    my_graph.add_directed_edge('i', 'g', 6)
    my_graph.add_directed_edge('h', 'g', 1)
    my_graph.add_directed_edge('g', 'f', 2)
    my_graph.add_directed_edge('c', 'f', 4)
    my_graph.add_directed_edge('d', 'f', 14)
    my_graph.add_directed_edge('d', 'e', 9)
    my_graph.add_directed_edge('f', 'e', 10)
    tree = prim(my_graph, 'a')
    for start_vertex, edges in tree.vertices.items():
        for end_vertex, weight in edges.items():
            print(f"({start_vertex}, {end_vertex}, {weight})")
if __name__ == "__main__":
    test_prim_algorithm()