import glb
def read_graph(file_path, delimiter):
    with open(file_path, 'r') as file:
        for line in file:
            node1, node2, weight = [x.strip() for x in line.split(delimiter)]
            if node1 not in glb.WGRAPH:
                glb.WGRAPH[node1] = {}
            glb.WGRAPH[node1][node2] = int(weight)
    return glb.WGRAPH
def add_visited(vertex):
    if vertex not in glb.Vr:
        glb.Vr.append(vertex)
        return True
    return False
def get_min():
    min_edge = (None, None, float('inf'))
    for v1 in glb.Vr:
        for v2, weight in glb.WGRAPH[v1].items():
            if v2 not in glb.Vr and weight < min_edge[2]:
                min_edge = (v1, v2, int(weight))
    return min_edge
def prims():
    total_distance = 0
    start_vertex = next(iter(glb.WGRAPH))
    add_visited(start_vertex)
    for _ in range(len(glb.WGRAPH) - 1):
        v1, v2, edge_distance = get_min()
        total_distance += edge_distance
        glb.MST.append((v1, v2, str(edge_distance), str(total_distance)))
        add_visited(v2)
    return glb.MST, total_distance