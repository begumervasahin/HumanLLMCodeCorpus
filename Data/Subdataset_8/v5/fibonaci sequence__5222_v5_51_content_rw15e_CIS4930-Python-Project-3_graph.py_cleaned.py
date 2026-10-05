class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []
    def add_vertex(self, vertex_name):
        if vertex_name in self.vertices:
            print(f"A vertex with name '{vertex_name}' already exists.")
        else:
            self.vertices.append(vertex_name)
    def add_edge(self, start_vertex, end_vertex):
        if end_vertex not in self.vertices:
            self.vertices.append(end_vertex)
        if start_vertex not in self.vertices:
            self.vertices.append(start_vertex)
        if (start_vertex, end_vertex) not in self.edges:
            self.edges.append((start_vertex, end_vertex))
    def remove_vertex(self, vertex_name):
        if vertex_name in self.vertices:
            self.vertices.remove(vertex_name)
            self.edges = [edge for edge in self.edges if vertex_name not in edge]
        else:
            print(f"Vertex '{vertex_name}' not found.")
    def remove_edge(self, start_vertex, end_vertex):
        if (start_vertex, end_vertex) in self.edges:
            self.edges.remove((start_vertex, end_vertex))
        else:
            print(f"Edge '{start_vertex}' -> '{end_vertex}' not found.")
    def print_all_vertices(self):
        print("Vertices:", ", ".join(self.vertices))
    def print_all_edges(self):
        print("Edges:")
        for edge in self.edges:
            print(f"{edge[0]} -> {edge[1]}")
    def is_connected(self, start_vertex, end_vertex):
        return (start_vertex, end_vertex) in self.edges
    def print_paths(self, start_vertex, end_vertex):
        paths = []
        for vertex in self.vertices:
            if vertex == start_vertex:
                try:
                    path = " <-> ".join(self.vertices[self.vertices.index(vertex):self.vertices.index(vertex) + 6])
                    paths.append(path)
                except IndexError:
                    pass
        if paths:
            print("\n".join(paths))
class UndirectedGraph(Graph):
    def add_edge(self, start_vertex, end_vertex):
        super().add_edge(start_vertex, end_vertex)
        if (end_vertex, start_vertex) not in self.edges:
            self.edges.append((end_vertex, start_vertex))
    def remove_edge(self, start_vertex, end_vertex):
        super().remove_edge(start_vertex, end_vertex)
        if (end_vertex, start_vertex) in self.edges:
            self.edges.remove((end_vertex, start_vertex))
    def print_all_edges(self):
        print("Edges:")
        for edge in self.edges:
            print(f"{edge[0]} <-> {edge[1]}")
    def print_paths(self, start_vertex, end_vertex):
        paths = []
        for vertex in self.vertices:
            if vertex == start_vertex:
                try:
                    path = " <-> ".join(self.vertices[self.vertices.index(vertex):self.vertices.index(vertex) + 6])
                    paths.append(path)
                except IndexError:
                    pass
        if paths:
            print("\n".join(paths))