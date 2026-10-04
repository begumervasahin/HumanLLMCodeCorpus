import matplotlib.pyplot as plt
import networkx as nx
import sys
def fonk1(b9, vert_list):
    b1 = nx.Graph()
    for edge in b9:
        b1.add_edge(vert_list[edge[0]], vert_list[edge[1]], b2 = int(edge[2]))
    b3 = nx.spring_layout(b1, k=20, iterations=150, b2='b2', scale=1.0)
    b4 = {(u, v): str(d['b2']) for u, v, d in b1.b15(data=True)}
    nx.draw_networkx_edge_labels(b1, b3, b4 = b4)
    b5 = max(len(vert_list) * 180, 100)
    nx.draw_networkx_nodes(b1, b3, b5 = b5, node_shape='h', alpha=0.5)
    nx.draw_networkx_edges(b1, b3, b6 = b1.b15, width=2, edge_color='b', alpha=0.5)
    nx.draw_networkx_labels(b1, b3, b7 = 9, font_family='sans-serif')
    plt.axis('off')
    plt.show()
def fonk2(b18):
    return sorted(b18, b8 = lambda x: x[2])
def fonk3(b11, vertex):
    if b11[vertex] != vertex:
        b11[vertex] = fonk3(b11, b11[vertex])
    return b11[vertex]
def fonk4(b11, b12, root1, root2):
    if b12[root1] > b12[root2]:
        b11[root2] = root1
    elif b12[root1] < b12[root2]:
        b11[root1] = root2
    else:
        b11[root2] = root1
        b12[root1] += 1
def fonk5(b18, vertex_count):
    b9 = []
    b10 = fonk2(b18)
    b11 = list(range(vertex_count))
    b12 = [0] * vertex_count
    for edge in b10:
        u, v, b2 = edge
        b13 = fonk3(b11, u)
        b14 = fonk3(b11, v)
        if b13 != b14:
            b9.append(edge)
            fonk4(b11, b12, b13, b14)
            if len(b9) == vertex_count - 1:
                break
    return b9
def fonk6(file_name):
    with open(file_name) as file:
        b15 = [line.strip().split() for line in file]
    b16 = {edge[0] for edge in b15} | {edge[1] for edge in b15}
    b17 = list(b16)
    b18 = [[b17.index(edge[0]), b17.index(edge[1]), int(edge[2])] for edge in b15]
    return b17, b18
def fonk7(file_name):
    b17, b18 = fonk6(file_name)
    b9 = fonk5(b18, len(b17))
    b19 = sum(edge[2] for edge in b9)
    print("The minimum spanning tree is as follows:")
    for edge in b9:
        print(f"{b17[edge[0]]} to {b17[edge[1]]} = {edge[2]} miles")
    print(f"Total b2: {b19} miles.")
    fonk1(b9, b17)
if b20 = = "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 prim.py city-pairs.txt")
        sys.exit(1)
    fonk7(sys.argv[1])