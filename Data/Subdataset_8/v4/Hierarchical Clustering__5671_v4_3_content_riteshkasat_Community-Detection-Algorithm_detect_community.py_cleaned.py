import networkx as nx
import community as c
import matplotlib.pyplot as plt
import sys
import copy
def remove_edges(G):
    edge_betweenness = nx.edge_betweenness_centrality(G)
    max_betweenness = max(edge_betweenness.values())
    edges_to_remove = [edge for edge, betweenness in edge_betweenness.items() if betweenness == max_betweenness]
    G.remove_edges_from(edges_to_remove)
    connected_subgraphs = list(nx.connected_component_subgraphs(G))
    community_labels = {}
    counter = 0
    for graph in connected_subgraphs:
        counter += 1
        for node in graph:
            community_labels[node] = counter
    if G.number_of_edges() == 0:
        return [list(nx.connected_component_subgraphs(G)), 0, G]
    modularity = c.modularity(community_labels, G)
    return [list(nx.connected_component_subgraphs(G)), modularity, G]
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: detect_communities <inputfile> <outputfile>")
        print("Inputfile : Contains representation of the graph")
        print("Outputfile : This file stores community visualization")
        sys.exit(-1)
    result_communities = []
    G = nx.read_edgelist(sys.argv[1])
    copy_graph = copy.deepcopy(G)
    community_labels = {}
    for node in G:
        community_labels[node] = 0
    initial_modularity = c.modularity(community_labels, G)
    result_communities.append([community_labels, initial_modularity, G])
    while G.number_of_edges() > 0:
        subgraphs = remove_edges(G)
        result_communities.append(subgraphs)
        G = subgraphs[-1]
    for step in result_communities:
        if step[1] > initial_modularity:
            detected_communities = step[0]
            modularity = step[1]
            sorted_communities = sorted([sorted([int(vertex) for vertex in graph]) for graph in detected_communities])
            for community in sorted_communities:
                print(community)
    community_labels = {}
    counter = 0
    for graph in detected_communities:
        for node in graph:
            community_labels[node] = counter
        counter += 1
    pos = nx.spring_layout(copy_graph)
    colors = ["violet", "black", "orange", "cyan", "red", "blue", "green", "yellow", "indigo", "pink"]
    for i in range(len(detected_communities)):
        graph = detected_communities[i]
        nlist = [node for node in graph]
        nx.draw_networkx_nodes(copy_graph, pos, nodelist=nlist, node_color=colors[i % 10], node_size=500, alpha=0.8)
    nx.draw_networkx_edges(copy_graph, pos)
    nx.draw_networkx_labels(copy_graph, pos, font_size=10)
    plt.axis('off')
    plt.savefig(sys.argv[2])
    plt.show()