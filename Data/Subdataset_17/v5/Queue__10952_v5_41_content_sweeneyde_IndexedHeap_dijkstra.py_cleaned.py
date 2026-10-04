from collections import defaultdict
from math import inf
from indexedheap import IndexedHeap
class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = defaultdict(list)
    def add_edge(self, source, destination, weight):
        if weight < 0:
            raise ValueError("Edge weights cannot be negative.")
        self.vertices.update({source, destination})
        self.edges[source].append((destination, weight))
    def distance_and_shortest_path(self, source, destination):
        if not {source, destination} <= self.vertices:
            return inf, None
        distance = {v: inf for v in self.vertices}
        distance[source] = 0
        predecessor = {}
        heap = IndexedHeap((distance[v], v) for v in self.vertices)
        while heap:
            current_distance, current_vertex = heap.pop()
            if current_vertex == destination:
                break
            for neighbor, weight in self.edges[current_vertex]:
                alternative_route = current_distance + weight
                if alternative_route < distance[neighbor]:
                    distance[neighbor] = alternative_route
                    predecessor[neighbor] = current_vertex
                    heap.change_weight(neighbor, alternative_route)
        if distance[destination] == inf:
            return inf, None
        path = []
        current_vertex = destination
        while current_vertex != source:
            path.append(current_vertex)
            current_vertex = predecessor[current_vertex]
        path.append(source)
        path.reverse()
        return distance[destination], path
if __name__ == "__main__":
    import doctest
    doctest.testmod()