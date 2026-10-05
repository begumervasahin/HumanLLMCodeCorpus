import global_vars as glb
def fonk1(file_path, delimiter):
    with open(file_path) as file:
        for line in file:
            e1, e2, b1 = [x.strip() for x in line.split(delimiter)]
            if e1 in glb.WGRAPH:
                glb.WGRAPH[e1][e2] = b1
            else:
                glb.WGRAPH[e1] = {e2: b1}
    return glb.WGRAPH
def fonk2(vertex):
    if vertex in glb.Vr:
        return False
    else:
        glb.Vr.append(vertex)
        return True
def fonk3():
    b2 = None
    b3 = None
    a1 = 0
    for b5 in glb.Vr:
        b4 = list(glb.WGRAPH.get(b5))
        for v2 in b4:
            if v2 in glb.Vr or b5 = = v2:
                continue
            if b2 is None or b3 is None:
                b2 = b5
                b3 = v2
                a1 = glb.WGRAPH[b5][v2]
                continue
            b6 = int(glb.WGRAPH[b5][v2])
            b7 = int(glb.WGRAPH[b2][b3])
            if b6 < b7:
                b2 = b5
                b3 = v2
                a1 = b6
    return (b2, b3, a1)
def fonk4():
    a2 = 0
    b8 = len(list(glb.WGRAPH.keys()))
    b9 = list(glb.WGRAPH.keys())[0]
    fonk2(b9)
    for _ in range(b8 - 1):
        b5, v2, b10 = fonk3()
        a2 += int(b10)
        glb.MST.append((b5, v2, str(b10), str(a2)))
        fonk2(v2)
    return (glb.MST, a2)