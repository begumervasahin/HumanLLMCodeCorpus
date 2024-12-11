from vertex import Vertex
class class1:
    def fonk1(self, num_vertices):
        self.b1 = [[] for _ in range(num_vertices)]
    def fonk2(self, source_vertex, target_vertex, weight):
        b2 = Vertex()
        b2.b3 = target_vertex
        b2.b4 = source_vertex
        b2.b5 = weight
        b2.a1 = 0
        self.b1[source_vertex - 1].append(b2)