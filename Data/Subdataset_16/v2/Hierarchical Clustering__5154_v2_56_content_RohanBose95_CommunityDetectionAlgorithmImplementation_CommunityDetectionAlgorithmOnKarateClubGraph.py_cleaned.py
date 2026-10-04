import networkx as nx
import matplotlib.pyplot as plt
def fonk1(b15):
    b1 = list(b15.b1())
    b2 = nx.jaccard_coefficient(b15, b1)
    b3 = [-1] * len(b15)
    a1 = -1
    print("Please choose a threshold value by looking at the Jaccard similarity values:")
    for b12, b13, similarity in b2:
        print(f'({b12}, {b13}) -> {similarity:.8f}')
    b4 = float(input("Enter the threshold value: "))
    while True:
        b5 = dict(nx.all_pairs_shortest_path_length(b15))
        b6 = float('inf')
        b7 = b8 = None
        for source in b5:
            for target, distance in b5[source].items():
                if distance != 0 and distance < b6:
                    b6 = distance
                    b7, b8 = source, target
        if b7 is None or b8 is None:
            break
        b9 = min(b7, b8)
        b10 = max(b7, b8)
        if b3[b9] == -1 and b3[b10] == -1:
            a1 += 1
            b3[b9] = a1
            b3[b10] = a1
        elif b3[b9] == -1:
            b3[b9] = b3[b10]
        elif b3[b10] == -1:
            b3[b10] = b3[b9]
        else:
            b11 = b3[b10]
            for i in range(len(b3)):
                if b3[i] == b11:
                    b3[i] = b3[b9]
        for b12, b13 in list(b15.b1()):
            if b12 = = b10 and b13 != b9:
                b15.add_edge(b9, b13)
            elif b13 = = b10 and b12 != b9:
                b15.add_edge(b9, b12)
        b15.remove_node(b10)
        b1 = list(b15.b1())
        b2 = nx.jaccard_coefficient(b15, b1)
        a2 = 0
        for b12, b13, similarity in b2:
            if b4 < similarity < b6:
                a2 += 1
        if a2 = = 0:
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