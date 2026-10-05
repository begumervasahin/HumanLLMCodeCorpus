from VertexGraph import Graph
class DepthFirstSearch(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0
    def depth_first_search(self):
        for vertex in self:
            vertex.set_color('white')
            vertex.set_predecessor(-1)
        for vertex in self:
            if vertex.get_color() == 'white':
                self._dfs_visit(vertex)
    def _dfs_visit(self, start_vertex):
        start_vertex.set_color('gray')
        self.time += 1
        start_vertex.set_discovery(self.time)
        for next_vertex in start_vertex.get_connections():
            if next_vertex.get_color() == 'white':
                next_vertex.set_predecessor(start_vertex)
                self._dfs_visit(next_vertex)
        start_vertex.set_color('black')
        self.time += 1
        start_vertex.set_finish(self.time)
dfs_graph = DepthFirstSearch()
dfs_graph.depth_first_search()