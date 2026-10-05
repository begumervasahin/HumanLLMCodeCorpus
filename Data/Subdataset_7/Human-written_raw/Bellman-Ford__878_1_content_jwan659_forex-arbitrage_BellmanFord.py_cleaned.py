from Vert import Vertex
from Edges import Edge
class class1():
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
        self.b3 = list()
    def fonk2(self, src):
        src.set_min_distance(0)
        for i in range(len(self.b1) - 1):
            for edge in self.b2:
                if (edge.get_start().get_min_distance() == float('inf')):
                    continue
                b4 = edge.get_start().get_min_distance() + edge.get_weight()
                if (b4 < edge.get_target().get_min_distance()):
                    edge.get_target().set_min_distance(b4)
                    edge.get_target().set_previous_vertex(edge.get_start())
        for edge in self.b2:
            if(edge.get_start().get_min_distance() != float('inf')):
                if(self.fonk3(edge)):
                    b5 = edge.get_start()
                    while (b5 != edge.get_target()):
                        self.b3.append(b5)
                        b5 = b5.get_previous_vertex()
                    self.b3.append(edge.get_target())
                    return
    def fonk3(self, edge):
        return edge.get_target().get_min_distance() > edge.get_start().get_min_distance() + edge.get_weight()
    def fonk4(self):
        if (self.b3):
            print("An arbitrage opportunity has been detected: ")
            for b5 in self.b3:
                print(b5)
        else:
            print("No arbitrage opportunity! ")