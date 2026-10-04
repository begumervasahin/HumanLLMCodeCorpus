def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
def quicksort(array):
    quicksort_aux(array, 0, len(array) - 1)
def quicksort_aux(array, start, end):
    if start < end:
        boundary = partition(array, start, end)
        quicksort_aux(array, start, boundary)
        quicksort_aux(array, boundary + 1, end)
def partition(array, start, end):
    mid = (start + end)
    pivot = array[mid][2]
    swap(array, start, mid)
    index = start
    for k in range(start + 1, end + 1):
        if array[k][2] < pivot:
            index += 1
            swap(array, k, index)
    swap(array, start, index)
    return index
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_x] = root_y
            if rank[root_x] == rank[root_y]:
                rank[root_y] += 1
def read_graph(filename):
    edges = []
    max_vertex = 0
    with open(filename, "r") as file:
        for line in file:
            u, v, w = map(int, line.split())
            edges.append([u, v, w])
            max_vertex = max(max_vertex, u, v)
    return edges, max_vertex + 1
def kruskal(filename, output_filename):
    edges, num_vertices = read_graph(filename)
    global parent, rank
    parent = list(range(num_vertices))
    rank = [0] * num_vertices
    quicksort(edges)
    mst = []
    for u, v, weight in edges:
        if find(u) != find(v):
            mst.append([u, v, weight])
            union(u, v)
    with open(output_filename, "w") as file:
        for u, v, w in mst:
            file.write(f"{u} {v} {w}\n")
