import queue
from collections import namedtuple
Edge = namedtuple('Edge', ['vertex', 'weight'])
class GraphUndirectedWeighted(object):
    def __init__(self, vertex_count):
        self.vertex_count = vertex_count
        self.adjacency_list = [[] for _ in range(vertex_count)]
    def add_edge(self, source, dest, weight):
        assert source < self.vertex_count
        assert dest < self.vertex_count
        self.adjacency_list[source].append(Edge(dest, weight))
        self.adjacency_list[dest].append(Edge(source, weight))
    def get_edges(self, vertex):
        for edge in self.adjacency_list[vertex]:
            yield edge
    def get_vertices(self):
        for vertex in range(self.vertex_count):
            yield vertex
def dijkstra(graph, source, dest):
    pq = queue.PriorityQueue()
    parents = [None] * graph.vertex_count
    distances = [float('inf')] * graph.vertex_count
    distances[source] = 0
    pq.put((0, source))
    while not pq.empty():
        curr_distance, curr_vertex = pq.get()
        if curr_distance > distances[curr_vertex]:
            continue
        for edge in graph.get_edges(curr_vertex):
            neighbor_vertex, edge_weight = edge
            new_distance = distances[curr_vertex] + edge_weight
            if new_distance < distances[neighbor_vertex]:
                distances[neighbor_vertex] = new_distance
                parents[neighbor_vertex] = curr_vertex
                pq.put((new_distance, neighbor_vertex))
    shortest_path = []
    curr_vertex = dest
    while curr_vertex is not None:
        shortest_path.append(curr_vertex)
        curr_vertex = parents[curr_vertex]
    shortest_path.reverse()
    return shortest_path, distances[dest]
graph = GraphUndirectedWeighted(9)
graph.add_edge(0, 1, 4)
graph.add_edge(1, 7, 6)
graph.add_edge(1, 2, 1)
graph.add_edge(2, 3, 3)
graph.add_edge(3, 7, 1)
graph.add_edge(3, 4, 2)
graph.add_edge(3, 5, 1)
graph.add_edge(4, 5, 1)
graph.add_edge(5, 6, 1)
graph.add_edge(6, 7, 2)
graph.add_edge(6, 8, 2)
graph.add_edge(7, 8, 2)
shortest_path, distance = dijkstra(graph, 0, 4)
print("Shortest path:", shortest_path)
print("Distance:", distance)