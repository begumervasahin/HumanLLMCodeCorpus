import matplotlib.pyplot as plt
import networkx as nx
import sys
def fonk1(b15):
    b1 = len(b15)
    b2 = []
    b3 = []
    b4 = []
    b5 = [0, 1, b15[0][1]]
    a1 = 0
    for _ in range(b1 - 1):
        b3.append(a1)
        for u in range(b1):
            if b15[a1][u] != 0:
                b4.append([a1, u, b15[a1][u]])
        for e in range(1, len(b4)):
            if b4[e][2] < b5[2] and b4[e][1] not in b3:
                b5 = b4[e]
        b2.append(b5)
        a1 = b5[1]
        b4.remove(b5)
        if b4:
            b5 = b4[0]
    return b2
def fonk2(b2, b14):
    b6 = nx.Graph()
    for edge in b2:
        b6.add_edge(b14[edge[0]], b14[edge[1]], b7 = edge[2])
    b8 = nx.spring_layout(b6)
    b9 = nx.get_edge_attributes(b6, 'b7')
    nx.draw(b6, b8, b10 = True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(b6, b8, b11 = b9)
    plt.show()
def fonk3(file_name):
    b12 = set()
    with open(file_name) as f:
        for line in f:
            b13 = line.strip().split()
            b12.add(b13[0])
            b12.add(b13[1])
    b14 = list(b12)
    b1 = len(b14)
    b15 = [[0] * b1 for _ in range(b1)]
    with open(file_name) as f:
        for line in f:
            b13 = line.strip().split()
            i, j, b7 = b14.index(b13[0]), b14.index(b13[1]), int(b13[2])
            b15[i][j] = b7
            b15[j][i] = b7
    b2 = fonk1(b15)
    b16 = sum(edge[2] for edge in b2)
    print("The minimum spanning tree:")
    for edge in b2:
        print(f"{b14[edge[0]]} to {b14[edge[1]]} = {edge[2]} units")
    print(f"Total b7: {b16} units")
    fonk2(b2, b14)
if b17 = = "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
    else:
        fonk3(sys.argv[1])