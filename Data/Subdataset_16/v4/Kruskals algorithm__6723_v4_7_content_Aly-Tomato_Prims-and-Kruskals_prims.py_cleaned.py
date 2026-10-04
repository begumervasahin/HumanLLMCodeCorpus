import glb
def fonk1(file_path, delimiter):
    with open(file_path, 'r') as file:
        for line in file:
            node1, node2, b1 = [x.strip() for x in line.split(delimiter)]
            if node1 not in glb.WGRAPH:
                glb.WGRAPH[node1] = {}
            glb.WGRAPH[node1][node2] = int(b1)
    return glb.WGRAPH
def fonk2(vertex):
    if vertex not in glb.Vr:
        glb.Vr.append(vertex)
        return True
    return False
def fonk3():
    b2 = (None, None, float('inf'))
    for v1 in glb.Vr:
        for v2, b1 in glb.WGRAPH[v1].items():
            if v2 not in glb.Vr and b1 < b2[2]:
                b2 = (v1, v2, int(b1))
    return b2
def fonk4():
    a1 = 0
    b3 = next(iter(glb.WGRAPH))
    fonk2(b3)
    for _ in range(len(glb.WGRAPH) - 1):
        v1, v2, b4 = fonk3()
        a1 += b4
        glb.MST.append((v1, v2, str(b4), str(a1)))
        fonk2(v2)
    return glb.MST, a1