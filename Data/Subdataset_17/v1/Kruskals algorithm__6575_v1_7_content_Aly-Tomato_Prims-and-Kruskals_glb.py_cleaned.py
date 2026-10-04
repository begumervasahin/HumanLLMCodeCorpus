WGRAPH = {}
MST = []
Vr = []
PARENT = {}
RANK = {}
EDGES = []
VERTICES = set()
def print_pretty():
    t1 = "Vertex 1"
    t2 = "Vertex 2"
    tw = "Distance"
    cd = "Cumulative Distance"
    print("******************************************************************************")
    print(t1.ljust(15, ' '), "\t", t2.ljust(15, ' '), "\t", tw.ljust(10, ' '), "\t", cd.ljust(10, ' '))
    print("******************************************************************************")
    for m in MST:
        v1, v2, w, c = m
        print(v1.ljust(15, ' '), "\t", v2.ljust(15, ' '), "\t", str(w).ljust(10, ' '), "\t", str(c).ljust(15, ' '))
def make_set(vertice):
    PARENT[vertice] = vertice
    RANK[vertice] = 0
def find(vertice):
    if PARENT[vertice] != vertice:
        PARENT[vertice] = find(PARENT[vertice])
    return PARENT[vertice]
def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if RANK[root1] < RANK[root2]:
            PARENT[root1] = root2
        else:
            PARENT[root2] = root1
            if RANK[root1] == RANK[root2]:
                RANK[root1] += 1
def kruskal():
    global MST
    cumulative_distance = 0
    for vertice in VERTICES:
        make_set(vertice)
    EDGES.sort(key=lambda x: x[2])
    for edge in EDGES:
        v1, v2, weight = edge
        if find(v1) != find(v2):
            union(v1, v2)
            cumulative_distance += weight
            MST.append((v1, v2, weight, cumulative_distance))
if __name__ == "__main__":
    VERTICES = {'A', 'B', 'C', 'D', 'E'}
    EDGES = [
        ('A', 'B', 1),
        ('A', 'C', 3),
        ('B', 'C', 2),
        ('B', 'D', 6),
        ('C', 'D', 4),
        ('C', 'E', 2),
        ('D', 'E', 5)
    ]
    kruskal()
    print_pretty()