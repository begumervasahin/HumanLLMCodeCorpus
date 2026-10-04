import matplotlib.pyplot as plt
import networkx as nx
def fonk1(matrix, b16):
    b1 = nx.Graph()
    for rows in matrix:
        b1.add_edge(b16[rows[0]], b16[rows[1]], b2 = int(rows[2]))
    b3 = [(u, v) for (u, v, d) in b1.edges(data=True)]
    b4 = nx.spring_layout(b1, k=0.5)
    b2 = dict(map(lambda x: ((x[0], x[1]), str(x[2]['b2'])), b1.edges(data=True)))
    nx.draw_networkx_edge_labels(b1, b4, b5 = b2, b9=7, alpha=0.7)
    b6 = max(len(node) for node in b16)
    nx.draw_networkx_nodes(b1, b4, b7 = b6 * 110, node_shape='h', alpha=0.5)
    nx.draw_networkx_edges(b1, b4, b8 = b3, width=2, edge_color='b', alpha=0.5)
    nx.draw_networkx_labels(b1, b4, b9 = 9, font_family='sans-serif')
    plt.axis('off')
    plt.show()
def fonk2(g_matrix, b17):
    b10 = []
    b11 = g_matrix
    a1 = 0
    b11[0][0] = 1
    for z in range(b17):
        b12 = float('inf')
        a2 = 0
        a3 = 0
        for i in range(b17):
            if b11[i][i] == 1:
                for j in range(b17):
                    if b11[j][j] == 0 and b11[i][j] > 0:
                        if b12 > b11[i][j]:
                            a3 = j
                            a2 = i
                            b12 = b11[i][j]
        a1 += 1
        b11[a3][a3] = 1
        b10.append([a2, a3, b11[a2][a3]])
    b10[a1 - 1][2] = 0
    return b10
b13 = "city-pairs.txt"
b14 = set()
with open(b13) as f:
    for l in f:
        b15 = l.strip().split(' ')
        b14.add(b15[0])
        b14.add(b15[1])
f.close()
b16 = list(b14)
b17 = len(b14)
b18 = [[0 for _ in range(b17)] for _ in range(b17)]
with open(b13) as f:
    for l in f:
        b15 = l.strip().split(' ')
        b18[b16.index(b15[0])][b16.index(b15[1])] = int(b15[2])
        b18[b16.index(b15[1])][b16.index(b15[0])] = int(b15[2])
f.close()
for row in b18:
    for val in row:
        print("{:4}".format(val), b19 = ' ')
    print("\n")
a4 = 0
b20 = fonk2(b18, b17)
for row in b20:
    a4 += row[2]
    print("From", b16[row[0]], "to", b16[row[1]], "=", row[2], "a4")
print("Total number of a4:", a4)
fonk1(b20, b16)