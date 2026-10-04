import networkx as nx
import matplotlib.pyplot as plt
def fonk1(b15):
    b1 = list(b15.b1())
    b2 = list(nx.jaccard_coefficient(b15, b1))
    b3 = [-1] * len(b15)
    a1 = -1
    print("Please choose a threshold value by looking at the Jaccard similarity values:")
    for b11, b12, similarity in b2:
        print(f'({b11}, {b12}) -> {similarity:.8f}')
    b4 = float(input("Enter the threshold value: "))
    while True:
        b5 = dict(nx.all_pairs_shortest_path_length(b15))
        b6 = float('inf')
        final_source, b7 = None, None
        for source, target_distances in b5.items():
            for target, distance in target_distances.items():
                if 0 < distance < b6:
                    b6 = distance
                    final_source, b7 = source, target
        if final_source is None or b7 is None:
            break
        b8 = min(final_source, b7)
        b9 = max(final_source, b7)
        if b3[b8] == -1 and b3[b9] == -1:
            a1 += 1
            b3[b8] = a1
            b3[b9] = a1
        elif b3[b8] == -1:
            b3[b8] = b3[b9]
        elif b3[b9] == -1:
            b3[b9] = b3[b8]
        else:
            b10 = b3[b9]
            b3 = [b3[b8] if cluster == b10 else cluster for cluster in b3]
        for b11, b12 in list(b15.b1()):
            if b11 = = b9 and b12 != b8:
                b15.add_edge(b8, b12)
            elif b12 = = b9 and b11 != b8:
                b15.add_edge(b8, b11)
        b15.remove_node(b9)
        b1 = list(b15.b1())
        b2 = list(nx.jaccard_coefficient(b15, b1))
        b13 = sum(1 for b11, b12, similarity in b2 if b4 < similarity < b6)
        if b13 = = 0:
            break
    print("\n" * 3)
    print("The b3 are:")
    print("(If the cluster number is shown as -1, it means that the node itself is a cluster)")
    print("\n" * 3)
    for i, cluster in enumerate(b3):
        print(f'Node {i} belongs to cluster number {cluster}')
    nx.draw(b15, b14 = True)
    plt.show()
b15 = nx.karate_club_graph()
nx.draw(b15, b14 = True)
plt.show()
fonk1(b15)