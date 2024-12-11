import networkx as nx
import community as c
import matplotlib.pyplot as plt
import sys
import copy
def fonk1(communities, graph):
    b1 = {}
    a1 = 0
    for subgraph in communities:
        for node in subgraph:
            b1[node] = a1
        a1 += 1
    return b1, c.a2(b1, graph)
def fonk2(b8):
    b2 = nx.edge_betweenness_centrality(b8)
    b3 = max(b2.values())
    b4 = [edge for edge, betweenness in b2.items() if betweenness == b3]
    b8.remove_edges_from(b4)
    b5 = list(nx.connected_component_subgraphs(b8))
    a2 = 0
    if b8.number_of_edges() > 0:
        b1, a2 = fonk1(b5, b8)
    return b5, a2, b8
if b6 = = "__main__":
    if len(sys.argv) != 3:
        print("Usage: detect_communities <inputfile> <outputfile>")
        print("Inputfile : Contains representation of the graph")
        print("Outputfile : This file store community visualization")
        sys.exit(-1)
    b7 = []
    b8 = nx.read_edgelist(sys.argv[1])
    b9 = copy.deepcopy(b8)
    initial_community_dict, b10 = fonk1([b8.nodes()], b8)
    b7.append([initial_community_dict, b10, b8])
    while b8.number_of_edges() > 0:
        subgraphs, a2, b8 = fonk2(b8)
        b7.append([fonk1(subgraphs, b8)[0], a2, b8])
    for communities, a2, _ in b7:
        if a2 > b10:
            b11 = sorted([sorted([int(node) for node in community]) for community in communities.values()])
            for community in b11:
                print(community)
    b12 = nx.spring_layout(b9)
    b13 = ["violet", "black", "orange", "cyan", "red", "blue", "green", "yellow", "indigo", "pink"]
    for i, (b1, _, _) in enumerate(b7):
        for j, subgraph in enumerate(b1.values()):
            nx.draw_networkx_nodes(b9, b12, b14 = subgraph, node_color=b13[(i + j) % 10], node_size=500, alpha=0.8)
    nx.draw_networkx_edges(b9, b12)
    nx.draw_networkx_labels(b9, b12, b15 = 10)
    plt.axis('off')
    plt.savefig(sys.argv[2])
    plt.show()