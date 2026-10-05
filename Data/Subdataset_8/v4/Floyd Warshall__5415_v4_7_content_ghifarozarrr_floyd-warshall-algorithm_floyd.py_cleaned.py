import numpy as np
def floyd_warshall(graph, num_nodes, next_vertices):
    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                if graph[i][j] > (graph[i][k] + graph[k][j]):
                    graph[i][j] = graph[i][k] + graph[k][j]
                    next_vertices[i][j] = next_vertices[i][k]
    return graph
def find_shortest_path(next_vertices, source, destination):
    shortest_path = [source]
    while source != destination:
        source = next_vertices[source][destination]
        shortest_path.append(source)
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
    print("\nIteration 0\n", distances)
    updated_distances = floyd_warshall(distances, num_nodes, next_vertices)
    print("\nShortest paths between nodes:")
    for i in range(num_nodes):
        for j in range(num_nodes):
            if i < j:
                shortest_path = find_shortest_path(next_vertices, i, j)
                print(f"Node {i} and node {j} are connected through nodes {shortest_path}, total distance = {updated_distances[i][j]}")
if __name__ == "__main__":
    main()