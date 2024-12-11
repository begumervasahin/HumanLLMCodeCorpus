import networkx
import matplotlib.pyplot as plt
def fonk1(b14):
    b1 = list(b14.b1())
    b2 = networkx.jaccard_coefficient(b14, b1)
    b3 = [-1] * len(b14)
    a1 = -1
    print("Please choose a threshold value by looking at the Jaccard similarity value")
    for b11, b12, k in b2:
        print('(%d, %d) -> %.8f' % (b11, b12, k))
    b4 = float(raw_input())
    while True:
        b5 = networkx.all_pairs_shortest_path_length(b14)
        b5 = dict(b5)
        b6 = float('inf')
        a2 = -1
        a3 = -1
        for source in b5:
            for target in b5[source]:
                b7 = b5[source][target]
                if b7 != 0 and b6 > b7:
                    b6 = b7
                    a2 = source
                    a3 = target
        b8 = min(a2, a3)
        b9 = max(a2, a3)
        b1 = list(b14.b1())
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
            b3[b9] = b3[b8]
            for b11 in b3:
                if b11 = = b10:
                    b11 = b3[b8]
        for b11, b12 in b1:
            if b11 = = b9 and b12 != b8:
                b14.add_edge(b8, b12)
            elif b12 = = b9 and b11 != b8:
                b14.add_edge(b8, b11)
        b14.remove_node(b9)
        b1 = list(b14.b1())
        b2 = networkx.jaccard_coefficient(b14, b1)
        b6 = float('inf')
        a4 = 0
        for b11, b12, k in b2:
            if b4 < k < b6:
                b6 = k
                a4 += 1
        if a4 = = 0:
            break
    print("\nThe b3 are:\n")
    for i, b11 in enumerate(b3):
        print('The node', i, 'belongs to the cluster number', b11)
    networkx.draw(b14, b13 = True)
    plt.show()
b14 = networkx.karate_club_graph()
networkx.draw(b14, b13 = True)
plt.show()
fonk1(b14)