import matplotlib.pyplot as plt
import networkx as nx
import sys
def fonk1(b16):
    b1 = len(b16)
    b2 = []
    b3 = [False] * b1
    b4 = []
    b3[0] = True
    for i in range(b1):
        if b16[0][i] != 0:
            b4.append((0, i, b16[0][i]))
    while len(b2) < b1 - 1:
        b4.sort(b5 = lambda x: x[2])
        for edge in b4:
            if not b3[edge[1]]:
                b2.append(edge)
                b6 = edge[1]
                b3[b6] = True
                break
        b4 = [edge for edge in b4 if not (b3[edge[0]] and b3[edge[1]])]
        for i in range(b1):
            if b16[b6][i] != 0 and not b3[i]:
                b4.append((b6, i, b16[b6][i]))
    return b2
def fonk2(b2, b15):
    b7 = nx.Graph()
    for edge in b2:
        b7.add_edge(b15[edge[0]], b15[edge[1]], b8 = edge[2])
    b9 = nx.spring_layout(b7)
    b10 = nx.get_edge_attributes(b7, 'b8')
    nx.draw(b7, b9, b11 = True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(b7, b9, b12 = b10)
    plt.show()
def fonk3(file_name):
    b13 = set()
    with open(file_name) as f:
        for line in f:
            u, b6, b14 = line.strip().split()
            b13.add(u)
            b13.add(b6)
    b15 = list(b13)
    b1 = len(b15)
    b16 = [[0] * b1 for b14 in range(b1)]
    with open(file_name) as f:
        for line in f:
            u, b6, b8 = line.strip().split()
            i, b17 = b15.index(u), b15.index(b6)
            b16[i][b17] = int(b8)
            b16[b17][i] = int(b8)
    return b15, b16
def fonk4(file_name):
    b15, b16 = fonk3(file_name)
    b2 = fonk1(b16)
    b18 = sum(edge[2] for edge in b2)
    print("The minimum spanning tree:")
    for edge in b2:
        print(f"{b15[edge[0]]} to {b15[edge[1]]} = {edge[2]} units")
    print(f"Total b8: {b18} units")
    fonk2(b2, b15)
if b19 = = "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
    else:
        fonk4(sys.argv[1])