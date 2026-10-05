import heapq
import glb
def fonk1(file, d):
    b1 = open(file)
    for lines in b1:
        b2 = [x.strip() for x in lines.split(f'{d}')]
        b3 = b2[0]
        b4 = b2[1]
        b5 = b2[2]
        if((int(b5),b4,b3) in glb.EDGES):
            continue
        heapq.heappush(glb.EDGES, (int(b5),b3,b4))
        glb.VERTICES.add(b3)
        glb.VERTICES.add(b4)
    return glb.EDGES
def fonk2(v):
     glb.PARENT[v] = v
     glb.RANK[v] = 0
def fonk3(v):
    if(glb.PARENT[v] != v):
        glb.PARENT[v] = fonk3(glb.PARENT[v])
    return glb.PARENT[v]
def fonk4(b3, b4):
    b6 = fonk3(b3)
    b7 = fonk3(b4)
    if(b6 != b7):
        if(glb.RANK[b6] > glb.RANK[b7]):
            glb.PARENT[b7] = b6
        else:
            glb.PARENT[b6] = b7
            glb.RANK[b7] += 1
def fonk5():
    a1 = 0
    for v in glb.VERTICES:
        fonk2(v)
    while(glb.EDGES):
        e,b3,b4 = heapq.heappop(glb.EDGES)
        if(fonk3(b3) != fonk3(b4)):
            fonk4(b3, b4)
            a1 += e
            glb.MST.append((b3, b4, str(e), str(a1)))
    return (glb.MST,a1)