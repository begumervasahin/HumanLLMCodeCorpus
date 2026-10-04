def read_file(input_file):
    with open(input_file, 'r', encoding="utf8") as file:
        num_nodes = int(file.readline().strip())
        graph = []
        node_names = []
        sets_of_nodes = [{str(i + 1)} for i in range(num_nodes)]
        for node_index in range(num_nodes):
            node_name = file.readline().strip()
            node_names.append(node_name)
            num_edges = int(file.readline().strip())
            for _ in range(num_edges):
                neighbor, weight = file.readline().strip().split()
                graph.append([str(node_index + 1), neighbor, int(weight)])
    return graph, node_names, sets_of_nodes
def remove_duplicate_edges_and_sort(graph):
    unique_edges = set()
    for u, v, weight in graph:
        edge = tuple(sorted([u, v]))
        unique_edges.add((edge[0], edge[1], weight))
    return sorted(unique_edges, key=lambda x: x[2])
def find_mst(graph, sets_of_nodes):
    mst_weight = 0
    mst_edges = []
    for u, v, weight in graph:
        from_set = next(s for s in sets_of_nodes if u in s)
        to_set = next(s for s in sets_of_nodes if v in s)
        if from_set != to_set:
            mst_edges.append((u, v, weight))
            mst_weight += weight
            from_set.update(to_set)
            sets_of_nodes.remove(to_set)
    return mst_weight, mst_edges
def minimum_spanning_tree(input_file):
    graph, node_names, sets_of_nodes = read_file(input_file)
    graph = remove_duplicate_edges_and_sort(graph)
    mst_weight, mst_edges = find_mst(graph, sets_of_nodes)
    print("The Length of Minimum Spanning Tree:", mst_weight)
if __name__ == "__main__":
    minimum_spanning_tree('tr_districts_IDs.txt')