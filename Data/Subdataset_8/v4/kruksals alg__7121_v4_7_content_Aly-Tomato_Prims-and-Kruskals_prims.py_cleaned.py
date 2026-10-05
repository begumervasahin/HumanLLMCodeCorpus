import global_vars as glb
def read_graph(file_path, delimiter):
    with open(file_path) as file:
        for line in file:
            e1, e2, weight = [x.strip() for x in line.split(delimiter)]
            if e1 in glb.WGRAPH:
                glb.WGRAPH[e1][e2] = weight
            else:
                glb.WGRAPH[e1] = {e2: weight}
    return glb.WGRAPH
def add_visited(vertex):
    if vertex in glb.Vr:
        return False
    else:
        glb.Vr.append(vertex)
        return True
def get_min():
    min_v1 = None
    min_v2 = None
    min_dist = 0
    for v1 in glb.Vr:
        neighbors = list(glb.WGRAPH.get(v1))
        for v2 in neighbors:
            if v2 in glb.Vr or v1 == v2:
                continue
            if min_v1 is None or min_v2 is None:
                min_v1 = v1
                min_v2 = v2
                min_dist = glb.WGRAPH[v1][v2]
                continue
            a = int(glb.WGRAPH[v1][v2])
            b = int(glb.WGRAPH[min_v1][min_v2])
            if a < b:
                min_v1 = v1
                min_v2 = v2
                min_dist = a
    return (min_v1, min_v2, min_dist)
def prims():
    total_weight = 0
    length = len(list(glb.WGRAPH.keys()))
    start_vertex = list(glb.WGRAPH.keys())[0]
    add_visited(start_vertex)
    for _ in range(length - 1):
        v1, v2, edge_dist = get_min()
        total_weight += int(edge_dist)
        glb.MST.append((v1, v2, str(edge_dist), str(total_weight)))
        add_visited(v2)
    return (glb.MST, total_weight)