
import glb
def read_graph(file, d):
    file_path = open(file)
    for lines in file_path:
        line = [x.strip() for x in lines.split(f'{d}')]
        e1 = line[0]
        e2 = line[1]
        weight = line[2]
        if e1 in glb.WGRAPH.keys():
            glb.WGRAPH[e1][e2] = weight
        else:
            glb.WGRAPH[e1] = {}
            glb.WGRAPH[e1][e2] = weight
    return glb.WGRAPH
def add_visited(Vertex):
    if Vertex in glb.Vr:
        return False
    else:
        glb.Vr.append(Vertex)
        return True
def get_min():
    minv1 = None
    minv2 = None
    mindist = 0
    for v1 in glb.Vr:
        neighbors = list(glb.WGRAPH.get(v1))
        for v2 in neighbors:
            if v2 in glb.Vr or v1 == v2:
                continue
            if minv1 is None or minv2 is None:
                minv1 = v1
                minv2 = v2
                mindist = glb.WGRAPH[v1][v2]
                continue
            a = int(glb.WGRAPH[v1][v2])
            b = int(glb.WGRAPH[minv1][minv2])
            if a < b:
                minv1 = v1
                minv2 = v2
                mindist = a
    return (minv1, minv2, mindist)
def prims():
    cdist = 0
    length = len(list(glb.WGRAPH.keys()))
    v = list(glb.WGRAPH.keys())[0]
    add_visited(v)
    for i in range(0, length - 1):
        v, v2, edist = get_min()
        cdist += int(edist)
        glb.MST.append((v, v2, str(edist), str(cdist)))
        add_visited(v2)
    return (glb.MST, cdist)
read_graph("graph.txt", ',')
result, total_distance = prims()
print("Minimum Spanning Tree Edges:")
for edge in result:
    print(edge)
print("Total Distance of Minimum Spanning Tree:", total_distance)