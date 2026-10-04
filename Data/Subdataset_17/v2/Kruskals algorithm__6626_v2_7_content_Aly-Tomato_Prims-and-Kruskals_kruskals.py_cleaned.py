
import heapq
EDGES = []
VERTICES = set()
PARENT = {}
RANK = {}
MST = []
def read_graph(file_path, delimiter):
    with open(file_path, 'r') as file:
        for line in file:
            v1, v2, weight = [x.strip() for x in line.split(delimiter)]
            weight = int(weight)
            if (weight, v2, v1) in EDGES:
                continue
            heapq.heappush(EDGES, (weight, v1, v2))
            VERTICES.add(v1)
            VERTICES.add(v2)
    return EDGES
def make_set(vertex):
    PARENT[vertex] = vertex
    RANK[vertex] = 0
def find(vertex):
    if PARENT[vertex] != vertex:
        PARENT[vertex] = find(PARENT[vertex])
    return PARENT[vertex]
def union(vertex1, vertex2):
    root1 = find(vertex1)
    root2 = find(vertex2)
    if root1 != root2:
        if RANK[root1] > RANK[root2]:
            PARENT[root2] = root1
        else:
            PARENT[root1] = root2
            if RANK[root1] == RANK[root2]:
                RANK[root2] += 1
def kruskals():
    total_cost = 0
    for vertex in VERTICES:
        make_set(vertex)
    while EDGES:
        weight, v1, v2 = heapq.heappop(EDGES)
        if find(v1) != find(v2):
            union(v1, v2)
            total_cost += weight
            MST.append((v1, v2, str(weight), str(total_cost)))
    return MST, total_cost
if __name__ == "__main__":
    read_graph('graph_data.txt', ' ')
    mst, total_cost = kruskals()
    print("Minimum Spanning Tree:")
    for edge in mst:
        print(edge)
    print("\nTotal Cost of MST:", total_cost)