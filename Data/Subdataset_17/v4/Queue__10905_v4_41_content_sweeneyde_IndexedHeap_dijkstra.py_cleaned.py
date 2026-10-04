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
        h = IndexedHeap((distance[v], v) for v in self.vertices)
        while h:
            v = h.pop()
            if v == destination:
                break
            v_dist = distance[v]
            for neighbor, edge_weight in self.edges[v]:
                alt_dist = v_dist + edge_weight
                if alt_dist < distance[neighbor]:
                    distance[neighbor] = alt_dist
                    predecessor[neighbor] = v
                    h.change_weight(neighbor, alt_dist)
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