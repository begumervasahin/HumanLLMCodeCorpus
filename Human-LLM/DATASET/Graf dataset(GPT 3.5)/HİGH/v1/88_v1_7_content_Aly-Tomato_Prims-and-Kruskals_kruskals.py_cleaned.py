import heapq
import glb
def fonk1(file, d):
    with open(file) as file_path:
        for lines in file_path:
            b1 = [x.strip() for x in lines.split(f'{d}')]
            v1, b5, b2 = b1[0], b1[1], b1[2]
            if (int(b2), b5, v1) in glb.EDGES:
                continue
            heapq.heappush(glb.EDGES, (int(b2), v1, b5))
            glb.VERTICES.add(v1)
            glb.VERTICES.add(b5)
    return glb.EDGES
def fonk2(v):
    glb.PARENT[v] = v
    glb.RANK[v] = 0
def fonk3(v):
    if glb.PARENT[v] != v:
        glb.PARENT[v] = fonk3(glb.PARENT[v])
    return glb.PARENT[v]
def fonk4(v1, b5):
    b3 = fonk3(v1)
    b4 = fonk3(b5)
    if b3 != b4:
        if glb.RANK[b3] > glb.RANK[b4]:
            glb.PARENT[b4] = b3
        else:
            glb.PARENT[b3] = b4
            glb.RANK[b4] += 1
def fonk5():
    a1 = 0
    for v in glb.VERTICES:
        fonk2(v)
    while glb.EDGES:
        e, v1, b5 = heapq.heappop(glb.EDGES)
        if fonk3(v1) != fonk3(b5):
            fonk4(v1, b5)
            a1 += e
            glb.MST.append((v1, b5, str(e), str(a1)))
    return glb.MST, a1