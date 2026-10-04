from graph import Graph
def dfs_aux(graph, vertex, vertices_marked, mark, dfs_order):
    if vertices_marked[vertex] != None:
        return []
    vertices_marked[vertex] = mark
    dfs_order.append(vertex)
    for neighbour in graph.get_neighbours(vertex):
        dfs_aux(graph, neighbour, vertices_marked, mark, dfs_order)
def dfs(graph):
    dfs_order = []
    vertices = graph.get_vertices()
    vertices_marked = {}
    for vertex in vertices:
        mark = vertex
        vertices_marked[vertex] = None
    for vertex in vertices:
        mark = vertex
        dfs_aux(graph, vertex, vertices_marked, mark, dfs_order)
    output = [dfs_order, vertices_marked]
    return output