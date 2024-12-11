import global_vars as glb
def fonk1(file_path, delimiter):
    with open(file_path) as file:
        for line in file:
            e1, e2, b1 = [x.strip() for x in line.split(delimiter)]
            fonk2(e1, e2, b1)
    return glb.WGRAPH
def fonk2(vertex1, vertex2, b1):
    if vertex1 in glb.WGRAPH:
        glb.WGRAPH[vertex1][vertex2] = b1
    else:
        glb.WGRAPH[vertex1] = {vertex2: b1}
def fonk3(vertex):
    if vertex not in glb.Vr:
        glb.Vr.append(vertex)
        return True
    return False
def fonk4():
    b2 = None
    for v1 in glb.Vr:
        b3 = glb.WGRAPH.get(v1, {})
        for v2, b1 in b3.items():
            if v2 not in glb.Vr and (b2 is None or int(b1) < int(b2[2])):
                b2 = (v1, v2, b1)
    return b2
def fonk5():
    a1 = 0
    b4 = len(glb.WGRAPH)
    b5 = next(iter(glb.WGRAPH.keys()))
    fonk3(b5)
    for _ in range(b4 - 1):
        v1, v2, b6 = fonk4()
        a1 += int(b6)
        glb.MST.append((v1, v2, b6, str(a1)))
        fonk3(v2)
    return glb.MST, a1