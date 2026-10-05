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
                self.dfs_visit(vertex)
    def dfs_visit(self, start_vertex):
        start_vertex.setColor('gray')
        self.time += 1
        start_vertex.setDiscovery(self.time)
        for next_vertex in start_vertex.getConnections():
            if next_vertex.getColor() == 'white':
                next_vertex.setPred(start_vertex)
                self.dfs_visit(next_vertex)
        start_vertex.setColor('black')
        self.time += 1
        start_vertex.setFinish(self.time)