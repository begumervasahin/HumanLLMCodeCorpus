import heapq
import global_variables as glb
def fonk1(file_path, delimiter):
    with open(file_path) as file:
        for line in file:
            vertex1, b4, b1 = [x.strip() for x in line.split(delimiter)]
            if (int(b1), b4, vertex1) in glb.EDGES:
                continue
            heapq.heappush(glb.EDGES, (int(b1), vertex1, b4))
            glb.VERTICES.add(vertex1)
            glb.VERTICES.add(b4)
    return glb.EDGES
def fonk2(vertex):
    glb.PARENT[vertex] = vertex
    glb.RANK[vertex] = 0
def fonk3(vertex):
    if glb.PARENT[vertex] != vertex:
        glb.PARENT[vertex] = fonk3(glb.PARENT[vertex])
    return glb.PARENT[vertex]
def fonk4(vertex1, b4):
    b2 = fonk3(vertex1)
    b3 = fonk3(b4)
    if b2 != b3:
        if glb.RANK[b2] > glb.RANK[b3]:
            glb.PARENT[b3] = b2
        else:
            glb.PARENT[b2] = b3
            glb.RANK[b3] += 1
def fonk5():
    a1 = 0
    for vertex in glb.VERTICES:
        fonk2(vertex)
    while glb.EDGES:
        b1, vertex1, b4 = heapq.heappop(glb.EDGES)
        if fonk3(vertex1) != fonk3(b4):
            fonk4(vertex1, b4)
            a1 += b1
            glb.MST.append((vertex1, b4, str(b1), str(a1)))
    return (glb.MST, a1)