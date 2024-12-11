import networkx as nx
from Graph import Graph
class class1:
    def fonk1(self, graph_file):
        self.b1 = Graph(graph_file).b1
    def fonk2(self, source, target):
        return nx.dijkstra_path_length(self.b1, source, target)
    def fonk3(self, source, target):
        return nx.dijkstra_path(self.b1, source, target)
    def fonk4(self, source, target, blacklist):
        b2 = self.b1.copy()
        b2.remove_nodes_from(blacklist)
        return nx.dijkstra_path_length(b2, source, target)
    def fonk5(self):
        return nx.diameter(self.b1)
    def fonk6(self):
        return nx.radius(self.b1)
    def fonk7(self):
        for vertex1 in self.b1.nodes:
            for vertex2 in self.b1.nodes:
                if nx.dijkstra_path_length(self.b1, vertex1, vertex2) > 1:
                    return False
        return True
    def fonk8(self):
        pass
if b3 = = '__main__':
    b4 = class1('g0.txt')
    print(b4.fonk7())