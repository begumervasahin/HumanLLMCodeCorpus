from DirectedGraphClass import DirectedGraph
def fonk1(b4, source):
    b4.add_edge(0, 1, 6)
    b4.add_edge(0, 3, 7)
    b4.add_edge(1, 2, 5)
    b4.add_edge(1, 3, 8)
    b4.add_edge(1, 4, -4)
    b4.add_edge(2, 1, -2)
    b4.add_edge(3, 2, -3)
    b4.add_edge(3, 4, 9)
    b4.add_edge(4, 0, 2)
    b4.add_edge(4, 2, 7)
def fonk2(b4):
    b1 = b4.b1()
    a1 = 0
    b2 = [float('inf')] * b1
    b3 = [-1] * b1
    b2[a1] = 0
    for _ in range(b1 - 1):
        for u, v, weight in b4.get_edges():
            if b2[u] != float('inf') and b2[u] + weight < b2[v]:
                b2[v] = b2[u] + weight
                b3[v] = u
    for u, v, weight in b4.get_edges():
        if b2[u] != float('inf') and b2[u] + weight < b2[v]:
            print("Graph contains negative cycle")
            return
    b4.set_shortest_path(b2, b3)
    return b4
def fonk3():
    b1 = 5
    a1 = 0
    b4 = DirectedGraph(b1)
    fonk1(b4, a1)
    b4 = fonk2(b4)
    if b4:
        b4.print_shortest_path()
if b5 = = "__main__":
    fonk3()