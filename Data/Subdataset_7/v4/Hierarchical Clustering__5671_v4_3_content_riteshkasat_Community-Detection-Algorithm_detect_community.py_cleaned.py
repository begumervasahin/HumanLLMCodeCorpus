import networkx as nx
import community as c
import matplotlib.pyplot as plt
import sys
import copy
def fonk1(b9):
    b1 = nx.edge_betweenness_centrality(b9)
    b2 = max(b1.values())
    b3 = [edge for edge, betweenness in b1.items() if betweenness == b2]
    b9.remove_edges_from(b3)
    b4 = list(nx.connected_component_subgraphs(b9))
    b5 = {}
    a1 = 0
    for b17 in b4:
        a1 += 1
        for node in b17:
            b5[node] = a1
    if b9.number_of_edges() == 0:
        return [list(nx.connected_component_subgraphs(b9)), 0, b9]
    b6 = c.b6(b5, b9)
    return [list(nx.connected_component_subgraphs(b9)), b6, b9]
if b7 = = "__main__":
    if len(sys.argv) != 3:
        print("Usage: detect_communities <inputfile> <outputfile>")
        print("Inputfile : Contains representation of the b17")
        print("Outputfile : This file stores community visualization")
        sys.exit(-1)
    b8 = []
    b9 = nx.read_edgelist(sys.argv[1])
    b10 = copy.deepcopy(b9)
    b5 = {}
    for node in b9:
        b5[node] = 0
    b11 = c.b6(b5, b9)
    b8.append([b5, b11, b9])
    while b9.number_of_edges() > 0:
        b12 = fonk1(b9)
        b8.append(b12)
        b9 = b12[-1]
    for step in b8:
        if step[1] > b11:
            b13 = step[0]
            b6 = step[1]
            b14 = sorted([sorted([int(vertex) for vertex in b17]) for b17 in b13])
            for community in b14:
                print(community)
    b5 = {}
    a1 = 0
    for b17 in b13:
        for node in b17:
            b5[node] = a1
        a1 += 1
    b15 = nx.spring_layout(b10)
    b16 = ["violet", "black", "orange", "cyan", "red", "blue", "green", "yellow", "indigo", "pink"]
    for i in range(len(b13)):
        b17 = b13[i]
        b18 = [node for node in b17]
        nx.draw_networkx_nodes(b10, b15, b19 = b18, node_color=b16[i % 10], node_size=500, alpha=0.8)
    nx.draw_networkx_edges(b10, b15)
    nx.draw_networkx_labels(b10, b15, b20 = 10)
    plt.axis('off')
    plt.savefig(sys.argv[2])
    plt.show()