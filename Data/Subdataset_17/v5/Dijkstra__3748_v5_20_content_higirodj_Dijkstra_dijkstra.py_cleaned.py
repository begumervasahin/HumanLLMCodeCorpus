import numpy as np
def dijkstra(graph, source):
    n = len(graph)
    infinity = float('inf')
    distance = [infinity] * n
    distance[source] = 0
    visited_nodes = []
    visited_nodes_and_cost = []
    priority_queue = {source: distance[source]}
    preceding_nodes = {}
    while priority_queue:
        current_node, current_cost = min(priority_queue.items(), key=lambda x: x[1])
        del priority_queue[current_node]
        visited_nodes.append(current_node)
        visited_nodes_and_cost.append((current_node, current_cost))
        for neighbor in range(n):
            if graph[current_node][neighbor] != 0 and neighbor not in visited_nodes:
                new_cost = distance[current_node] + graph[current_node][neighbor]
                if new_cost < distance[neighbor]:
                    distance[neighbor] = new_cost
                    priority_queue[neighbor] = new_cost
                    preceding_nodes[neighbor] = current_node
    return visited_nodes_and_cost, preceding_nodes
def get_node_input(prompt, graph_size):
    while True:
        try:
            node = int(input(prompt))
            if 0 <= node < graph_size:
                return node
            else:
                print(f"The value entered is out of bounds. Try again.")
        except ValueError:
            print(f"Invalid input. Please enter an integer.")
def main():
    filename = input('Enter the file name (without extension): ') + '.txt'
    graph = np.loadtxt(filename)
    start_node = get_node_input('Enter starting node: ', len(graph))
    end_node = get_node_input('Enter end node: ', len(graph))
    costs, previous_nodes = dijkstra(graph, start_node)
    print(f"The shortest path from the start node {start_node} to every other node in the graph is:\n{costs}")
    shortest_path = []
    node = end_node
    while node != start_node:
        shortest_path.append(node)
        node = previous_nodes[node]
    shortest_path.append(start_node)
    shortest_path.reverse()
    print(f"The shortest path from the start node {start_node} to the target node {end_node} is {shortest_path} with a distance of {dict(costs).get(end_node)}")
if __name__ == "__main__":
    main()