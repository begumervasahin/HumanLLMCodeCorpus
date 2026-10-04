import networkx as nx
import community as community_louvain
import matplotlib.pyplot as plt
import sys
import copy
def fonk1(b8):
    b1 = []
    b2 = nx.edge_betweenness_centrality(b8)
    b3 = max(b2.values())
    for edge, b4 in b2.items():
        if b4 = = b3:
            b1.append(edge)
    b8.remove_edges_from(b1)
    b5 = list(nx.connected_components(b8))
    b6 = {node: idx for idx, component in enumerate(b5) for node in component}
    if b8.number_of_edges() == 0:
        return [list(nx.connected_components(b8)), 0, b8]
    b7 = community_louvain.b7(b6, b8)
    return [list(nx.connected_components(b8)), b7, b8]
def fonk2(b22, b23):
    b8 = nx.read_edgelist(b22)
    b9 = copy.deepcopy(b8)
    b6 = {node: 0 for node in b8}
    b10 = community_louvain.b7(b6, b8)
    b11 = [[b6, b10, b8]]
    while b8.number_of_edges() > 0:
        b12 = fonk1(b8)
        b11.append(b12)
        b8 = b12[-1]
    b13 = None
    b14 = b10
    for step in b11:
        if step[1] > b14:
            b13 = step[0]
            b14 = step[1]
    b15 = []
    for community in b13:
        b15.append(sorted([int(node) for node in community]))
    for community in b15:
        print(community)
    b16 = nx.spring_layout(b9)
    b17 = ["violet", "black", "orange", "cyan", "red", "blue", "green", "yellow", "indigo", "pink"]
    for i, community in enumerate(b13):
        nx.draw_networkx_nodes(
            b9, b16, b18 = list(community),
            b19 = b17[i % len(b17)], node_size=500, alpha=0.8
        )
    nx.draw_networkx_edges(b9, b16)
    nx.draw_networkx_labels(b9, b16, b20 = 10)
    plt.axis('off')
    plt.savefig(b23)
    plt.show()
if b21 = = "__main__":
    if len(sys.argv) != 3:
        print("Usage: python detect_communities.py <inputfile> <outputfile>")
        sys.exit(-1)
    b22 = sys.argv[1]
    b23 = sys.argv[2]
    fonk2(b22, b23)