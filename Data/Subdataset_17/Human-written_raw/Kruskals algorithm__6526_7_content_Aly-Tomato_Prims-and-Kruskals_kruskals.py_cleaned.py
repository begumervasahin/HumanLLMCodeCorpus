import heapq
import glb
def read_graph(file, d):
    file_path = open(file)
    for lines in file_path:
        line = [x.strip() for x in lines.split(f'{d}')]
        v1 = line[0]
        v2 = line[1]
        weight = line[2]
        if((int(weight),v2,v1) in glb.EDGES):
            continue
        heapq.heappush(glb.EDGES, (int(weight),v1,v2))
        glb.VERTICES.add(v1)
        glb.VERTICES.add(v2)
    return glb.EDGES
def make_set(v):
     glb.PARENT[v] = v
     glb.RANK[v] = 0
def find(v):
    if(glb.PARENT[v] != v):
        glb.PARENT[v] = find(glb.PARENT[v])
    return glb.PARENT[v]
def union(v1, v2):
    root1 = find(v1)
    root2 = find(v2)
    if(root1 != root2):
        if(glb.RANK[root1] > glb.RANK[root2]):
            glb.PARENT[root2] = root1
        else:
            glb.PARENT[root1] = root2
            glb.RANK[root2] += 1
def kruskals():
    cdist = 0
    for v in glb.VERTICES:
        make_set(v)
    while(glb.EDGES):
        e,v1,v2 = heapq.heappop(glb.EDGES)
        if(find(v1) != find(v2)):
            union(v1, v2)
            cdist += e
            glb.MST.append((v1, v2, str(e), str(cdist)))
    return (glb.MST,cdist)