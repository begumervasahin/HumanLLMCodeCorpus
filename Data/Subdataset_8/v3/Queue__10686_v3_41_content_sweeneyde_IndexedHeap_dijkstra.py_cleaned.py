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
        self.vertices |= {destination, source}
        self.edges[source].append((destination, weight))
    def distance_and_shortest_path(self, source, destination):
        if not {source, destination} <= self.vertices:
            return inf, None
        distance = {v: inf for v in self.vertices}
        distance[source] = 0
        predecessor = {}
        heap = IndexedHeap((distance[v], v) for v in self.vertices)
        while heap.peek() != destination:
            current_vertex = heap.pop()
            current_distance = distance[current_vertex]
            for neighbor, edge_weight in self.edges[current_vertex]:
                alternative_distance = current_distance + edge_weight
                if alternative_distance < distance[neighbor]:
                    distance[neighbor] = alternative_distance
                    predecessor[neighbor] = current_vertex
                    heap.change_weight(neighbor, alternative_distance)
        if distance[destination] == inf:
            return inf, None
        path = [destination]
        while path[-1] != source:
            path.append(predecessor[path[-1]])
        path.reverse()
        return distance[destination], path
if __name__ == "__main__":
    import doctest
    doctest.testmod()