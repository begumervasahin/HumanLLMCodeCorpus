import heapq
import glb
def read_graph(file_path, delimiter):
    with open(file_path, 'r') as file:
        for line in file:
            v1, v2, weight = map(str.strip, line.split(delimiter))
            weight = int(weight)
            if (weight, v2, v1) in glb.EDGES:
                continue
            heapq.heappush(glb.EDGES, (weight, v1, v2))
            glb.VERTICES.update([v1, v2])
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
            if glb.RANK[root1] == glb.RANK[root2]:
                glb.RANK[root2] += 1
def kruskals():
    total_cost = 0
    for vertex in glb.VERTICES:
        make_set(vertex)
    while glb.EDGES:
        weight, v1, v2 = heapq.heappop(glb.EDGES)
        if find(v1) != find(v2):
            union(v1, v2)
            total_cost += weight
            glb.MST.append((v1, v2, str(weight), str(total_cost)))
    return glb.MST, total_cost