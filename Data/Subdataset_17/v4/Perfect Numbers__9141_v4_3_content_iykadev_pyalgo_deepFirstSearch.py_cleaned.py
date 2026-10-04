from VertexGraph import Graph
class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0
    def dfs(self):
        for vertex in self:
            vertex.setColor('white')
            vertex.setPred(-1)
        for vertex in self:
            if vertex.getColor() == 'white':
                self._dfs_visit(vertex)
    def _dfs_visit(self, vertex):
        vertex.setColor('gray')
        self.time += 1
        vertex.setDiscovery(self.time)
        for next_vertex in vertex.getConnections():
            if next_vertex.getColor() == 'white':
                next_vertex.setPred(vertex)
                self._dfs_visit(next_vertex)
        vertex.setColor('black')
        self.time += 1
        vertex.setFinish(self.time)