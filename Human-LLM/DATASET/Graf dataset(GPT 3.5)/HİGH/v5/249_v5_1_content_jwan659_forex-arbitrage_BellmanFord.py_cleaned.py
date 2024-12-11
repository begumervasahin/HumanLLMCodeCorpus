class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
        self.b3 = []
    def fonk2(self, source_vertex):
        source_vertex.set_min_distance(0)
        for _ in range(len(self.b1) - 1):
            for edge in self.b2:
                if edge.get_start().get_min_distance() == float('inf'):
                    continue
                b4 = edge.get_start().get_min_distance() + edge.get_weight()
                if b4 < edge.get_target().get_min_distance():
                    edge.get_target().set_min_distance(b4)
                    edge.get_target().set_previous_vertex(edge.get_start())
        for edge in self.b2:
            if edge.get_start().get_min_distance() != float('inf'):
                if self.fonk3(edge):
                    self.fonk4(edge)
                    return
    def fonk3(self, edge):
        return edge.get_target().get_min_distance() > edge.get_start().get_min_distance() + edge.get_weight()
    def fonk4(self, edge):
        b5 = edge.get_start()
        while b5 != edge.get_target():
            self.b3.append(b5)
            b5 = b5.get_previous_vertex()
        self.b3.append(edge.get_target())
    def fonk5(self):
        if self.b3:
            print("An arbitrage opportunity has been detected:")
            for b5 in self.b3:
                print(b5)
        else:
            print("No arbitrage opportunity!")
if b6 = = "__main__":
    b7 = Vertex('A')
    b8 = Vertex('B')
    b9 = Vertex('C')
    b10 = Edge(b7, b8, 10)
    b11 = Edge(b8, b9, 5)
    b12 = Edge(b9, b7, -15)
    b13 = [b7, b8, b9]
    b14 = [b10, b11, b12]
    b15 = class1(b13, b14)
    b15.fonk2(b7)
    b15.fonk5()