import matplotlib.pyplot as plt
import networkx as nx
def fonk1(b15):
    return sorted(b15, b1 = lambda x: x[2])
def fonk2(b4, vertex):
    if b4[vertex] != vertex:
        b4[vertex] = fonk2(b4, b4[vertex])
    return b4[vertex]
def fonk3(b4, b5, root1, root2):
    if b5[root1] > b5[root2]:
        b4[root2] = root1
    elif b5[root1] < b5[root2]:
        b4[root1] = root2
    else:
        b4[root2] = root1
        b5[root1] += 1
def fonk4(b15, num_vertices):
    b2 = []
    b3 = fonk1(b15)
    b4 = list(range(num_vertices))
    b5 = [0] * num_vertices
    for edge in b3:
        v, u, b6 = edge
        b7 = fonk2(b4, v)
        b8 = fonk2(b4, u)
        if b7 != b8:
            b2.append(edge)
            fonk3(b4, b5, b7, b8)
    return b2
def fonk5(b2, b14):
    b9 = nx.Graph()
    for edge in b2:
        b9.add_edge(b14[edge[0]], b14[edge[1]], b6 = edge[2])
    b10 = nx.spring_layout(b9, k=20, iterations=150)
    b11 = nx.get_edge_attributes(b9, 'b6')
    nx.draw(b9, b10, b12 = True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(b9, b10, b13 = b11)
    plt.show()
def fonk6(b21):
    b14 = set()
    b15 = []
    with open(b21) as file:
        for line in file:
            v1, v2, b6 = line.strip().split()
            b14.add(v1)
            b14.add(v2)
            b15.append((v1, v2, int(b6)))
    b16 = list(b14)
    b17 = len(b16)
    b18 = [(b16.index(v1), b16.index(v2), b6) for v1, v2, b6 in b15]
    b2 = fonk4(b18, b17)
    b19 = sum(edge[2] for edge in b2)
    print("The minimum spanning tree:")
    for edge in b2:
        print(f"{b16[edge[0]]} to {b16[edge[1]]} = {edge[2]} units.")
    print(f"Total b6: {b19} units.")
    fonk5(b2, b16)
if b20 = = "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)
    b21 = sys.argv[1]
    fonk6(b21)