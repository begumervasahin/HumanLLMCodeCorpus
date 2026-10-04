import networkx as nx
import community as community_louvain
import matplotlib.pyplot as plt
import sys
import copy
def remove_edges_with_highest_betweenness(G):
    betweenness = nx.edge_betweenness_centrality(G)
    max_betweenness = max(betweenness.values())
    edges_to_remove = [edge for edge, value in betweenness.items() if value == max_betweenness]
    G.remove_edges_from(edges_to_remove)
    subgraphs = list(nx.connected_components(G))
    partition = {node: idx for idx, component in enumerate(subgraphs) for node in component}
    if G.number_of_edges() == 0:
        return subgraphs, 0, G
    modularity = community_louvain.modularity(partition, G)
    return subgraphs, modularity, G
def detect_communities(input_file, output_file):
    G = nx.read_edgelist(input_file)
    original_graph = copy.deepcopy(G)
    partition = {node: 0 for node in G}
    initial_modularity = community_louvain.modularity(partition, G)
    community_history = [(partition, initial_modularity, G)]
    while G.number_of_edges() > 0:
        subgraphs, modularity, G = remove_edges_with_highest_betweenness(G)
        community_history.append((subgraphs, modularity, G))
    best_partition = max(community_history, key=lambda x: x[1])[0]
    print_communities(best_partition)
    visualize_communities(original_graph, best_partition, output_file)
def print_communities(communities):
    sorted_communities = [sorted(community) for community in communities]
    for community in sorted_communities:
        print(community)
def visualize_communities(G, communities, output_file):
    pos = nx.spring_layout(G)
    colors = ["violet", "black", "orange", "cyan", "red", "blue", "green", "yellow", "indigo", "pink"]
    for i, community in enumerate(communities):
        nx.draw_networkx_nodes(
            G, pos, nodelist=list(community),
            node_color=colors[i % len(colors)], node_size=500, alpha=0.8
        )
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos, font_size=10)
    plt.axis('off')
    plt.savefig(output_file)
    plt.show()
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python detect_communities.py <inputfile> <outputfile>")
        sys.exit(-1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    detect_communities(input_file, output_file)