import networkx as nx
from Graph import Graph
class GraphAlgo:
    def __init__(self, filename):
        g = Graph(filename)
        self.graph = g.graph
    def calculate_distance(self, v1, v2):
        return nx.dijkstra_path_length(self.graph, v1, v2)
    def calculate_path(self, v1, v2):
        return nx.dijkstra_path(self.graph, v1, v2)
    def calculate_path_with_blacklist(self, v1, v2, blacklist):
        temp_graph = self.graph.copy()
        for node in blacklist:
            temp_graph.remove_node(node)
        return nx.dijkstra_path(temp_graph, v1, v2)
    def get_diameter(self):
        return nx.diameter(self.graph)
    def get_radius(self):
        return nx.radius(self.graph)
    def satisfies_triangle_inequality(self):
        nodes = list(self.graph.nodes)
        for i in range(len(nodes)):
            for j in range(len(nodes)):
                if nx.dijkstra_path_length(self.graph, nodes[i], nodes[j]) > 1:
                    return False
        return True
    def time(self):
        pass
if __name__ == '__main__':
    graph_algo = GraphAlgo('g0.txt')
    print("Does the graph satisfy the triangle inequality?", graph_algo.satisfies_triangle_inequality())