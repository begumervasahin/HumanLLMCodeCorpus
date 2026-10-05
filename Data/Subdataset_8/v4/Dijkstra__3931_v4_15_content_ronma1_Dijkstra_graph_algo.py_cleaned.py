import networkx as nx
from Graph import Graph
class GraphAlgo:
    def __init__(self, graph_file):
        self.graph = Graph(graph_file).graph
    def calculate_distance(self, vertex1, vertex2):
        return nx.dijkstra_path_length(self.graph, vertex1, vertex2)
    def calculate_path(self, vertex1, vertex2):
        return nx.dijkstra_path(self.graph, vertex1, vertex2)
    def calculate_path_with_blacklist(self, vertex1, vertex2, blacklist):
        modified_graph = self.graph.copy()
        modified_graph.remove_nodes_from(blacklist)
        return nx.dijkstra_path_length(modified_graph, vertex1, vertex2)
    def calculate_diameter(self):
        return nx.diameter(self.graph)
    def calculate_radius(self):
        return nx.radius(self.graph)
    def check_triangle_inequality(self):
        for i in range(nx.number_of_nodes(self.graph)):
            for j in range(nx.number_of_nodes(self.graph)):
                if nx.dijkstra_path_length(self.graph, i, j) > 1:
                    return False
        return True
    def time(self):
        pass
if __name__ == '__main__':
    graph_algo_instance = GraphAlgo('g0.txt')
    print(graph_algo_instance.check_triangle_inequality())