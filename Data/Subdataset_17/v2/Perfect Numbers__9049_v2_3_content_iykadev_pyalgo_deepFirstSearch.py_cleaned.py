class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}
        self.color = 'white'
        self.predecessor = None
        self.discovery_time = 0
        self.finish_time = 0
    def add_neighbor(self, neighbor, weight=0):
        self.connected_to[neighbor] = weight
    def set_color(self, color):
        self.color = color
    def set_predecessor(self, predecessor):
        self.predecessor = predecessor
    def set_discovery_time(self, time):
        self.discovery_time = time
    def set_finish_time(self, time):
        self.finish_time = time
    def get_connections(self):
        return self.connected_to.keys()
    def get_color(self):
        return self.color
    def get_predecessor(self):
        return self.predecessor
    def get_discovery_time(self):
        return self.discovery_time
    def get_finish_time(self):
        return self.finish_time
    def get_id(self):
        return self.id
    def get_weight(self, neighbor):
        return self.connected_to[neighbor]
    def __str__(self):
        return f"{self.id} connected to: {[x.id for x in self.connected_to]}"
class Graph:
    def __init__(self):
        self.vertex_list = {}
        self.num_vertices = 0
    def add_vertex(self, key):
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vertex_list[key] = new_vertex
        return new_vertex
    def get_vertex(self, key):
        return self.vertex_list.get(key)
    def __contains__(self, key):
        return key in self.vertex_list
    def add_edge(self, from_vertex, to_vertex, weight=0):
        if from_vertex not in self.vertex_list:
            self.add_vertex(from_vertex)
        if to_vertex not in self.vertex_list:
            self.add_vertex(to_vertex)
        self.vertex_list[from_vertex].add_neighbor(self.vertex_list[to_vertex], weight)
    def get_vertices(self):
        return self.vertex_list.keys()
    def __iter__(self):
        return iter(self.vertex_list.values())
class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0
    def dfs(self):
        for vertex in self:
            vertex.set_color('white')
            vertex.set_predecessor(None)
        for vertex in self:
            if vertex.get_color() == 'white':
                self._dfs_visit(vertex)
    def _dfs_visit(self, vertex):
        vertex.set_color('gray')
        self.time += 1
        vertex.set_discovery_time(self.time)
        for next_vertex in vertex.get_connections():
            if next_vertex.get_color() == 'white':
                next_vertex.set_predecessor(vertex)
                self._dfs_visit(next_vertex)
        vertex.set_color('black')
        self.time += 1
        vertex.set_finish_time(self.time)
if __name__ == "__main__":
    g = DFSGraph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('B', 'E')
    g.add_edge('C', 'F')
    g.add_edge('C', 'G')
    g.dfs()
    for vertex in g:
        print(f"Vertex {vertex.get_id()}: discovery time = {vertex.get_discovery_time()}, finish time = {vertex.get_finish_time()}")