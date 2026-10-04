class Graph:
    def __init__(self):
        self.vertexList = []
        self.edgeList = []
    def add_vertex(self, name):
        if name in self.vertexList:
            print(f"A vertex with name {name} already exists.")
        else:
            self.vertexList.append(name)
    def add_edge(self, start, end):
        if start not in self.vertexList:
            self.vertexList.append(start)
        if end not in self.vertexList:
            self.vertexList.append(end)
        if start in self.vertexList and end in self.vertexList:
            self.edgeList.append((start, end))
    def remove_vertex(self, name):
        if name in self.vertexList:
            self.vertexList.remove(name)
            self.edgeList = [edge for edge in self.edgeList if edge[0] != name and edge[1] != name]
        else:
            print(f"No vertex named {name} found.")
    def remove_edge(self, start, end):
        if (start, end) in self.edgeList:
            self.edgeList.remove((start, end))
        else:
            print(f"No edge from {start} to {end} found.")
    def vertices(self):
        return self.vertexList
    def print_edges(self):
        for start, end in self.edgeList:
            print(f"{start} -> {end}")
    def is_connected(self, start, end):
        return (start, end) in self.edgeList
    def print_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            print(" -> ".join(path))
        if start not in self.vertexList:
            return
        for node in self.vertexList:
            if (start, node) in self.edgeList and node not in path:
                self.print_paths(node, end, path)
class UndirectedGraph(Graph):
    def __init__(self):
        super().__init__()
    def add_edge(self, start, end):
        super().add_edge(start, end)
        if (end, start) not in self.edgeList:
            self.edgeList.append((end, start))
    def print_edges(self):
        for start, end in self.edgeList:
            print(f"{start} <-> {end}")
    def print_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            print(" <-> ".join(path))
        if start not in self.vertexList:
            return
        for node in self.vertexList:
            if (start, node) in self.edgeList and node not in path:
                self.print_paths(node, end, path)
g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "C")
print("Vertices:", g.vertices())
g.print_edges()
print("Is connected A -> B:", g.is_connected("A", "B"))
print("Paths from A to C:")
g.print_paths("A", "C")
ug = UndirectedGraph()
ug.add_vertex("X")
ug.add_vertex("Y")
ug.add_edge("X", "Y")
ug.add_edge("X", "Z")
ug.add_edge("Y", "Z")
print("Vertices:", ug.vertices())
ug.print_edges()
print("Is connected X <-> Y:", ug.is_connected("X", "Y"))
print("Paths from X to Z:")
ug.print_paths("X", "Z")