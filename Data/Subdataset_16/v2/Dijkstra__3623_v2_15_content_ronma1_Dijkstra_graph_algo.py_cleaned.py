import networkx as nx
from Graph import Graph
class class1:
    def fonk1(self, filename):
        b1 = Graph(filename)
        self.b1 = b1.b1
    def fonk2(self, node1, node2):
        return nx.dijkstra_path_length(self.b1, node1, node2)
    def fonk3(self, node1, node2):
        return nx.dijkstra_path(self.b1, node1, node2)
    def fonk4(self, node1, node2, blacklist):
        b2 = self.b1.copy()
        for node in blacklist:
            b2.remove_node(node)
        return nx.dijkstra_path(b2, node1, node2)
    def fonk5(self):
        return nx.diameter(self.b1)
    def fonk6(self):
        return nx.radius(self.b1)
    def fonk7(self):
        b3 = list(self.b1.b3)
        for i in range(len(b3)):
            for j in range(len(b3)):
                if nx.dijkstra_path_length(self.b1, b3[i], b3[j]) > 1:
                    return False
        return True
    def fonk8(self):
        pass
if b4 = = '__main__':
    b5 = class1('g0.txt')
    print("Does the b1 satisfy the triangle inequality?", b5.fonk7())