import random
class Graph:
    def __init__(self, is_undirected=False):
        self._adjacency_list = {}
        self._is_weighted = False
        self._is_undirected = is_undirected
    def vertices(self):
        return list(self._adjacency_list.keys())
    def edges(self):
        visited_edges = set()
        edge_list = []
        for vertex in self.vertices():
            for adjacent_vertex in self.adjacent(vertex):
                weight = self.weight((vertex, adjacent_vertex))
                edge = (vertex, adjacent_vertex, weight)
                edge_pair = (min(vertex, adjacent_vertex), max(vertex, adjacent_vertex))
                if edge_pair not in visited_edges:
                    edge_list.append(edge)
                    visited_edges.add(edge_pair)
        return edge_list
    def adjacent(self, vertex):
        return list(self._adjacency_list.get(vertex, {}).keys())
    def is_adjacent(self, origin, vertex):
        return vertex in self._adjacency_list.get(origin, {})
    def add_vertex(self, vertex):
        if vertex not in self._adjacency_list:
            self._adjacency_list[vertex] = {}
    def add_edge(self, edge, weight=1):
        vertex1, vertex2 = edge
        self._adjacency_list[vertex1][vertex2] = weight
        if self.is_undirected():
            self._adjacency_list[vertex2][vertex1] = weight
        self._is_weighted = self._is_weighted or weight != 1
    def weight(self, edge):
        vertex1, vertex2 = edge
        return self._adjacency_list[vertex1].get(vertex2, None)
    def random_vertex(self):
        vertex_list = self.vertices()
        return random.choice(vertex_list)
    def is_weighted(self):
        return self._is_weighted
    def is_undirected(self):
        return self._is_undirected