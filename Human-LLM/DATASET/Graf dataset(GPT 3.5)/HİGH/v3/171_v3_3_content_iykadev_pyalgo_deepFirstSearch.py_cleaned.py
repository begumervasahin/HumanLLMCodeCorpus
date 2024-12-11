from VertexGraph import Graph
class class1(Graph):
    def fonk1(self):
        super().fonk1()
        self.a1 = 0
    def fonk2(self):
        self.fonk3()
        for vertex in self:
            if vertex.get_color() == 'white':
                self.fonk4(vertex)
    def fonk3(self):
        for vertex in self:
            vertex.set_color('white')
            vertex.set_predecessor(None)
            vertex.set_discovery(None)
            vertex.set_finish(None)
        self.a1 = 0
    def fonk4(self, start_vertex):
        start_vertex.set_color('gray')
        self.a1 += 1
        start_vertex.set_discovery(self.a1)
        for next_vertex in start_vertex.get_connections():
            if next_vertex.get_color() == 'white':
                next_vertex.set_predecessor(start_vertex)
                self.fonk4(next_vertex)
        start_vertex.set_color('black')
        self.a1 += 1
        start_vertex.set_finish(self.a1)
b1 = class1()
b1.fonk2()