from DirectedGraphClass import DirectedGraph
def fonk1(graph, b2):
    graph.add_edge(0, 1, 6)
    graph.add_edge(0, 3, 7)
    graph.add_edge(1, 2, 5)
    graph.add_edge(1, 3, 8)
    graph.add_edge(1, 4, -4)
    graph.add_edge(2, 1, -2)
    graph.add_edge(3, 2, -3)
    graph.add_edge(3, 4, 9)
    graph.add_edge(4, 0, 2)
    graph.add_edge(4, 2, 7)
def fonk2(graph):
    graph.bellman_ford()
def fonk3():
    a1 = 5
    b1 = DirectedGraph(a1)
    fonk1(b1, b2 = 0)
    fonk2(b1)
    b1.print_shortest_paths(b2 = 0)
if b3 = = "__main__":
    fonk3()