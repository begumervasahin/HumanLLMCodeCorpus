import networkx as nx
import matplotlib.pyplot as plt
def hierarchical_clustering(G):
    edges = list(G.edges())
    jaccard_similarities = nx.jaccard_coefficient(G, edges)
    clusters = [-1] * len(G)
    cluster_number = -1
    print("Please choose a threshold value by looking at the Jaccard similarity values:")
    for u, v, similarity in jaccard_similarities:
        print(f'({u}, {v}) -> {similarity:.8f}')
    threshold_value = float(input("Enter the threshold value: "))
    while True:
        shortest_paths = dict(nx.all_pairs_shortest_path_length(G))
        min_distance = float('inf')
        final_source = final_target = None
        for source in shortest_paths:
            for target, distance in shortest_paths[source].items():
                if distance != 0 and distance < min_distance:
                    min_distance = distance
                    final_source, final_target = source, target
        if final_source is None or final_target is None:
            break
        min_node = min(final_source, final_target)
        max_node = max(final_source, final_target)
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
            for i in range(len(clusters)):
                if clusters[i] == max_cluster:
                    clusters[i] = clusters[min_node]
        for u, v in list(G.edges()):
            if u == max_node and v != min_node:
                G.add_edge(min_node, v)
            elif v == max_node and u != min_node:
                G.add_edge(min_node, u)
        G.remove_node(max_node)
        edges = list(G.edges())
        jaccard_similarities = nx.jaccard_coefficient(G, edges)
        num_edges_above_threshold = 0
        for u, v, similarity in jaccard_similarities:
            if threshold_value < similarity < min_distance:
                num_edges_above_threshold += 1
        if num_edges_above_threshold == 0:
            break
    print("\n" * 3)
    print("The clusters are:")
    print("(If the cluster number is shown as -1, it means that the node itself is a cluster)")
    print("\n" * 3)
    for i, cluster in enumerate(clusters):
        print(f'Node {i} belongs to cluster number {cluster}')
    nx.draw(G, with_labels=True)
    plt.show()
G = nx.karate_club_graph()
nx.draw(G, with_labels=True)
plt.show()
hierarchical_clustering(G)