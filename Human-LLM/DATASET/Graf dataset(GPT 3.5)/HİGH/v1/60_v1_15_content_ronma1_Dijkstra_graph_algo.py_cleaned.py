import networkx as nx
from Graph import Graph
class class1:
    def fonk1(self, name):
        b1 = Graph(name)
        self.b2 = b1.b2
    def fonk2(self, v1, v2):
        return nx.dijkstra_path_length(self.b2, v1, v2)
    def fonk3(self, v1, v2):
        return nx.dijkstra_path(self.b2, v1, v2)
    def fonk4(self, v1, v2, blacklist):
        for node in blacklist:
            self.b2.remove_node(node)
        return nx.dijkstra_path_length(self.b2, v1, v2)
    def fonk5(self):
        return nx.fonk5(self.b2)
    def fonk6(self):
        return nx.fonk6(self.b2)
    def fonk7(self):
        for i in range(nx.number_of_nodes(self.b2)):
            for j in range(nx.number_of_nodes(self.b2)):
                if nx.dijkstra_path_length(self.b2, i, j) > 1:
                    return False
        return True
    def fonk8(self):
        pass
if b3 = = '__main__':
    b4 = class1('g0.txt')
    print(b4.fonk7())