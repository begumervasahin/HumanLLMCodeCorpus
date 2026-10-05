class Graph:
    def __init__(self):
        self.vertex_list = []
        self.edge_list = []
    def add_vertex(self, name):
        if name in self.vertex_list:
            print(f"A vertex with name '{name}' already exists.")
        else:
            self.vertex_list.append(name)
    def add_edge(self, start, end):
        if end not in self.vertex_list:
            self.vertex_list.append(end)
        if start not in self.vertex_list:
            self.vertex_list.append(start)
        if start in self.vertex_list and end in self.vertex_list:
            self.edge_list.append((start, end))
    def remove_vertex(self, name):
        if name in self.vertex_list:
            self.vertex_list.remove(name)
            self.edge_list = [edge for edge in self.edge_list if name not in edge]
        else:
            print(f"Vertex '{name}' not found.")
    def remove_edge(self, start, end):
        if (start, end) in self.edge_list:
            self.edge_list.remove((start, end))
        else:
            print(f"Edge '{start}' -> '{end}' not found.")
    def vertices(self):
        return self.vertex_list
    def print_edges(self):
        for edge in self.edge_list:
            print(f"{edge[0]} -> {edge[1]}")
    def is_connected(self, start, end):
        return any(edge == (start, end) for edge in self.edge_list)
    def print_paths(self, start, end):
        for i, vertex in enumerate(self.vertex_list):
            if vertex == start:
                try:
                    path = " <-> ".join(self.vertex_list[i:i+6])
                    print(path)
                except IndexError:
                    pass
class UndirectedGraph(Graph):
    def __init__(self):
        super().__init__()
    def add_edge(self, start, end):
        super().add_edge(start, end)
        self.edge_list.append((end, start))
    def remove_edge(self, start, end):
        super().remove_edge(start, end)
        self.edge_list.remove((end, start))
    def print_edges(self):
        for edge in self.edge_list:
            print(f"{edge[0]} <-> {edge[1]}")
    def print_paths(self, start, end):
        for i, vertex in enumerate(self.vertex_list):
            if vertex == start:
                try:
                    path = " <-> ".join(self.vertex_list[i:i+6])
                    print(path)
                except IndexError:
                    pass