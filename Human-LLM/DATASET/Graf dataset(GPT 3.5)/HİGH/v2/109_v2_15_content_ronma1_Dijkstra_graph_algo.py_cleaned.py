import networkx as nx
from Graph import Graph
class class1:
    def fonk1(self, name):
        b1 = Graph(name)
        self.b2 = b1.b2
    def fonk2(self, vertex1, vertex2):
        return nx.dijkstra_path_length(self.b2, vertex1, vertex2)
    def fonk3(self, start_vertex, end_vertex):
        return nx.dijkstra_path(self.b2, start_vertex, end_vertex)
    def fonk4(self, start_vertex, end_vertex, blacklist):
        b3 = self.b2.copy()
        b3.remove_nodes_from(blacklist)
        return nx.dijkstra_path_length(b3, start_vertex, end_vertex)
    def fonk5(self):
        return nx.diameter(self.b2)
    def fonk6(self):
        return nx.radius(self.b2)
    def fonk7(self):
        for vertex1 in self.b2.nodes:
            for vertex2 in self.b2.nodes:
                if nx.dijkstra_path_length(self.b2, vertex1, vertex2) > 1:
                    return False
        return True
    def fonk8(self):
        pass
if b4 = = '__main__':
    b5 = class1('g0.txt')
    print(b5.fonk7())