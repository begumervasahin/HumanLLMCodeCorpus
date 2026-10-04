import networkx as nx
import matplotlib.pyplot as plt
def fonk1(b16):
    b1 = list(b16.b1())
    return list(nx.jaccard_coefficient(b16, b1))
def fonk2(b8):
    b2 = float('inf')
    final_source, b3 = None, None
    for source, target_distances in b8.items():
        for target, distance in target_distances.items():
            if 0 < distance < b2:
                b2 = distance
                final_source, b3 = source, target
    return final_source, b3
def fonk3(b16, b5, b9, b10, a1):
    if b5[b9] == -1 and b5[b10] == -1:
        a1 += 1
        b5[b9] = a1
        b5[b10] = a1
    elif b5[b9] == -1:
        b5[b9] = b5[b10]
    elif b5[b10] == -1:
        b5[b10] = b5[b9]
    else:
        b4 = b5[b10]
        b5 = [b5[b9] if cluster == b4 else cluster for cluster in b5]
    return b5, a1
def fonk4(b16):
    b5 = [-1] * len(b16)
    a1 = -1
    b6 = fonk1(b16)
    print("Please choose a threshold value by looking at the Jaccard similarity values:")
    for b11, b12, similarity in b6:
        print(f'({b11}, {b12}) -> {similarity:.8f}')
    b7 = float(input("Enter the threshold value: "))
    while True:
        b8 = dict(nx.all_pairs_shortest_path_length(b16))
        final_source, b3 = fonk2(b8)
        if final_source is None or b3 is None:
            break
        b9 = min(final_source, b3)
        b10 = max(final_source, b3)
        b5, a1 = fonk3(b16, b5, b9, b10, a1)
        for b11, b12 in list(b16.b1()):
            if b11 = = b10 and b12 != b9:
                b16.add_edge(b9, b12)
            elif b12 = = b10 and b11 != b9:
                b16.add_edge(b9, b11)
        b16.remove_node(b10)
        b6 = fonk1(b16)
        b13 = sum(1 for b11, b12, similarity in b6 if b7 < similarity < float('inf'))
        if b13 = = 0:
            break
    print("\nThe b5 are:")
    print("(If the cluster number is shown as -1, it means that the node itself is a cluster)\n")
    for i, cluster in enumerate(b5):
        print(f'Node {i} belongs to cluster number {cluster}')
    nx.draw(b16, b14 = True)
    plt.show()
if b15 = = "__main__":
    b16 = nx.karate_club_graph()
    nx.draw(b16, b14 = True)
    plt.show()
    fonk4(b16)