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
        self.vertices.update([source, destination])
        self.edges[source].append((destination, weight))
    def distance_and_shortest_path(self, source, destination):
        if source not in self.vertices or destination not in self.vertices:
            return inf, None
        distance = {vertex: inf for vertex in self.vertices}
        distance[source] = 0
        predecessor = {}
        heap = IndexedHeap((distance[vertex], vertex) for vertex in self.vertices)
        while not heap.is_empty():
            current_distance, current_vertex = heap.pop()
            if current_vertex == destination:
                break
            for neighbor, weight in self.edges[current_vertex]:
                new_distance = current_distance + weight
                if new_distance < distance[neighbor]:
                    distance[neighbor] = new_distance
                    predecessor[neighbor] = current_vertex
                    heap.change_weight(neighbor, new_distance)
        if distance[destination] == inf:
            return inf, None
        path = self._reconstruct_path(predecessor, source, destination)
        return distance[destination], path
    def _reconstruct_path(self, predecessor, source, destination):
        path = []
        step = destination
        while step != source:
            path.append(step)
            step = predecessor.get(step)
            if step is None:
                return None
        path.append(source)
        path.reverse()
        return path
if __name__ == "__main__":
    import doctest
    doctest.testmod()