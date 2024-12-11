import json
import networkx as nx
class class1:
    @staticmethod
    def fonk1(filename):
        b1 = nx.Graph()
        with open(filename, 'r') as file:
            b2 = json.load(file)
        b3 = b2.get("nodes", [])
        for node_data in b3:
            b4 = node_data.get("name")
            b5 = node_data.get("b5", [])
            b6 = node_data.get("b6", [])
            for neighbor, b7 in zip(b5, b6):
                b1.add_node(b4)
                b1.add_edge(b4, neighbor, b7 = b7)
        return b1
