import networkx as nx
import community as c
import matplotlib.pyplot as plt
import sys
import copy
def fonk1(b10):
    b1 = nx.edge_betweenness_centrality(b10)
    b2 = max(b1.values())
    b3 = [edge for edge, betweenness in b1.items() if betweenness == b2]
    b10.remove_edges_from(b3)
    b4 = list(nx.connected_component_subgraphs(b10))
    b5 = {}
    for idx, graph in enumerate(b4, b6 = 1):
        for node in graph:
            b5[node] = idx
    if b10.number_of_edges() == 0:
        return [list(nx.connected_component_subgraphs(b10)), 0, b10]
    b7 = c.b7(b5, b10)
    return [list(nx.connected_component_subgraphs(b10)), b7, b10]
if b8 = = "__main__":
    if len(sys.argv) != 3:
        print("Usage: detect_communities <inputfile> <outputfile>")
        print("Inputfile: Contains representation of the graph")
        print("Outputfile: This file stores community visualization")
        sys.exit(-1)
    b9 = []
    b10 = nx.read_edgelist(sys.argv[1])
    b11 = copy.deepcopy(b10)
    b5 = {node: 0 for node in b10}
    b12 = c.b7(b5, b10)
    b9.append([b5, b12, b10])
    while b10.number_of_edges() > 0:
        b13 = fonk1(b10)
        b9.append(b13)
        b10 = b13[-1]
    for step in b9:
        if step[1] > b12:
            b14 = step[0]
            b15 = sorted([sorted(map(int, graph)) for graph in b14])
            for community in b15:
                print(community)
    b5 = {}
    for idx, graph in enumerate(b14, b6 = 1):
        for node in graph:
            b5[node] = idx
    b16 = nx.spring_layout(b11)
    b17 = ["violet", "black", "orange", "cyan", "red", "blue", "green", "yellow", "indigo", "pink"]
    for i, graph in enumerate(b14):
        b18 = list(graph)
        nx.draw_networkx_nodes(b11, b16, b19 = b18, node_color=b17[i % len(b17)], node_size=500, alpha=0.8)
    nx.draw_networkx_edges(b11, b16)
    nx.draw_networkx_labels(b11, b16, b20 = 10)
    plt.axis('off')
    plt.savefig(sys.argv[2])
    plt.show()