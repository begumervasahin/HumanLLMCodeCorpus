import global_vars as glb
def read_graph(file_path, delimiter):
    with open(file_path) as file:
        for line in file:
            e1, e2, weight = [x.strip() for x in line.split(delimiter)]
            update_weighted_graph(e1, e2, weight)
    return glb.WGRAPH
def update_weighted_graph(vertex1, vertex2, weight):
    if vertex1 in glb.WGRAPH:
        glb.WGRAPH[vertex1][vertex2] = weight
    else:
        glb.WGRAPH[vertex1] = {vertex2: weight}
def add_visited(vertex):
    if vertex not in glb.Vr:
        glb.Vr.append(vertex)
        return True
    return False
def get_min_edge():
    min_edge = None
    for v1 in glb.Vr:
        neighbors = glb.WGRAPH.get(v1, {})
        for v2, weight in neighbors.items():
            if v2 not in glb.Vr and (min_edge is None or int(weight) < int(min_edge[2])):
                min_edge = (v1, v2, weight)
    return min_edge
def prims():
    total_weight = 0
    num_vertices = len(glb.WGRAPH)
    start_vertex = next(iter(glb.WGRAPH.keys()))
    add_visited(start_vertex)
    for _ in range(num_vertices - 1):
        v1, v2, edge_weight = get_min_edge()
        total_weight += int(edge_weight)
        glb.MST.append((v1, v2, edge_weight, str(total_weight)))
        add_visited(v2)
    return glb.MST, total_weight