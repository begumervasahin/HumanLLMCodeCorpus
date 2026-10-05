import sys
class DirectedGraph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_list = [{} for _ in range(num_vertices)]
        self.shortest_path = [sys.maxsize] * num_vertices
        self.visited = [False] * num_vertices
        self.queue = []
    def print_graph(self):
        for vertex, neighbors in enumerate(self.adjacency_list):
            print(f"Adjacent vertices for {vertex}: {neighbors}")
    def print_shortest_path(self):
        for vertex, shortest_dist in enumerate(self.shortest_path):
            print(f"Bellman-Ford shortest path to {vertex}: {shortest_dist}")
def add_edge(graph, src, dest, weight):
    graph.adjacency_list[src][dest] = weight
def bellman_ford(graph):
    while graph.queue:
        bellman_ford_algorithm(graph, graph.queue.pop())
def bellman_ford_algorithm(graph, source):
    if graph.visited[source]:
        return
    for dest, weight in graph.adjacency_list[source].items():
        temp_add = graph.shortest_path[source] + weight
        if graph.shortest_path[dest] > temp_add:
            graph.shortest_path[dest] = temp_add
            graph.queue.insert(0, dest)
            graph.visited[dest] = False
    graph.visited[source] = True
def create_directed_graph(graph, source):
    graph.shortest_path[source] = 0
    graph.queue.insert(0, source)
    add_edge(graph, 0, 1, 4)
    add_edge(graph, 0, 2, 2)
    add_edge(graph, 1, 2, 3)
    add_edge(graph, 1, 3, 2)
    add_edge(graph, 1, 4, 3)
    add_edge(graph, 2, 1, 1)
    add_edge(graph, 2, 3, 4)
    add_edge(graph, 2, 4, 5)
    add_edge(graph, 4, 3, -5)
graph = DirectedGraph(5)
create_directed_graph(graph, 0)
bellman_ford(graph)
graph.print_shortest_path()