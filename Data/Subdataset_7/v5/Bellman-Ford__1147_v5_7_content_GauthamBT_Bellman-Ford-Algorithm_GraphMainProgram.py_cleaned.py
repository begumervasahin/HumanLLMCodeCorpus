from DirectedGraphClass import DirectedGraph
def fonk1(graph):
    graph.add_edge(0, 1, b1 = 6)
    graph.add_edge(0, 3, b1 = 7)
    graph.add_edge(1, 2, b1 = 5)
    graph.add_edge(1, 3, b1 = 8)
    graph.add_edge(1, 4, b1 = -4)
    graph.add_edge(2, 1, b1 = -2)
    graph.add_edge(3, 2, b1 = -3)
    graph.add_edge(3, 4, b1 = 9)
    graph.add_edge(4, 0, b1 = 2)
    graph.add_edge(4, 2, b1 = 7)
def fonk2(graph):
    graph.bellman_ford()
def fonk3():
    a1 = 5
    b2 = DirectedGraph(a1)
    fonk1(b2)
    fonk2(b2)
    a2 = 0
    b2.print_shortest_paths(a2)
if b3 = = "__main__":
    fonk3()