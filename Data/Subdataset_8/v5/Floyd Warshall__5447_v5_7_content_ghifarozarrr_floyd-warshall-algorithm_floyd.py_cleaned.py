import numpy as np
def floyd_warshall(graph, num_nodes, next_vertices):
    for intermediate_node in range(num_nodes):
        for start_node in range(num_nodes):
            for end_node in range(num_nodes):
                if graph[start_node][end_node] > (graph[start_node][intermediate_node] + graph[intermediate_node][end_node]):
                    graph[start_node][end_node] = graph[start_node][intermediate_node] + graph[intermediate_node][end_node]
                    next_vertices[start_node][end_node] = next_vertices[start_node][intermediate_node]
    return graph
def find_shortest_path(next_vertices, start_node, end_node):
    shortest_path = [start_node]
    while start_node != end_node:
        start_node = next_vertices[start_node][end_node]
        shortest_path.append(start_node)
    return shortest_path
def main():
    num_nodes = int(input("Enter the number of nodes: "))
    distances = np.zeros(shape=(num_nodes, num_nodes), dtype=np.int)
    next_vertices = np.zeros(shape=(num_nodes, num_nodes), dtype=np.int)
    for i in range(num_nodes):
        for j in range(num_nodes):
            distance_input = input(f"Distance from node {i} to node {j}: ")
            if i == j:
                distance_input = 0
            if distance_input == "-":
                distance_input = 9999
            else:
                distance_input = int(distance_input)
            distances[i][j] = distance_input
            next_vertices[i][j] = j
    print("\nInitial distances:\n", distances)
    updated_distances = floyd_warshall(distances, num_nodes, next_vertices)
    print("\nShortest paths between nodes:")
    for i in range(num_nodes):
        for j in range(num_nodes):
            if i < j:
                shortest_path = find_shortest_path(next_vertices, i, j)
                print(f"Node {i} and node {j} are connected through nodes {shortest_path}, total distance = {updated_distances[i][j]}")
if __name__ == "__main__":
    main()