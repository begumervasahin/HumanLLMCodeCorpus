import networkx as nx
from Graph import Graph
class GraphAlgo:
    def __init__(self, name):
        graph_loader = Graph(name)
        self.graph = graph_loader.graph
    def calculate_distance(self, vertex1, vertex2):
        return nx.dijkstra_path_length(self.graph, vertex1, vertex2)
    def find_shortest_path(self, start_vertex, end_vertex):
        return nx.dijkstra_path(self.graph, start_vertex, end_vertex)
    def calculate_path_with_blacklist(self, start_vertex, end_vertex, blacklist):
        modified_graph = self.graph.copy()
        modified_graph.remove_nodes_from(blacklist)
        return nx.dijkstra_path_length(modified_graph, start_vertex, end_vertex)
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