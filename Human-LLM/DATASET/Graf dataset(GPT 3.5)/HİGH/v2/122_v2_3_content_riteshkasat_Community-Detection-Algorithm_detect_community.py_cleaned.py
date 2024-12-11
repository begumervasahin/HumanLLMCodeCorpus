import networkx as nx
import community as c
import matplotlib.pyplot as plt
import sys
import copy
def fonk1(b10):
    b1 = nx.edge_betweenness_centrality(b10)
    b2 = max(b1.values())
    b3 = []
    for k, b4 in b1.items():
        if b4 = = b2:
            b3.append(k)
    b10.remove_edges_from(b3)
    b5 = list(nx.connected_component_subgraphs(b10))
    b6 = {}
    a1 = 0
    for b18 in b5:
        a1 += 1
        for node in b18:
            b6[node] = a1
    if b10.number_of_edges() == 0:
        return [list(nx.connected_component_subgraphs(b10)), 0, b10]
    b7 = c.b7(b6, b10)
    return [list(nx.connected_component_subgraphs(b10)), b7, b10]
if b8 = = "__main__":
    if len(sys.argv) != 3:
        print("Usage: detect_communities <inputfile> <outputfile>")
        print("Inputfile : Contains representation of the b18")
        print("Outputfile : This file store community visualization")
        sys.exit(-1)
    b9 = []
    b10 = nx.read_edgelist(sys.argv[1])
    b11 = copy.deepcopy(b10)
    b6 = {node: 0 for node in b10}
    b12 = c.b7(b6, b10)
    b9.append([b6, b12, b10])
    while b10.number_of_edges() > 0:
        b13 = fonk1(b10)
        b9.append(b13)
        b10 = b13[-1]
    for step in b9:
        if step[1] > b12:
            b14 = step[0]
            b15 = []
            b7 = step[1]
            for b18 in step[0]:
                b15.append(sorted([int(vertex) for vertex in b18]))
            for community in b15:
                print(community)
    b6 = {}
    a1 = 0
    for b18 in b14:
        for node in b18:
            b6[node] = a1
        a1 += 1
    b16 = nx.spring_layout(b11)
    b17 = ["violet", "black", "orange", "cyan", "red", "blue", "green", "yellow", "indigo", "pink"]
    for i in range(len(b14)):
        b18 = b14[i]
        b19 = [node for node in b18]
        nx.draw_networkx_nodes(b11, b16, b20 = b19, node_color=b17[i % 10], node_size=500, alpha=0.8)
    nx.draw_networkx_edges(b11, b16)
    nx.draw_networkx_labels(b11, b16, b21 = 10)
    plt.axis('off')
    plt.savefig(sys.argv[2])
    plt.show()