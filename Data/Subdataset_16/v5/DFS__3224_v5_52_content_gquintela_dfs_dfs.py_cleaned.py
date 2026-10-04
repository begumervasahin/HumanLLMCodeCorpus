from graph import Graph
def fonk1(graph, vertex, b2, mark, b1):
    if b2[vertex] is not None:
        return
    b2[vertex] = mark
    b1.append(vertex)
    for neighbor in graph.get_neighbours(vertex):
        fonk1(graph, neighbor, b2, mark, b1)
def fonk2(graph):
    b1 = []
    b2 = {vertex: None for vertex in graph.get_vertices()}
    for vertex in graph.get_vertices():
        if b2[vertex] is None:
            fonk1(graph, vertex, b2, vertex, b1)
    return [b1, b2]
def fonk3():
    b3 = Graph()
    b4 = fonk2(b3)
    b1, b2 = b4
    print("DFS Order:", b1)
    print("Vertices Marked:", b2)
if b5 = = "__main__":
    fonk3()