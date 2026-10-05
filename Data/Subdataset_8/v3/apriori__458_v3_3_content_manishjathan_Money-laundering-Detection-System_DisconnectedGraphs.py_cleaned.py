import drawGraph as dG
def depth_first_search(edge_list, graph, source_node):
    dfs_stack = []
    explored_stack = [source_node]
    while explored_stack:
        visited_node = explored_stack.pop()
        if visited_node not in dfs_stack:
            dfs_stack.append(visited_node)
        if visited_node in graph:
            for neighbor in graph[visited_node]:
                explored_stack.append(neighbor)
    print("Vertices in Graph")
    dfs_stack.sort()
    print(dfs_stack)
    return dfs_stack
def find_source_nodes(indegree_map):
    print("Source Nodes")
    source_nodes = [node for node, indegree in indegree_map.items() if indegree == 0]
    print(source_nodes)
    return source_nodes
def split_edge_list(edge_list, graph, source_nodes):
    new_edge_lists = []
    for source_node in source_nodes:
        vertex_set = depth_first_search(edge_list, graph, source_node)
        new_edge_list = [edge for edge in edge_list if edge[0] in vertex_set and edge[1] in vertex_set]
        new_edge_lists.append(new_edge_list)
    print("New Edge Lists after splitting")
    for i, edge_list in enumerate(new_edge_lists):
        print(edge_list)
        dG.drawGraph(edge_list, f"Graph{i}.png")
    return new_edge_lists
edge_list = [(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 5), (3, 6), (4, 5), (4, 6), (5, 6), (7, 8), (8, 9), (8, 10), (9, 10)]
graph = {
    1: [2, 3], 2: [3, 4], 3: [4, 5, 6],
    4: [5, 6], 5: [6], 7: [8], 8: [9, 10], 9: [10]
}
indegree_map = {
    1: 0, 2: 1, 3: 2, 4: 2, 5: 2, 6: 3,
    7: 0, 8: 1, 9: 1, 10: 2
}
source_nodes = find_source_nodes(indegree_map)
split_edge_list(edge_list, graph, source_nodes)