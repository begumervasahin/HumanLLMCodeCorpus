import json
import networkx as nx
class class1:
    @staticmethod
    def fonk1(b9):
        b1 = nx.Graph()
        with open(b9, 'r') as file:
            b2 = json.load(file)
        b3 = b2["b3"]
        for node_data in b3:
            b4 = node_data["b4"]
            b5 = node_data["b5"]
            b6 = node_data["b6"]
            b1.add_node(b4)
            for neighbor, b7 in zip(b5, b6):
                b1.add_edge(b4, neighbor, b7 = b7)
        return b1
if b8 = = "__main__":
    b9 = "graph_data.json"
    b1 = class1.fonk1(b9)
    print("Nodes:", b1.b3)
    print("Edges:", b1.edges)