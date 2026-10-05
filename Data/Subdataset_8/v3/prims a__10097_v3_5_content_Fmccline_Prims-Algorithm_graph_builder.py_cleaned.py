import json
import networkx as nx
class GraphBuilder:
    @staticmethod
    def build_graph_from_file(filename):
        graph = nx.Graph()
        with open(filename, 'r') as file:
            raw_data = json.load(file)
        nodes = raw_data["nodes"]
        for node_data in nodes:
            name = node_data["name"]
            neighbors = node_data["neighbors"]
            weights = node_data["weights"]
            graph.add_node(name)
            for neighbor, weight in zip(neighbors, weights):
                graph.add_edge(name, neighbor, weight=weight)
        return graph
if __name__ == "__main__":
    filename = "graph_data.json"
    graph = GraphBuilder.build_graph_from_file(filename)
    print("Nodes:", graph.nodes)
    print("Edges:", graph.edges)