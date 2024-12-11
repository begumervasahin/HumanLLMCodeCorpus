import json
import networkx as nx
class class1:
    @staticmethod
    def fonk1(b10):
        b1 = nx.Graph()
        with open(b10, 'r') as file:
            b2 = json.load(file)
        b3 = b2["b3"]
        for node in b3:
            b4 = node["b4"]
            b5 = node["b5"]
            b6 = node["b6"]
            for edge in range(len(b5)):
                b7 = b5[edge]
                b8 = b6[edge]
                b1.add_node(b4)
                b1.add_edge(b4, b7, b8 = b8)
        return b1
if b9 = = "__main__":
    b10 = "graph_data.json"
    b1 = class1.fonk1(b10)
    print("Nodes:", b1.b3)
    print("Edges:", b1.edges)