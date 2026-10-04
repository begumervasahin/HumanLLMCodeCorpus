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
        while heap.peek() != destination:
            current_vertex = heap.pop()
            current_distance = distance[current_vertex]
            for neighbor, edge_weight in self.edges[current_vertex]:
                new_distance = current_distance + edge_weight
                if new_distance < distance[neighbor]:
                    distance[neighbor] = new_distance
                    predecessor[neighbor] = current_vertex
                    heap.change_weight(neighbor, new_distance)
        if distance[destination] == inf:
            return inf, None
        path = []
        step = destination
        while step != source:
            path.append(step)
            step = predecessor.get(step)
            if step is None:
                return inf, None
        path.append(source)
        path.reverse()
        return distance[destination], path
if __name__ == "__main__":
    import doctest
    doctest.testmod()