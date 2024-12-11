import global_variables as global_vars
def fonk1(file_path, delimiter):
    with open(file_path) as file:
        for line in file:
            b1 = [x.strip() for x in line.split(delimiter)]
            vertex1, vertex2, b2 = b1[0], b1[1], b1[2]
            if vertex1 in global_vars.WEIGHTED_GRAPH:
                global_vars.WEIGHTED_GRAPH[vertex1][vertex2] = b2
            else:
                global_vars.WEIGHTED_GRAPH[vertex1] = {vertex2: b2}
    return global_vars.WEIGHTED_GRAPH
def fonk2(vertex):
    if vertex not in global_vars.VISITED_VERTICES:
        global_vars.VISITED_VERTICES.append(vertex)
        return True
    return False
def fonk3():
    b3 = min_vertex2 = b5 = None
    for v1 in global_vars.VISITED_VERTICES:
        b4 = global_vars.WEIGHTED_GRAPH.get(v1, {})
        for v2, b2 in b4.items():
            if v2 not in global_vars.VISITED_VERTICES and (b5 is None or int(b2) < b5):
                b3, min_vertex2, b5 = v1, v2, int(b2)
    return b3, min_vertex2, b5
def fonk4():
    a1 = 0
    b6 = len(global_vars.WEIGHTED_GRAPH)
    b7 = list(global_vars.WEIGHTED_GRAPH.keys())[0]
    fonk2(b7)
    for _ in range(b6 - 1):
        vertex, next_vertex, b8 = fonk3()
        a1 += b8
        global_vars.MINIMUM_SPANNING_TREE.append((vertex, next_vertex, str(b8), str(a1)))
        fonk2(next_vertex)
    return global_vars.MINIMUM_SPANNING_TREE, a1
fonk1("graph.txt", ',')
result, a1 = fonk4()
print("Minimum Spanning Tree Edges:")
for edge in result:
    print(edge)
print("Total Distance of Minimum Spanning Tree:", a1)