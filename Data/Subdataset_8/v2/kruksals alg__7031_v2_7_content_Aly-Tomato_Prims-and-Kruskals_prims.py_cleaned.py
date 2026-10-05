import global_variables as global_vars
def read_graph(file_path, delimiter):
    with open(file_path) as file:
        for line in file:
            elements = [x.strip() for x in line.split(delimiter)]
            vertex1, vertex2, weight = elements[0], elements[1], elements[2]
            if vertex1 in global_vars.WEIGHTED_GRAPH.keys():
                global_vars.WEIGHTED_GRAPH[vertex1][vertex2] = weight
            else:
                global_vars.WEIGHTED_GRAPH[vertex1] = {vertex2: weight}
    return global_vars.WEIGHTED_GRAPH
def add_visited(vertex):
    if vertex in global_vars.VISITED_VERTICES:
        return False
    else:
        global_vars.VISITED_VERTICES.append(vertex)
        return True
def get_min_edge():
    min_vertex1 = None
    min_vertex2 = None
    min_distance = 0
    for v1 in global_vars.VISITED_VERTICES:
        neighbors = list(global_vars.WEIGHTED_GRAPH.get(v1))
        for v2 in neighbors:
            if v2 in global_vars.VISITED_VERTICES or v1 == v2:
                continue
            if min_vertex1 is None or min_vertex2 is None:
                min_vertex1 = v1
                min_vertex2 = v2
                min_distance = global_vars.WEIGHTED_GRAPH[v1][v2]
                continue
            edge_distance = int(global_vars.WEIGHTED_GRAPH[v1][v2])
            current_min_distance = int(global_vars.WEIGHTED_GRAPH[min_vertex1][min_vertex2])
            if edge_distance < current_min_distance:
                min_vertex1 = v1
                min_vertex2 = v2
                min_distance = edge_distance
    return (min_vertex1, min_vertex2, min_distance)
def prims():
    total_distance = 0
    length = len(list(global_vars.WEIGHTED_GRAPH.keys()))
    vertex = list(global_vars.WEIGHTED_GRAPH.keys())[0]
    add_visited(vertex)
    for _ in range(0, length - 1):
        vertex, next_vertex, edge_distance = get_min_edge()
        total_distance += int(edge_distance)
        global_vars.MINIMUM_SPANNING_TREE.append((vertex, next_vertex, str(edge_distance), str(total_distance)))
        add_visited(next_vertex)
    return (global_vars.MINIMUM_SPANNING_TREE, total_distance)
read_graph("graph.txt", ',')
result, total_distance = prims()
print("Minimum Spanning Tree Edges:")
for edge in result:
    print(edge)
print("Total Distance of Minimum Spanning Tree:", total_distance)