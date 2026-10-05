import math
import heapq
class DijkstraOutput:
    def __init__(self, graph, start):
        self.start = start
        self.graph = graph
        self.distance_from_start = {vertex: math.inf for vertex in graph.vertices}
        self.distance_from_start[start] = 0
        self.predecessor_edges = {vertex: [] for vertex in graph.vertices}
    def update_distance(self, vertex, edge, new_distance):
        self.distance_from_start[vertex] = new_distance
        if new_distance < self.distance_from_start[vertex]:
            self.predecessor_edges[vertex] = [edge]
        else:
            self.predecessor_edges[vertex].append(edge)
    def path_contains_edge(self, destination, edge):
        predecessors = self.predecessor_edges[destination]
        if edge in predecessors:
            return True
        return any(self.path_contains_edge(e.source, edge) for e in predecessors)
    def total_distance(self, subset=None):
        subset = subset or self.graph.vertices
        return sum(self.distance_from_start[vertex] for vertex in subset)
def dijkstra(graph, start):
    output = DijkstraOutput(graph, start)
    visit_queue = [(0, start)]
    while visit_queue:
        priority, current = heapq.heappop(visit_queue)
        for incident_edge in graph.incident_edges[current]:
            target_vertex = incident_edge.target
            edge_weight = incident_edge.weight
            distance_from_current = output.distance_from_start[current] + edge_weight
            if distance_from_current <= output.distance_from_start[target_vertex]:
                output.update_distance(target_vertex, incident_edge, distance_from_current)
                heapq.heappush(visit_queue, (distance_from_current, target_vertex))
    return output