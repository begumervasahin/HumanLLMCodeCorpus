import networkx as nx
import matplotlib.pyplot as plt
def calculate_jaccard_similarity(G):
    edges = list(G.edges())
    return list(nx.jaccard_coefficient(G, edges))
def find_closest_pair(shortest_paths):
    min_distance = float('inf')
    final_source, final_target = None, None
    for source, target_distances in shortest_paths.items():
        for target, distance in target_distances.items():
            if 0 < distance < min_distance:
                min_distance = distance
                final_source, final_target = source, target
    return final_source, final_target
def merge_clusters(G, clusters, min_node, max_node, cluster_number):
    if clusters[min_node] == -1 and clusters[max_node] == -1:
        cluster_number += 1
        clusters[min_node] = cluster_number
        clusters[max_node] = cluster_number
    elif clusters[min_node] == -1:
        clusters[min_node] = clusters[max_node]
    elif clusters[max_node] == -1:
        clusters[max_node] = clusters[min_node]
    else:
        max_cluster = clusters[max_node]
        clusters = [clusters[min_node] if cluster == max_cluster else cluster for cluster in clusters]
    return clusters, cluster_number
def hierarchical_clustering(G):
    clusters = [-1] * len(G)
    cluster_number = -1
    jaccard_similarities = calculate_jaccard_similarity(G)
    print("Please choose a threshold value by looking at the Jaccard similarity values:")
    for u, v, similarity in jaccard_similarities:
        print(f'({u}, {v}) -> {similarity:.8f}')
    threshold_value = float(input("Enter the threshold value: "))
    while True:
        shortest_paths = dict(nx.all_pairs_shortest_path_length(G))
        final_source, final_target = find_closest_pair(shortest_paths)
        if final_source is None or final_target is None:
            break
        min_node = min(final_source, final_target)
        max_node = max(final_source, final_target)
        clusters, cluster_number = merge_clusters(G, clusters, min_node, max_node, cluster_number)
        for u, v in list(G.edges()):
            if u == max_node and v != min_node:
                G.add_edge(min_node, v)
            elif v == max_node and u != min_node:
                G.add_edge(min_node, u)
        G.remove_node(max_node)
        jaccard_similarities = calculate_jaccard_similarity(G)
        num_edges_above_threshold = sum(1 for u, v, similarity in jaccard_similarities if threshold_value < similarity < float('inf'))
        if num_edges_above_threshold == 0:
            break
    print("\nThe clusters are:")
    print("(If the cluster number is shown as -1, it means that the node itself is a cluster)\n")
    for i, cluster in enumerate(clusters):
        print(f'Node {i} belongs to cluster number {cluster}')
    nx.draw(G, with_labels=True)
    plt.show()
if __name__ == "__main__":
    G = nx.karate_club_graph()
    nx.draw(G, with_labels=True)
    plt.show()
    hierarchical_clustering(G)