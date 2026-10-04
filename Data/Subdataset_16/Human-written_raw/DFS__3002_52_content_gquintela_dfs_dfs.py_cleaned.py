from graph import Graph
def fonk1(graph, vertex, b3, b4, b1):
    if b3[vertex] != None:
        return []
    b3[vertex] = b4
    b1.append(vertex)
    for neighbour in graph.get_neighbours(vertex):
        fonk1(graph, neighbour, b3, b4, b1)
def fonk2(graph):
    b1 = []
    b2 = graph.get_vertices()
    b3 = {}
    for vertex in b2:
        b4 = vertex
        b3[vertex] = None
    for vertex in b2:
        b4 = vertex
        fonk1(graph, vertex, b3, b4, b1)
    b5 = [b1, b3]
    return b5