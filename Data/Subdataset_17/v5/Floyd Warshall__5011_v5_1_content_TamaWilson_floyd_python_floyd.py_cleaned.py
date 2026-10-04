
INFINITY = float("inf")
graph = [
    [0, 5, INFINITY, 10],
    [INFINITY, 0, 3, INFINITY],
    [INFINITY, INFINITY, 0, 1],
    [INFINITY, INFINITY, INFINITY, 0]
]
def floyd_warshall(graph):
    num_vertices = len(graph)
    distance_matrix = [row[:] for row in graph]
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                distance_matrix[i][j] = min(distance_matrix[i][j], distance_matrix[i][k] + distance_matrix[k][j])
    print_distance_matrix(distance_matrix)
def print_distance_matrix(distance_matrix):
    for row in distance_matrix:
        formatted_row = "\t".join(f"{distance if distance != INFINITY else 'INF'}" for distance in row)
        print(formatted_row)
if __name__ == '__main__':
    floyd_warshall(graph)