import matplotlib.pyplot as plt
import networkx as nx
def fonk1(b18):
    b1 = sorted(b18, key=lambda x: x[2])
    return b1
def fonk2(b2, b4):
    while b2 != b4[b2]:
        b2 = b4[b2]
    return b2
def fonk3(b4, b8, b7, b5):
    if b5[b8] > b5[b7]:
        b4[b7] = b8
    elif b5[b8] < b5[b7]:
        b4[b8] = b7
    else:
        b4[b7] = b8
        b5[b8] += 1
def fonk4(b18, b17):
    b3 = []
    b1 = fonk1(b18)
    b4 = list(range(b17))
    b5 = [0] * b17
    a1 = 0
    a2 = 0
    while a1 < (b17 - 1):
        v, u, b6 = b1[a2]
        a2 += 1
        b7 = fonk2(v, b4)
        b8 = fonk2(u, b4)
        if b8 != b7:
            a1 += 1
            b3.append([v, u, b6])
            fonk3(b4, b8, b7, b5)
    return b3
def fonk5(b3, b16, b17):
    b9 = nx.Graph()
    for edge in b3:
        b9.add_edge(b16[edge[0]], b16[edge[1]], b6 = edge[2])
    b10 = nx.spring_layout(b9, a2=20, iterations=150)
    b11 = nx.get_edge_attributes(b9, 'b6')
    nx.draw(b9, b10, b12 = True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(b9, b10, b13 = b11)
    plt.show()
def fonk6(b21):
    b14 = set()
    with open(b21) as f:
        for line in f:
            b15 = line.strip().split(' ')
            b14.add(b15[0])
            b14.add(b15[1])
    b16 = list(b14)
    b17 = len(b14)
    b18 = []
    with open(b21) as f:
        for line in f:
            b15 = line.strip().split(' ')
            b18.append([
                b16.index(b15[0]),
                b16.index(b15[1]),
                int(b15[2])
            ])
    b3 = fonk4(b18, b17)
    b19 = sum(edge[2] for edge in b3)
    print("The minimum spanning tree:")
    for edge in b3:
        print(f"{b16[edge[0]]} to {b16[edge[1]]} = {edge[2]} units.")
    print(f"Total b6: {b19} units.")
    fonk5(b3, b16, b17)
if b20 = = "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)
    b21 = sys.argv[1]
    fonk6(b21)