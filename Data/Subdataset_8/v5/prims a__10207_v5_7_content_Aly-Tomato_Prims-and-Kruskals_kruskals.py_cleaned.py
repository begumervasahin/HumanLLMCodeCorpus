import heapq
import global_variables as glb
def read_graph(file_path, delimiter):
    with open(file_path) as file:
        for line in file:
            vertex1, vertex2, weight = [x.strip() for x in line.split(delimiter)]
            if (int(weight), vertex2, vertex1) in glb.EDGES:
                continue
            heapq.heappush(glb.EDGES, (int(weight), vertex1, vertex2))
            glb.VERTICES.add(vertex1)
            glb.VERTICES.add(vertex2)
    return glb.EDGES
def make_set(vertex):
    glb.PARENT[vertex] = vertex
    glb.RANK[vertex] = 0
def find(vertex):
    if glb.PARENT[vertex] != vertex:
        glb.PARENT[vertex] = find(glb.PARENT[vertex])
    return glb.PARENT[vertex]
def union(vertex1, vertex2):
    root1 = find(vertex1)
    root2 = find(vertex2)
    if root1 != root2:
        if glb.RANK[root1] > glb.RANK[root2]:
            glb.PARENT[root2] = root1
        else:
            glb.PARENT[root1] = root2
            glb.RANK[root2] += 1
def kruskals():
    total_weight = 0
    for vertex in glb.VERTICES:
        make_set(vertex)
    while glb.EDGES:
        weight, vertex1, vertex2 = heapq.heappop(glb.EDGES)
        if find(vertex1) != find(vertex2):
            union(vertex1, vertex2)
            total_weight += weight
            glb.MST.append((vertex1, vertex2, str(weight), str(total_weight)))
    return (glb.MST, total_weight)