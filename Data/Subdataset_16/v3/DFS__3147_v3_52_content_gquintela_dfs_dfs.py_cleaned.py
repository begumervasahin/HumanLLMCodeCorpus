from graph import Graph
def fonk1(graph, vertex, b3, mark, b1):
    if b3[vertex] is not None:
        return
    b3[vertex] = mark
    b1.append(vertex)
    for neighbor in graph.get_neighbours(vertex):
        fonk1(graph, neighbor, b3, mark, b1)
def fonk2(graph):
    b1 = []
    b2 = graph.get_vertices()
    b3 = {vertex: None for vertex in b2}
    for vertex in b2:
        if b3[vertex] is None:
            fonk1(graph, vertex, b3, vertex, b1)
    return [b1, b3]
def fonk3():
    b4 = Graph()
    b5 = fonk2(b4)
    b1, b3 = b5
    print("DFS Order:", b1)
    print("Vertices Marked:", b3)
if b6 = = "__main__":
    fonk3()