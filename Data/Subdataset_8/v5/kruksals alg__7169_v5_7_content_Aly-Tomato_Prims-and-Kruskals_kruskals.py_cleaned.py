import heapq
import global_vars as glb
def read_graph(file_path, delimiter):
    with open(file_path) as file:
        for line in file:
            v1, v2, weight = [x.strip() for x in line.split(delimiter)]
            add_edge(v1, v2, int(weight))
            add_vertices(v1, v2)
    return glb.EDGES
def add_edge(v1, v2, weight):
    if (weight, v2, v1) not in glb.EDGES:
        heapq.heappush(glb.EDGES, (weight, v1, v2))
def add_vertices(*vertices):
    glb.VERTICES.update(vertices)
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
        weight, v1, v2 = heapq.heappop(glb.EDGES)
        if find(v1) != find(v2):
            union(v1, v2)
            total_weight += weight
            glb.MST.append((v1, v2, str(weight), str(total_weight)))
    return (glb.MST, total_weight)