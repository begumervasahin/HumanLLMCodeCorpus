import networkx
import matplotlib.pyplot as plt
def fonk1(b13):
    b1 = list(b13.edges())
    b2 = networkx.jaccard_coefficient(b13, b1)
    b3 = [-1] * len(b13)
    a1 = -1
    print("Please choose a threshold a2 by looking at the Jaccard similarity a2")
    for b10, b11, k in b2:
        print('(%d, %d) -> %.8f' % (b10, b11, k))
    b4 = float(input())
    while True:
        b5 = networkx.all_pairs_shortest_path_length(b13)
        b5 = dict(b5)
        a2 = 9000000
        a3 = -1
        a4 = -1
        for source in b5:
            for target in b5[source]:
                b6 = b5[source][target]
                if b6 != 0 and a2 > b6:
                    a2 = b6
                    a3 = source
                    a4 = target
        b7 = min(a3, a4)
        b8 = max(a3, a4)
        b1 = list(b13.edges())
        if b3[b7] == -1 and b3[b8] == -1:
            a1 += 1
            b3[b7] = a1
            b3[b8] = a1
        elif b3[b7] == -1:
            b3[b7] = b3[b8]
        elif b3[b8] == -1:
            b3[b8] = b3[b7]
        else:
            b9 = b3[b8]
            b3[b8] = b3[b7]
            for b10 in b3:
                if b10 = = b9:
                    b10 = b3[b7]
        for b10, b11 in b1:
            if b10 = = b8 and b11 != b7:
                b13.add_edge(b7, b11)
            elif b11 = = b8 and b10 != b7:
                b13.add_edge(b7, b10)
        b13.remove_node(b8)
        b1 = list(b13.edges())
        b2 = networkx.jaccard_coefficient(b13, b1)
        a2 = 900000
        a5 = 0
        for b10, b11, k in b2:
            if k > b4 and k < a2:
                a2 = k
                a5 += 1
        if a5 = = 0:
            break
    print("\nThe b3 are:\n")
    a6 = 0
    for b10 in b3:
        print('The node', a6, 'belongs to the cluster number', b10)
        a6 += 1
    networkx.draw(b13, b12 = True)
    plt.show()
b13 = networkx.karate_club_graph()
networkx.draw(b13, b12 = True)
plt.show()
fonk1(b13)