import numpy as np
def floyd_warshall(dist_matrix, num_nodes, next_node):
    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                if dist_matrix[i][j] > dist_matrix[i][k] + dist_matrix[k][j]:
                    dist_matrix[i][j] = dist_matrix[i][k] + dist_matrix[k][j]
                    next_node[i][j] = next_node[i][k]
    return dist_matrix
def reconstruct_path(next_node, source, destination):
    path = [source]
    while source != destination:
        source = next_node[source][destination]
        path.append(source)
    return path
def get_distance_matrix(num_nodes):
    dist_matrix = np.zeros((num_nodes, num_nodes), dtype=int)
    next_node = np.zeros((num_nodes, num_nodes), dtype=int)
    for i in range(num_nodes):
        for j in range(num_nodes):
            distance = input(f"Distance from node {i} to node {j} (use '-' for infinity): ")
            if i == j:
                distance = 0
            elif distance == "-":
                distance = 9999
            else:
                distance = int(distance)
            dist_matrix[i][j] = distance
            next_node[i][j] = j
    return dist_matrix, next_node
def display_results(updated_dist_matrix, next_node, num_nodes):
    print("\nShortest paths and distances:\n")
    for i in range(num_nodes):
        for j in range(num_nodes):
            if i != j:
                path = reconstruct_path(next_node, i, j)
                distance = updated_dist_matrix[i][j]
                print(f"Path from node {i} to node {j}: {path}, Total distance: {distance}")
def main():
    num_nodes = int(input("Enter the number of nodes: "))
    dist_matrix, next_node = get_distance_matrix(num_nodes)
    print("\nInitial Distance Matrix (Iteration 0):\n", dist_matrix)
    updated_dist_matrix = floyd_warshall(dist_matrix, num_nodes, next_node)
    display_results(updated_dist_matrix, next_node, num_nodes)
if __name__ == '__main__':
    main()