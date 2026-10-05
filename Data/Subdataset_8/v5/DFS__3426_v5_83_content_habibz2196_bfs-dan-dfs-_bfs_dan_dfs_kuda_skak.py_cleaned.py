def breadth_first_search(graph, start, end):
    """
    Perform Breadth-First Search (BFS) on the given graph to find a path from the start node to the end node.
    Returns the path if found, otherwise prints "Tidak ditemukan".
    """
    queue = [[start]]
    visited = set()
    while queue:
        path = queue.pop(0)
        state = path[-1]
        if state == end:
            return path
        elif state not in visited:
            for neighbor in graph.get(state, []):
                new_path = path[:]
                new_path.append(neighbor)
                queue.append(new_path)
            visited.add(state)
    print("Tidak ditemukan")
def depth_first_search(graph, start, end):
    """
    Perform Depth-First Search (DFS) on the given graph to find a path from the start node to the end node.
    Returns the path if found, otherwise prints "Tidak ditemukan".
    """
    stack = [[start]]
    visited = set()
    while stack:
        path = stack.pop()
        state = path[-1]
        if state == end:
            return path
        elif state not in visited:
            for neighbor in graph.get(state, []):
                new_path = path[:]
                new_path.append(neighbor)
                stack.append(new_path)
            visited.add(state)
    print("Tidak ditemukan")
graph = {
    '1': {'18', '11'}, '2': {'12', '17', '19'}, '3': {'18', '20', '9', '13'},
}
start_node = '1'
end_node = '5'
bfs_path = breadth_first_search(graph, start_node, end_node)
print("BFS Path from", start_node, "to", end_node, ":", bfs_path)
dfs_path = depth_first_search(graph, start_node, end_node)
print("DFS Path from", start_node, "to", end_node, ":", dfs_path)