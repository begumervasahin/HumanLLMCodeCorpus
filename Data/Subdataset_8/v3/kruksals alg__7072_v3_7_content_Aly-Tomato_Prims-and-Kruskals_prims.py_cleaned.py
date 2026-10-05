import global_variables as global_vars
def read_graph(file_path, delimiter):
    with open(file_path) as file:
        for line in file:
            elements = [x.strip() for x in line.split(delimiter)]
            vertex1, vertex2, weight = elements[0], elements[1], elements[2]
            if vertex1 in global_vars.WEIGHTED_GRAPH:
                global_vars.WEIGHTED_GRAPH[vertex1][vertex2] = weight
            else:
                global_vars.WEIGHTED_GRAPH[vertex1] = {vertex2: weight}
    return global_vars.WEIGHTED_GRAPH
def add_visited(vertex):
    if vertex not in global_vars.VISITED_VERTICES:
        global_vars.VISITED_VERTICES.append(vertex)
        return True
    return False
def get_min_edge():
    min_vertex1 = min_vertex2 = min_distance = None
    for v1 in global_vars.VISITED_VERTICES:
        neighbors = global_vars.WEIGHTED_GRAPH.get(v1, {})
        for v2, weight in neighbors.items():
            if v2 not in global_vars.VISITED_VERTICES and (min_distance is None or int(weight) < min_distance):
                min_vertex1, min_vertex2, min_distance = v1, v2, int(weight)
    return min_vertex1, min_vertex2, min_distance
def prims():
    total_distance = 0
    length = len(global_vars.WEIGHTED_GRAPH)
    start_vertex = list(global_vars.WEIGHTED_GRAPH.keys())[0]
    add_visited(start_vertex)
    for _ in range(length - 1):
        vertex, next_vertex, edge_distance = get_min_edge()
        total_distance += edge_distance
        global_vars.MINIMUM_SPANNING_TREE.append((vertex, next_vertex, str(edge_distance), str(total_distance)))
        add_visited(next_vertex)
    return global_vars.MINIMUM_SPANNING_TREE, total_distance
read_graph("graph.txt", ',')
result, total_distance = prims()
print("Minimum Spanning Tree Edges:")
for edge in result:
    print(edge)
print("Total Distance of Minimum Spanning Tree:", total_distance)