class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []
    def add_vertex(self, name):
        if name in self.vertices:
            print(f"A vertex with name '{name}' already exists.")
        else:
            self.vertices.append(name)
    def add_edge(self, start, end):
        if end not in self.vertices:
            self.vertices.append(end)
        if start not in self.vertices:
            self.vertices.append(start)
        if start in self.vertices and end in self.vertices:
            self.edges.append((start, end))
    def remove_vertex(self, name):
        if name in self.vertices:
            self.vertices.remove(name)
            self.edges = [edge for edge in self.edges if name not in edge]
        else:
            print(f"Vertex '{name}' not found.")
    def remove_edge(self, start, end):
        if (start, end) in self.edges:
            self.edges.remove((start, end))
        else:
            print(f"Edge '{start}' -> '{end}' not found.")
    def get_vertices(self):
        return self.vertices
    def print_edges(self):
        for edge in self.edges:
            print(f"{edge[0]} -> {edge[1]}")
    def is_connected(self, start, end):
        return any(edge == (start, end) for edge in self.edges)
    def print_paths(self, start, end):
        paths = []
        for edge in self.edges:
            if edge[0] == start:
                paths.append(edge[1])
            elif edge[1] == start:
                paths.append(edge[0])
        for vertex in paths:
            print(f"{start} -> {vertex} -> {end}")
class UndirectedGraph(Graph):
    def add_edge(self, start, end):
        super().add_edge(start, end)
        self.edges.append((end, start))
    def remove_edge(self, start, end):
        super().remove_edge(start, end)
        self.edges.remove((end, start))
    def print_edges(self):
        for edge in self.edges:
            print(f"{edge[0]} <-> {edge[1]}")
    def print_paths(self, start, end):
        paths = []
        for edge in self.edges:
            if edge[0] == start:
                paths.append(edge[1])
            elif edge[1] == start:
                paths.append(edge[0])
        for vertex in paths:
            print(f"{start} <-> {vertex} <-> {end}")