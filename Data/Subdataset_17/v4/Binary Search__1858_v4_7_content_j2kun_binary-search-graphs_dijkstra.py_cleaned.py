import math
import heapq
class DijkstraOutput:
    def __init__(self, graph, start):
        self.start = start
        self.graph = graph
        self.distance_from_start = {v: math.inf for v in graph.vertices}
        self.distance_from_start[start] = 0
        self.predecessor_edges = {v: [] for v in graph.vertices}
    def found_shorter_path(self, vertex, edge, new_distance):
        self.distance_from_start[vertex] = new_distance
        if new_distance < self.distance_from_start[vertex]:
            self.predecessor_edges[vertex] = [edge]
        else:
            self.predecessor_edges[vertex].append(edge)
    def path_to_destination_contains_edge(self, destination, edge):
        if edge in self.predecessor_edges[destination]:
            return True
        return any(self.path_to_destination_contains_edge(e.source, edge)
                   for e in self.predecessor_edges[destination])
    def sum_of_distances(self, subset=None):
        subset = subset or self.graph.vertices
        return sum(self.distance_from_start[v] for v in subset)
def single_source_shortest_paths(graph, start):
    output = DijkstraOutput(graph, start)
    visit_queue = [(0, start)]
    while visit_queue:
        current_distance, current_vertex = heapq.heappop(visit_queue)
        for edge in graph.incident_edges[current_vertex]:
            neighbor = edge.target
            distance = current_distance + edge.weight
            if distance < output.distance_from_start[neighbor]:
                output.found_shorter_path(neighbor, edge, distance)
                heapq.heappush(visit_queue, (distance, neighbor))
            elif distance == output.distance_from_start[neighbor]:
                output.found_shorter_path(neighbor, edge, distance)
    return output