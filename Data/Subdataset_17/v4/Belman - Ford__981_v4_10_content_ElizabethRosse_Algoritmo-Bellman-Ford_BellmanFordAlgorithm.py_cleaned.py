
vertices = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5}
edges = [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5], [4, 6], [5, 6]]
weights = [1, 2, 4, 3, 5, 2, 4]
inf = float("inf")
distances = [inf] * len(vertices)
previous = [0] * len(vertices)
distances[0] = 0
for i in range(len(vertices) - 1):
    print("\nIteration:", i + 1)
    print("Resulting Table:")
    for e in range(len(edges)):
        u = vertices[edges[e][0]]
        v = vertices[edges[e][1]]
        weight = weights[e]
        if distances[u] + weight < distances[v]:
            distances[v] = distances[u] + weight
            previous[v] = edges[e][0]
            print("Edge:", edges[e])
            print("Vertices:", vertices)
            print("Distances (cost):", distances)
            print("Previous:", previous)
def print_path(destination):
    if previous[vertices[destination]] != 0:
        print_path(previous[vertices[destination]])
    print(destination, end=" ")
print("\nList of vertices that make up the shortest path with the least cost:")
print_path(6)
print()