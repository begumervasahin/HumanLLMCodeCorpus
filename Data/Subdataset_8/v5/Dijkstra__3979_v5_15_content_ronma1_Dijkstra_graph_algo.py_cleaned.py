import networkx as nx
from Graph import Graph
class GraphAlgo:
    def __init__(self, graph_file):
        self.graph = Graph(graph_file).graph
    def calculate_distance(self, source, target):
        return nx.dijkstra_path_length(self.graph, source, target)
    def calculate_path(self, source, target):
        return nx.dijkstra_path(self.graph, source, target)
    def calculate_path_with_blacklist(self, source, target, blacklist):
        modified_graph = self.graph.copy()
        modified_graph.remove_nodes_from(blacklist)
        return nx.dijkstra_path_length(modified_graph, source, target)
    def calculate_diameter(self):
        return nx.diameter(self.graph)
    def calculate_radius(self):
        return nx.radius(self.graph)
    def check_triangle_inequality(self):
        for vertex1 in self.graph.nodes:
            for vertex2 in self.graph.nodes:
                if nx.dijkstra_path_length(self.graph, vertex1, vertex2) > 1:
                    return False
        return True
    def time(self):
        pass
if __name__ == '__main__':
    graph_algo_instance = GraphAlgo('g0.txt')
    print(graph_algo_instance.check_triangle_inequality())