import heapq
import global_vars as glb
def fonk1(file_path, delimiter):
    with open(file_path) as file:
        for line in file:
            v1, b4, b1 = [x.strip() for x in line.split(delimiter)]
            fonk2(v1, b4, int(b1))
            fonk3(v1, b4)
    return glb.EDGES
def fonk2(v1, b4, b1):
    if (b1, b4, v1) not in glb.EDGES:
        heapq.heappush(glb.EDGES, (b1, v1, b4))
def fonk3(*vertices):
    glb.VERTICES.update(vertices)
def fonk4(vertex):
    glb.PARENT[vertex] = vertex
    glb.RANK[vertex] = 0
def fonk5(vertex):
    if glb.PARENT[vertex] != vertex:
        glb.PARENT[vertex] = fonk5(glb.PARENT[vertex])
    return glb.PARENT[vertex]
def fonk6(vertex1, vertex2):
    b2 = fonk5(vertex1)
    b3 = fonk5(vertex2)
    if b2 != b3:
        if glb.RANK[b2] > glb.RANK[b3]:
            glb.PARENT[b3] = b2
        else:
            glb.PARENT[b2] = b3
            glb.RANK[b3] += 1
def fonk7():
    a1 = 0
    for vertex in glb.VERTICES:
        fonk4(vertex)
    while glb.EDGES:
        b1, v1, b4 = heapq.heappop(glb.EDGES)
        if fonk5(v1) != fonk5(b4):
            fonk6(v1, b4)
            a1 += b1
            glb.MST.append((v1, b4, str(b1), str(a1)))
    return (glb.MST, a1)