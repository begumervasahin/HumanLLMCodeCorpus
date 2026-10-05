import json
import networkx as nx
class GraphBuilder:
    @staticmethod
    def build_graph_from_file(filename):
        graph = nx.Graph()
        with open(filename, 'r') as file:
            raw_data = json.load(file)
        nodes_data = raw_data.get("nodes", [])
        for node_data in nodes_data:
            node_name = node_data.get("name")
            neighbors = node_data.get("neighbors", [])
            weights = node_data.get("weights", [])
            for neighbor, weight in zip(neighbors, weights):
                graph.add_node(node_name)
                graph.add_edge(node_name, neighbor, weight=weight)
        return graph
