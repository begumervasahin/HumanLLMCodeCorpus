import networkx
import matplotlib.pyplot as plt
def hierarchical_clustering(G):
    edges = list(G.edges())
    jaccard_similarities = networkx.jaccard_coefficient(G, edges)
    clusters = [-1] * len(G)
    cluster_number = -1
    print("Please choose a threshold value by looking at the Jaccard similarity value")
    for u, v, k in jaccard_similarities:
        print('(%d, %d) -> %.8f' % (u, v, k))
    threshold_value = float(raw_input())
    while True:
        shortest_paths = networkx.all_pairs_shortest_path_length(G)
        shortest_paths = dict(shortest_paths)
        min_distance = float('inf')
        final_s = -1
        final_t = -1
        for source in shortest_paths:
            for target in shortest_paths[source]:
                distance = shortest_paths[source][target]
                if distance != 0 and min_distance > distance:
                    min_distance = distance
                    final_s = source
                    final_t = target
        min_node = min(final_s, final_t)
        max_node = max(final_s, final_t)
        edges = list(G.edges())
        if clusters[min_node] == -1 and clusters[max_node] == -1:
            cluster_number += 1
            clusters[min_node] = cluster_number
            clusters[max_node] = cluster_number
        elif clusters[min_node] == -1:
            clusters[min_node] = clusters[max_node]
        elif clusters[max_node] == -1:
            clusters[max_node] = clusters[min_node]
        else:
            cluster_max_node_belongs_to = clusters[max_node]
            clusters[max_node] = clusters[min_node]
            for u in clusters:
                if u == cluster_max_node_belongs_to:
                    u = clusters[min_node]
        for u, v in edges:
            if u == max_node and v != min_node:
                G.add_edge(min_node, v)
            elif v == max_node and u != min_node:
                G.add_edge(min_node, u)
        G.remove_node(max_node)
        edges = list(G.edges())
        jaccard_similarities = networkx.jaccard_coefficient(G, edges)
        min_distance = float('inf')
        num = 0
        for u, v, k in jaccard_similarities:
            if threshold_value < k < min_distance:
                min_distance = k
                num += 1
        if num == 0:
            break
    print("\nThe clusters are:\n")
    for i, u in enumerate(clusters):
        print('The node', i, 'belongs to the cluster number', u)
    networkx.draw(G, with_labels=True)
    plt.show()
G = networkx.karate_club_graph()
networkx.draw(G, with_labels=True)
plt.show()
hierarchical_clustering(G)