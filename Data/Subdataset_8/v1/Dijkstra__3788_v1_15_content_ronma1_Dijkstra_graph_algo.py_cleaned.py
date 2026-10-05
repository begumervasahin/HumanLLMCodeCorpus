import networkx as nx
from Graph import Graph
class GraphAlgo:
    def __init__(self, name):
        g = Graph(name)
        self.graph = g.graph
    def calc_dist(self, v1, v2):
        return nx.dijkstra_path_length(self.graph, v1, v2)
    def calc_path(self, v1, v2):
        return nx.dijkstra_path(self.graph, v1, v2)
    def calc_path_with_blacklist(self, v1, v2, blacklist):
        for node in blacklist:
            self.graph.remove_node(node)
        return nx.dijkstra_path_length(self.graph, v1, v2)
    def diameter(self):
        return nx.diameter(self.graph)
    def radius(self):
        return nx.radius(self.graph)
    def is_triangle_inequality(self):
        for i in range(nx.number_of_nodes(self.graph)):
            for j in range(nx.number_of_nodes(self.graph)):
                if nx.dijkstra_path_length(self.graph, i, j) > 1:
                    return False
        return True
    def time(self):
        pass
if __name__ == '__main__':
    g1 = GraphAlgo('g0.txt')
    print(g1.is_triangle_inequality())