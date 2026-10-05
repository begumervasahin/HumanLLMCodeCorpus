import numpy as np
def dijkstra(graph, source):
    n = len(graph)
    infinity = float('inf')
    distance = [infinity for _ in range(n)]
    distance[source] = 0
    visited_nodes = set()
    previous_nodes = {}
    while len(visited_nodes) < n:
        current_node = min(
            (node for node in range(n) if node not in visited_nodes),
            key=lambda x: distance[x]
        )
        visited_nodes.add(current_node)
        for neighbor, weight in enumerate(graph[current_node]):
            if weight > 0 and neighbor not in visited_nodes:
                if distance[current_node] + weight < distance[neighbor]:
                    distance[neighbor] = distance[current_node] + weight
                    previous_nodes[neighbor] = current_node
    return distance, previous_nodes
def main():
    filename = input('Enter the file name (without extension): ') + '.txt'
    graph = np.loadtxt(filename)
    start_node = int(input('Enter the starting node: '))
    while start_node >= len(graph) or start_node < 0:
        start_node = int(input('The value entered is out of bounds. Try again: '))
    end_node = int(input('Enter the end node: '))
    while end_node >= len(graph) or end_node < 0:
        end_node = int(input('The value entered is out of bounds. Try again: '))
    distances, predecessors = dijkstra(graph, start_node)
    target_node = end_node
    shortest_path = []
    while True:
        shortest_path.append(target_node)
        if target_node == start_node:
            break
        target_node = predecessors[target_node]
    shortest_path.reverse()
    print(f"The shortest path from start node {start_node} to every other node in the graph is:")
    for node, distance in enumerate(distances):
        print(f"Node {node}: Distance = {distance}")
    print(f"\nThe shortest path from start node {start_node} to end node {end_node} is:")
    print(shortest_path)
    print(f"Distance: {distances[end_node]}")
if __name__ == "__main__":
    main()