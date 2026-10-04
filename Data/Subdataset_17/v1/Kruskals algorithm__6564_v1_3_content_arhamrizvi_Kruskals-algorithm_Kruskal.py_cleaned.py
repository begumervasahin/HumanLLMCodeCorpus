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
    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    else:
        parent[root_y] = root_x
        if rank[root_x] == rank[root_y]:
            rank[root_x] += 1
def kruskal_mst(input_filename, output_filename):
    edges = []
    with open(input_filename, 'r') as file:
        for line in file:
            u, v, w = map(int, line.split())
            edges.append([u, v, w])
    N = max(max(u, v) for u, v, _ in edges) + 1
    global parent, rank
    parent = list(range(N))
    rank = [0] * N
    quicksort(edges)
    mst = []
    for u, v, w in edges:
        if find(u) != find(v):
            mst.append([u, v, w])
            union(u, v)
    with open(output_filename, 'w') as file:
        for u, v, w in mst:
            file.write(f"{u} {v} {w}\n")
input_filename = 'inputgraphfile.txt'
output_filename = 'output_kruskal.txt'
kruskal_mst(input_filename, output_filename)