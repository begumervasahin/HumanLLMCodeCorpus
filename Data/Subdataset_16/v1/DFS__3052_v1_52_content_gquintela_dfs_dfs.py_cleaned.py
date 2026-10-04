from graph import Graph
def fonk1(graph, vertex, b3, b4, b1):
    if b3[vertex] is not None:
        return []
    b3[vertex] = b4
    b1.append(vertex)
    for neighbour in graph.get_neighbours(vertex):
        fonk1(graph, neighbour, b3, b4, b1)
def fonk2(graph):
    b1 = []
    b2 = graph.get_vertices()
    b3 = {vertex: None for vertex in b2}
    for vertex in b2:
        b4 = vertex
        fonk1(graph, vertex, b3, b4, b1)
    return [b1, b3]
if b5 = = "__main__":
    b6 = Graph()
    b7 = fonk2(b6)
    b1, b3 = b7
    print("DFS Order:", b1)
    print("Vertices Marked:", b3)