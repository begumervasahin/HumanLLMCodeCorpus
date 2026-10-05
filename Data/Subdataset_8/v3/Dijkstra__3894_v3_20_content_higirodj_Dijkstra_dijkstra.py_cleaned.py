import numpy as np
def dijkstra(graph, source):
    num_nodes = len(graph)
    infinity = float('inf')
    distances = [infinity for _ in range(num_nodes)]
    distances[source] = 0
    visited_nodes = set()
    previous_nodes = {}
    while len(visited_nodes) < num_nodes:
        current_node = min(
            (node for node in range(num_nodes) if node not in visited_nodes),
            key=lambda x: distances[x]
        )
        visited_nodes.add(current_node)
        for neighbor, weight in enumerate(graph[current_node]):
            if weight > 0 and neighbor not in visited_nodes:
                if distances[current_node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[current_node] + weight
                    previous_nodes[neighbor] = current_node
    return distances, previous_nodes
def main():
    filename = input('Enter the file name (without extension): ') + '.txt'
    graph = np.loadtxt(filename)
    start_node = int(input('Enter the starting node: '))
    while not (0 <= start_node < len(graph)):
        start_node = int(input('Invalid input. Please enter a valid starting node: '))
    end_node = int(input('Enter the end node: '))
    while not (0 <= end_node < len(graph)):
        end_node = int(input('Invalid input. Please enter a valid end node: '))
    distances, predecessors = dijkstra(graph, start_node)
    shortest_path = []
    current_node = end_node
    while current_node != start_node:
        shortest_path.append(current_node)
        current_node = predecessors[current_node]
    shortest_path.append(start_node)
    shortest_path.reverse()
    print(f"The shortest path from start node {start_node} to every other node in the graph is:")
    for node, distance in enumerate(distances):
        print(f"Node {node}: Distance = {distance}")
    print(f"\nThe shortest path from start node {start_node} to end node {end_node} is:")
    print(shortest_path)
    print(f"Distance: {distances[end_node]}")
if __name__ == "__main__":
    main()