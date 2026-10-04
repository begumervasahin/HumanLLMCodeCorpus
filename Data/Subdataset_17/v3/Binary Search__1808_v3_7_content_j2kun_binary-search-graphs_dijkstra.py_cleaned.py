import math
import heapq
from collections import defaultdict
class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight
class Graph:
    def __init__(self):
        self.vertices = set()
        self.incident_edges = defaultdict(list)
    def add_edge(self, source, target, weight):
        edge = Edge(source, target, weight)
        self.vertices.add(source)
        self.vertices.add(target)
        self.incident_edges[source].append(edge)
class DijkstraOutput:
    def __init__(self, graph, start):
        self.start = start
        self.graph = graph
        self.distance_from_start = {v: math.inf for v in graph.vertices}
        self.distance_from_start[start] = 0
        self.predecessor_edges = {v: [] for v in graph.vertices}
    def update_shorter_path(self, vertex, edge, new_distance):
        if new_distance < self.distance_from_start[vertex]:
            self.distance_from_start[vertex] = new_distance
            self.predecessor_edges[vertex] = [edge]
        elif new_distance == self.distance_from_start[vertex]:
            self.predecessor_edges[vertex].append(edge)
    def contains_edge_in_path(self, destination, edge):
        if edge in self.predecessor_edges[destination]:
            return True
        return any(self.contains_edge_in_path(e.source, edge)
                   for e in self.predecessor_edges[destination])
    def total_distance_sum(self, subset=None):
        subset = subset or self.graph.vertices
        return sum(self.distance_from_start[v] for v in subset)
def dijkstra_shortest_paths(graph, start):
    output = DijkstraOutput(graph, start)
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        if current_distance > output.distance_from_start[current_vertex]:
            continue
        for edge in graph.incident_edges[current_vertex]:
            target = edge.target
            new_distance = current_distance + edge.weight
            if new_distance < output.distance_from_start[target]:
                output.update_shorter_path(target, edge, new_distance)
                heapq.heappush(priority_queue, (new_distance, target))
            elif new_distance == output.distance_from_start[target]:
                output.update_shorter_path(target, edge, new_distance)
    return output
if __name__ == "__main__":
    graph = Graph()
    graph.add_edge('A', 'B', 1)
    graph.add_edge('A', 'C', 4)
    graph.add_edge('B', 'C', 2)
    graph.add_edge('B', 'D', 5)
    graph.add_edge('C', 'D', 1)
    start_vertex = 'A'
    dijkstra_output = dijkstra_shortest_paths(graph, start_vertex)
    for vertex in graph.vertices:
        distance = dijkstra_output.distance_from_start[vertex]
        print(f"Distance from {start_vertex} to {vertex}: {distance}")
    total_distance = dijkstra_output.total_distance_sum()
    print(f"Sum of distances: {total_distance}")