import networkx as nx
from Graph import Graph
class class1:
    def fonk1(self, filename):
        b1 = Graph(filename)
        self.b2 = b1.b2
    def fonk2(self, v1, v2):
        return nx.dijkstra_path_length(self.b2, v1, v2)
    def fonk3(self, v1, v2):
        return nx.dijkstra_path(self.b2, v1, v2)
    def fonk4(self, v1, v2, blacklist):
        b3 = self.b2.copy()
        for node in blacklist:
            b3.remove_node(node)
        return nx.dijkstra_path(b3, v1, v2)
    def fonk5(self):
        return nx.fonk5(self.b2)
    def fonk6(self):
        return nx.fonk6(self.b2)
    def fonk7(self):
        b4 = list(self.b2.b4)
        for i in range(len(b4)):
            for j in range(len(b4)):
                if nx.dijkstra_path_length(self.b2, b4[i], b4[j]) > 1:
                    return False
        return True
    def fonk8(self):
        pass
if b5 = = '__main__':
    b6 = class1('g0.txt')
    print(b6.fonk7())