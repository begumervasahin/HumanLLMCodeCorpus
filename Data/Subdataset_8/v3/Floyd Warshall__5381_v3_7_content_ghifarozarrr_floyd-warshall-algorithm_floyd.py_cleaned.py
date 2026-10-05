import numpy as np
def floyd_warshall(graph, num_nodes, next_vertices):
    for intermediate_node in range(num_nodes):
        for start_node in range(num_nodes):
            for end_node in range(num_nodes):
                if graph[start_node][end_node] > (graph[start_node][intermediate_node] + graph[intermediate_node][end_node]):
                    graph[start_node][end_node] = graph[start_node][intermediate_node] + graph[intermediate_node][end_node]
                    next_vertices[start_node][end_node] = next_vertices[start_node][intermediate_node]
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
    for row in range(num_nodes):
        for col in range(num_nodes):
            distance_input = input("Distance from node %d to node %d: " % (row, col))
            if row == col:
                distance_input = 0
            if distance_input == "-":
                distance_input = 9999
            else:
                distance_input = int(distance_input)
            distances[row][col] = distance_input
            next_vertices[row][col] = col
    print("\nInitial distances:\n", distances)
    updated_distances = floyd_warshall(distances, num_nodes, next_vertices)
    print("\nShortest paths between nodes:")
    for start_node in range(num_nodes):
        for end_node in range(num_nodes):
            if start_node < end_node:
                shortest_path = find_shortest_path(next_vertices, start_node, end_node)
                print("Shortest path from node", start_node, "to node", end_node, ":", shortest_path,
                      "with total distance of", updated_distances[start_node][end_node])
if __name__ == "__main__":
    main()