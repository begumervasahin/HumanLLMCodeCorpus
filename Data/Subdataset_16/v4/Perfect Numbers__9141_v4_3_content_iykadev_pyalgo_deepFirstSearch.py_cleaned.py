from VertexGraph import Graph
class class1(Graph):
    def fonk1(self):
        super().fonk1()
        self.a1 = 0
    def fonk2(self):
        for vertex in self:
            vertex.setColor('white')
            vertex.setPred(-1)
        for vertex in self:
            if vertex.getColor() == 'white':
                self.fonk3(vertex)
    def fonk3(self, vertex):
        vertex.setColor('gray')
        self.a1 += 1
        vertex.setDiscovery(self.a1)
        for next_vertex in vertex.getConnections():
            if next_vertex.getColor() == 'white':
                next_vertex.setPred(vertex)
                self.fonk3(next_vertex)
        vertex.setColor('black')
        self.a1 += 1
        vertex.setFinish(self.a1)