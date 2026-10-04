def read_file(input_file):
    with open(input_file, 'r', encoding="utf8") as file:
        num_nodes = int(file.readline().strip())
        graph = []
        node_names = []
        node_sets = [{str(i + 1)} for i in range(num_nodes)]
        for i in range(num_nodes):
            node_names.append(file.readline().split())
            num_edges = int(file.readline().strip())
            for _ in range(num_edges):
                node, weight = file.readline().split()
                graph.append([str(i + 1), node, int(weight)])
    return graph, node_names, node_sets
def sort_and_remove_duplicates(graph):
    unique_edges = []
    for edge in graph:
        if not any(e[0] == edge[1] and e[1] == edge[0] and e[2] == edge[2] for e in unique_edges):
            unique_edges.append(edge)
    unique_edges.sort(key=lambda x: x[2])
    return unique_edges
def find_minimum_spanning_tree(graph, node_sets):
    mst_weight = 0
    mst_edges = []
    for edge in graph:
        u, v, weight = edge
        u_set = next(s for s in node_sets if u in s)
        v_set = next(s for s in node_sets if v in s)
        if u_set != v_set:
            mst_edges.append(edge)
            mst_weight += weight
            u_set.update(v_set)
            node_sets.remove(v_set)
        if len(node_sets) == 1:
            break
    return mst_weight, mst_edges
def minimum_spanning_tree(input_file):
    graph, node_names, node_sets = read_file(input_file)
    graph = sort_and_remove_duplicates(graph)
    mst_weight, mst_edges = find_minimum_spanning_tree(graph, node_sets)
    print("The Length of Minimum Spanning Tree:", mst_weight)
    for edge in mst_edges:
        print(f"Edge: {edge[0]} -> {edge[1]} with weight {edge[2]}")
minimum_spanning_tree('tr_districts_IDs.txt')