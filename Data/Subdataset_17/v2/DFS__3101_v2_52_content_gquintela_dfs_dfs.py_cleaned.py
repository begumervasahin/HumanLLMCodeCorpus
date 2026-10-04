from graph import Graph
def dfs_aux(graph, vertex, vertices_marked, mark, dfs_order):
    if vertices_marked[vertex] is not None:
        return
    vertices_marked[vertex] = mark
    dfs_order.append(vertex)
    for neighbor in graph.get_neighbours(vertex):
        dfs_aux(graph, neighbor, vertices_marked, mark, dfs_order)
def dfs(graph):
    dfs_order = []
    vertices = graph.get_vertices()
    vertices_marked = {vertex: None for vertex in vertices}
    for vertex in vertices:
        if vertices_marked[vertex] is None:
            dfs_aux(graph, vertex, vertices_marked, vertex, dfs_order)
    return [dfs_order, vertices_marked]
if __name__ == "__main__":
    g = Graph()
    result = dfs(g)
    dfs_order, vertices_marked = result
    print("DFS Order:", dfs_order)
    print("Vertices Marked:", vertices_marked)