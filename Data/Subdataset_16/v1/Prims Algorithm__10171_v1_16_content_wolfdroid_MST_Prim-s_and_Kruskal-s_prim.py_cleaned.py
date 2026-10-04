import matplotlib.pyplot as plt
import networkx as nx
import sys
def fonk1(b15):
    b1 = []
    b2 = []
    b3 = []
    b4 = [0, 1, b15[0][1]]
    a1 = 0
    b5 = len(b15)
    for V in range(b5 - 1):
        b2.append(a1)
        for u in range(b5):
            if b15[a1][u] != 0:
                b3.append([a1, u, b15[a1][u]])
        for e in range(1, len(b3)):
            if b3[e][2] < b4[2] and b3[e][1] not in b2:
                b4 = b3[e]
        b1.append(b4)
        a1 = b4[1]
        b3.remove(b4)
        if b3:
            b4 = b3[0]
    return b1
def fonk2(b1, b14):
    b6 = nx.Graph()
    for edge in b1:
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
            b13 = line.strip().split(' ')
            b12.add(b13[0])
            b12.add(b13[1])
    b14 = list(b12)
    b5 = len(b12)
    b15 = [[0 for _ in range(b5)] for _ in range(b5)]
    with open(file_name) as f:
        for line in f:
            b13 = line.strip().split(' ')
            i, j, b7 = b14.index(b13[0]), b14.index(b13[1]), int(b13[2])
            b15[i][j] = b7
            b15[j][i] = b7
    b1 = fonk1(b15)
    b16 = sum(edge[2] for edge in b1)
    print("The minimum spanning tree:")
    for edge in b1:
        print(f"{b14[edge[0]]} to {b14[edge[1]]} = {edge[2]} units")
    print(f"Total b7: {b16} units")
    fonk2(b1, b14)
if b17 = = "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
    else:
        fonk3(sys.argv[1])