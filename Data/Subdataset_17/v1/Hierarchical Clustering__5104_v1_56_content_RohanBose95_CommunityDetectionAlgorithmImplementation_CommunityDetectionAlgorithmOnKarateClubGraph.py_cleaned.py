import networkx as nx
import matplotlib.pyplot as plt
def hierarchical_clustering(G):
    E = list(G.edges())
    J = nx.jaccard_coefficient(G, E)
    clusters = [-1] * len(G)
    cluster_number = -1
    print("Please choose a threshold value by looking at the Jaccard similarity values:")
    for u, v, k in J:
        print(f'({u}, {v}) -> {k:.8f}')
    threshold_value = float(input("Enter the threshold value: "))
    while True:
        length = dict(nx.all_pairs_shortest_path_length(G))
        value = float('inf')
        final_s = -1
        final_t = -1
        for source in length:
            for target in length[source]:
                val = length[source][target]
                if val != 0 and val < value:
                    value = val
                    final_s = source
                    final_t = target
        min_node = min(final_s, final_t)
        max_node = max(final_s, final_t)
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
            for i in range(len(clusters)):
                if clusters[i] == cluster_max_node_belongs_to:
                    clusters[i] = clusters[min_node]
        for u, v in list(G.edges()):
            if u == max_node and v != min_node:
                G.add_edge(min_node, v)
            elif v == max_node and u != min_node:
                G.add_edge(min_node, u)
        G.remove_node(max_node)
        E = list(G.edges())
        J = nx.jaccard_coefficient(G, E)
        value = float('inf')
        num = 0
        for u, v, k in J:
            if k > threshold_value and k < value:
                value = k
                num += 1
        if num == 0:
            break
    print("\n" * 3)
    print("The clusters are:")
    print("\n(If the cluster number is shown as -1, then it means that the node itself is a cluster)")
    print("\n" * 3)
    for i, cluster in enumerate(clusters):
        print(f'The node {i} belongs to the cluster number {cluster}')
    nx.draw(G, with_labels=True)
    plt.show()
G = nx.karate_club_graph()
nx.draw(G, with_labels=True)
plt.show()
hierarchical_clustering(G)