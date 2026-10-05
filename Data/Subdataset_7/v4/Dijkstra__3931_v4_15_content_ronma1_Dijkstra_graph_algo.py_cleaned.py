import networkx as nx
from Graph import Graph
class class1:
    def fonk1(self, graph_file):
        self.b1 = Graph(graph_file).b1
    def fonk2(self, vertex1, vertex2):
        return nx.dijkstra_path_length(self.b1, vertex1, vertex2)
    def fonk3(self, vertex1, vertex2):
        return nx.dijkstra_path(self.b1, vertex1, vertex2)
    def fonk4(self, vertex1, vertex2, blacklist):
        b2 = self.b1.copy()
        b2.remove_nodes_from(blacklist)
        return nx.dijkstra_path_length(b2, vertex1, vertex2)
    def fonk5(self):
        return nx.diameter(self.b1)
    def fonk6(self):
        return nx.radius(self.b1)
    def fonk7(self):
        for i in range(nx.number_of_nodes(self.b1)):
            for j in range(nx.number_of_nodes(self.b1)):
                if nx.dijkstra_path_length(self.b1, i, j) > 1:
                    return False
        return True
    def fonk8(self):
        pass
if b3 = = '__main__':
    b4 = class1('g0.txt')
    print(b4.fonk7())