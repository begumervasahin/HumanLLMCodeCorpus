def next_edges(graph, available_edges, vertex, graph_size):
    for j in range(graph_size):
        if graph[vertex][j] != 0:
            available_edges.append([vertex, j])
def prim_frontier_edge(graph, available_edges, visited):
    min_cost = float('inf')
    selected_edge = None
    for u, v in available_edges:
        if graph[u][v] != 0 and visited[u] and not visited[v] and graph[u][v] < min_cost:
            min_cost = graph[u][v]
            selected_edge = [u, v]
    if selected_edge:
        visited[selected_edge[1]] = True
    return selected_edge
def update_frontier_edges(graph, available_edges, new_vertex, graph_size):
    available_edges = [edge for edge in available_edges if edge[1] != new_vertex]
    next_edges(graph, available_edges, new_vertex, graph_size)
    return available_edges
def prims(graph, start):
    graph_size = len(graph)
    spanning_edges = []
    available_edges = []
    visited = [False] * graph_size
    visited[start] = True
    next_edges(graph, available_edges, start, graph_size)
    for _ in range(graph_size - 1):
        minimum_edge = prim_frontier_edge(graph, available_edges, visited)
        if minimum_edge:
            spanning_edges.append(minimum_edge)
            new_vertex = minimum_edge[1]
            available_edges = update_frontier_edges(graph, available_edges, new_vertex, graph_size)
    total_cost = sum(graph[u][v] for u, v in spanning_edges)
    mstree = [[0] * graph_size for _ in range(graph_size)]
    for u, v in spanning_edges:
        mstree[u][v] = graph[u][v]
        mstree[v][u] = graph[u][v]
    print("The total cost is:", total_cost)
    print("The minimum spanning tree is:")
    for row in mstree:
        print(row)
    return mstree
def get_graph_input(graph_size):
    graph = []
    for i in range(graph_size):
        row = []
        for j in range(graph_size):
            value = int(input(f"Enter the value for edge {i}-{j}: "))
            row.append(value)
        graph.append(row)
    return graph
def main():
    graph_size = int(input("Enter the number of vertices: "))
    graph = get_graph_input(graph_size)
    start = int(input("Enter the start vertex: "))
    prims(graph, start)
if __name__ == "__main__":
    main()