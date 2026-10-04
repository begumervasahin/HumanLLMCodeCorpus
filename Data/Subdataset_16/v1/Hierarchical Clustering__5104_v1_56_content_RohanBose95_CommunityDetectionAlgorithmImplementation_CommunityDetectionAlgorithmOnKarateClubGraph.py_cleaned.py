import networkx as nx
import matplotlib.pyplot as plt
def fonk1(b14):
    b1 = list(b14.edges())
    b2 = nx.jaccard_coefficient(b14, b1)
    b3 = [-1] * len(b14)
    a1 = -1
    print("Please choose a threshold b6 by looking at the Jaccard similarity values:")
    for b11, b12, k in b2:
        print(f'({b11}, {b12}) -> {k:.8f}')
    b4 = float(input("Enter the threshold b6: "))
    while True:
        b5 = dict(nx.all_pairs_shortest_path_length(b14))
        b6 = float('inf')
        a2 = -1
        a3 = -1
        for source in b5:
            for target in b5[source]:
                b7 = b5[source][target]
                if b7 != 0 and b7 < b6:
                    b6 = b7
                    a2 = source
                    a3 = target
        b8 = min(a2, a3)
        b9 = max(a2, a3)
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
            for i in range(len(b3)):
                if b3[i] == b10:
                    b3[i] = b3[b8]
        for b11, b12 in list(b14.edges()):
            if b11 = = b9 and b12 != b8:
                b14.add_edge(b8, b12)
            elif b12 = = b9 and b11 != b8:
                b14.add_edge(b8, b11)
        b14.remove_node(b9)
        b1 = list(b14.edges())
        b2 = nx.jaccard_coefficient(b14, b1)
        b6 = float('inf')
        a4 = 0
        for b11, b12, k in b2:
            if k > b4 and k < b6:
                b6 = k
                a4 += 1
        if a4 = = 0:
            break
    print("\n" * 3)
    print("The b3 are:")
    print("\n(If the cluster number is shown as -1, then it means that the node itself is a cluster)")
    print("\n" * 3)
    for i, cluster in enumerate(b3):
        print(f'The node {i} belongs to the cluster number {cluster}')
    nx.draw(b14, b13 = True)
    plt.show()
b14 = nx.karate_club_graph()
nx.draw(b14, b13 = True)
plt.show()
fonk1(b14)