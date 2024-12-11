import glb
def fonk1(file, d):
    b1 = open(file)
    for lines in b1:
        b2 = [x.strip() for x in lines.split(f'{d}')]
        b3 = b2[0]
        b4 = b2[1]
        b5 = b2[2]
        if b3 in glb.WGRAPH.keys():
            glb.WGRAPH[b3][b4] = b5
        else:
            glb.WGRAPH[b3] = {}
            glb.WGRAPH[b3][b4] = b5
    return glb.WGRAPH
def fonk2(Vertex):
    if(Vertex in glb.Vr):
        return False
    else:
        glb.Vr.append(Vertex)
        return True
def fonk3():
    b6 = None
    b7 = None
    a1 = 0
    for b9 in glb.Vr:
        b8 = list(glb.WGRAPH.get(b9))
        for v2 in b8:
            if v2 in glb.Vr or b9 = = v2:
                continue
            if b6 = = None or b7 == None:
                b6 = b9
                b7 = v2
                a1 = glb.WGRAPH[b9][v2]
                continue
            b10 = int(glb.WGRAPH[b9][v2])
            b11 = int(glb.WGRAPH[b6][b7])
            if b10 < b11:
                b6 = b9
                b7 = v2
                a1 = b10
    return (b6,b7,a1)
def fonk4():
    a2 = 0
    b12 = len(list(glb.WGRAPH.keys()))
    b13 = list(glb.WGRAPH.keys())[0]
    fonk2(b13)
    for i in range(0,b12-1):
        b13, v2, b14 = fonk3()
        a2 += int(b14)
        glb.MST.append((b13,v2,str(b14),str(a2)))
        fonk2(v2)
    return (glb.MST,a2)