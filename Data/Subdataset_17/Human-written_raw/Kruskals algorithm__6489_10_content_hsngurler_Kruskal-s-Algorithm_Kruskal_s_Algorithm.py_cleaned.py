def read_file(input_file):
    file = open(input_file, 'r', encoding="utf8")
    graph = []
    name_of_nodes = []
    sets_of_nodes = []
    for k in range(int(file.readline())):
        name_of_nodes.append(file.readline().split())
        sets_of_nodes.append({str(k + 1)})
        for l in range(int(file.readline())):
            split_line = file.readline().split()
            graph.append([str(k + 1), str(split_line[0]), int(split_line[1])])
    return graph, name_of_nodes, sets_of_nodes
def sort_remove(graph):
    for i in graph:
        for p in graph:
            if i[0] == p[1] and i[1] == p[0] and i[2] == p[2]:
                graph.remove(p)
    graph.sort(key=lambda x: x[2])
    return graph
def find_mst(graph, sets_of_nodes):
    minimum_spanning_tree = 0
    edges = []
    for e in graph:
        for s in sets_of_nodes:
            if {e[0]}.issubset(s):
                index_from_edge = sets_of_nodes.index(s)
            if {e[1]}.issubset(s):
                index_to_edge = sets_of_nodes.index(s)
        if index_from_edge != index_to_edge and len(sets_of_nodes) != 1:
            edges.append([e[0], e[1], e[2]])
            sets_of_nodes[index_from_edge] = sets_of_nodes[index_from_edge].union(sets_of_nodes[index_to_edge])
            sets_of_nodes.remove(sets_of_nodes[index_to_edge])
            minimum_spanning_tree += e[2]
    return minimum_spanning_tree, edges
def minimum_st(input_file):
    path, names, sets = read_file(input_file)
    path = sort_remove(path)
    mst, edges = find_mst(path, sets)
    print("The Lenght of Minimum Spanning Tree:", mst)
minimum_st('tr_districts_IDs.txt')