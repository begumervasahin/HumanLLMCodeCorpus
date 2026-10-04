import networkx as nx
import community as community_louvain
import matplotlib.pyplot as plt
import sys
import copy
def fonk1(b7):
    b1 = nx.edge_betweenness_centrality(b7)
    b2 = max(b1.values())
    b3 = [edge for edge, value in b1.items() if value == b2]
    b7.remove_edges_from(b3)
    b4 = list(nx.connected_components(b7))
    b5 = {node: idx for idx, component in enumerate(b4) for node in component}
    if b7.number_of_edges() == 0:
        return b4, 0, b7
    b6 = community_louvain.b6(b5, b7)
    return b4, b6, b7
def fonk2(b19, b20):
    b7 = nx.read_edgelist(b19)
    b8 = copy.deepcopy(b7)
    b5 = {node: 0 for node in b7}
    b9 = community_louvain.b6(b5, b7)
    b10 = [(b5, b9, b7)]
    while b7.number_of_edges() > 0:
        b4, b6, b7 = fonk1(b7)
        b10.append((b4, b6, b7))
    b11 = max(b10, key=lambda x: x[1])[0]
    b12 = [sorted(community) for community in b11]
    for community in b12:
        print(community)
    fonk3(b8, b11, b20)
def fonk3(b7, b12, b20):
    b13 = nx.spring_layout(b7)
    b14 = ["violet", "black", "orange", "cyan", "red", "blue", "green", "yellow", "indigo", "pink"]
    for i, community in enumerate(b12):
        nx.draw_networkx_nodes(
            b7, b13, b15 = list(community),
            b16 = b14[i % len(b14)], node_size=500, alpha=0.8
        )
    nx.draw_networkx_edges(b7, b13)
    nx.draw_networkx_labels(b7, b13, b17 = 10)
    plt.axis('off')
    plt.savefig(b20)
    plt.show()
if b18 = = "__main__":
    if len(sys.argv) != 3:
        print("Usage: python detect_communities.py <inputfile> <outputfile>")
        sys.exit(-1)
    b19 = sys.argv[1]
    b20 = sys.argv[2]
    fonk2(b19, b20)