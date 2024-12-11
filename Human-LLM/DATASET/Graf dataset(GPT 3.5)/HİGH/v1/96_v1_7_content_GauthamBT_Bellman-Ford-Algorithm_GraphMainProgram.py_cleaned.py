from DirectedGraphClass import DirectedGraph
def fonk1(directed_graph, a1):
    directed_graph.add_edge(0, 1, 6)
    directed_graph.add_edge(0, 3, 7)
    directed_graph.add_edge(1, 2, 5)
    directed_graph.add_edge(1, 3, 8)
    directed_graph.add_edge(1, 4, -4)
    directed_graph.add_edge(2, 1, -2)
    directed_graph.add_edge(3, 2, -3)
    directed_graph.add_edge(3, 4, 9)
    directed_graph.add_edge(4, 0, 2)
    directed_graph.add_edge(4, 2, 7)
def fonk2(directed_graph):
    b1 = directed_graph.num_vertices()
    a1 = 0
    b2 = [float('inf')] * b1
    b3 = [-1] * b1
    b2[a1] = 0
    for _ in range(b1 - 1):
        for u, v, w in directed_graph.get_edges():
            if b2[u] != float('inf') and b2[u] + w < b2[v]:
                b2[v] = b2[u] + w
                b3[v] = u
    for u, v, w in directed_graph.get_edges():
        if b2[u] != float('inf') and b2[u] + w < b2[v]:
            print("Graph contains negative cycle")
            return
    directed_graph.set_shortest_path(b2, b3)
    return directed_graph
def fonk3():
    a2 = 5
    a3 = 0
    b4 = DirectedGraph(a2)
    fonk1(b4, a3)
    b4 = fonk2(b4)
    if b4:
        b4.print_shortest_path()
if b5 = = "__main__":
    fonk3()