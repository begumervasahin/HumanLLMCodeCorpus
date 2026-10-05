import heapq
class GlobalVars:
    EDGES = []
    VERTICES = set()
    PARENT = {}
    RANK = {}
    MST = []
glb = GlobalVars()
def read_graph(file, delimiter):
    with open(file) as file_path:
        for line in file_path:
            v1, v2, weight = map(str.strip, line.split(delimiter))
            if (int(weight), v2, v1) in glb.EDGES:
                continue
            heapq.heappush(glb.EDGES, (int(weight), v1, v2))
            glb.VERTICES.add(v1)
            glb.VERTICES.add(v2)
    return glb.EDGES
def make_set(v):
    glb.PARENT[v] = v
    glb.RANK[v] = 0
def find(v):
    if glb.PARENT[v] != v:
        glb.PARENT[v] = find(glb.PARENT[v])
    return glb.PARENT[v]
def union(v1, v2):
    root1 = find(v1)
    root2 = find(v2)
    if root1 != root2:
        if glb.RANK[root1] > glb.RANK[root2]:
            glb.PARENT[root2] = root1
        else:
            glb.PARENT[root1] = root2
            if glb.RANK[root1] == glb.RANK[root2]:
                glb.RANK[root2] += 1
def kruskals():
    total_weight = 0
    for v in glb.VERTICES:
        make_set(v)
    while glb.EDGES:
        weight, v1, v2 = heapq.heappop(glb.EDGES)
        if find(v1) != find(v2):
            union(v1, v2)
            total_weight += weight
            glb.MST.append((v1, v2, str(weight), str(total_weight)))
    return (glb.MST, total_weight)
graph_file = "graph.txt"
delimiter = ","
read_graph(graph_file, delimiter)
mst, total_weight = kruskals()
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
print("Total Weight of MST:", total_weight)