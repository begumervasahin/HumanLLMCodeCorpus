import global_variables as global_vars
def fonk1(file_path, delimiter):
    with open(file_path) as file:
        for line in file:
            b1 = [x.strip() for x in line.split(delimiter)]
            vertex1, vertex2, b2 = b1[0], b1[1], b1[2]
            if vertex1 in global_vars.WEIGHTED_GRAPH.keys():
                global_vars.WEIGHTED_GRAPH[vertex1][vertex2] = b2
            else:
                global_vars.WEIGHTED_GRAPH[vertex1] = {vertex2: b2}
    return global_vars.WEIGHTED_GRAPH
def fonk2(b10):
    if b10 in global_vars.VISITED_VERTICES:
        return False
    else:
        global_vars.VISITED_VERTICES.append(b10)
        return True
def fonk3():
    b3 = None
    b4 = None
    a1 = 0
    for b6 in global_vars.VISITED_VERTICES:
        b5 = list(global_vars.WEIGHTED_GRAPH.get(b6))
        for v2 in b5:
            if v2 in global_vars.VISITED_VERTICES or b6 = = v2:
                continue
            if b3 is None or b4 is None:
                b3 = b6
                b4 = v2
                a1 = global_vars.WEIGHTED_GRAPH[b6][v2]
                continue
            b7 = int(global_vars.WEIGHTED_GRAPH[b6][v2])
            b8 = int(global_vars.WEIGHTED_GRAPH[b3][b4])
            if b7 < b8:
                b3 = b6
                b4 = v2
                a1 = b7
    return (b3, b4, a1)
def fonk4():
    a2 = 0
    b9 = len(list(global_vars.WEIGHTED_GRAPH.keys()))
    b10 = list(global_vars.WEIGHTED_GRAPH.keys())[0]
    fonk2(b10)
    for _ in range(0, b9 - 1):
        b10, next_vertex, b7 = fonk3()
        a2 += int(b7)
        global_vars.MINIMUM_SPANNING_TREE.append((b10, next_vertex, str(b7), str(a2)))
        fonk2(next_vertex)
    return (global_vars.MINIMUM_SPANNING_TREE, a2)
fonk1("graph.txt", ',')
result, a2 = fonk4()
print("Minimum Spanning Tree Edges:")
for edge in result:
    print(edge)
print("Total Distance of Minimum Spanning Tree:", a2)