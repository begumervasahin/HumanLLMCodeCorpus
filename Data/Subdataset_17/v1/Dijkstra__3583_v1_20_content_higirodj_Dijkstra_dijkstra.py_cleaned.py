import numpy as np
def dijkstra(graph, source):
    n = len(graph)
    infinity = float('inf')
    distance = [infinity] * n
    distance[source] = 0
    visited_nodes = []
    visited_nodes_and_cost = []
    dictionary = {source: distance[source]}
    preceding_nodes = {}
    while dictionary:
        current_node, cost = min(dictionary.items(), key=lambda x: x[1])
        del dictionary[current_node]
        visited_nodes.append(current_node)
        visited_nodes_and_cost.append((current_node, cost))
        for j in range(n):
            if graph[current_node][j] != 0 and j not in visited_nodes:
                new_cost = distance[current_node] + graph[current_node][j]
                if new_cost < distance[j]:
                    distance[j] = new_cost
                    dictionary[j] = new_cost
                    preceding_nodes[j] = current_node
    return visited_nodes_and_cost, preceding_nodes
def main():
    filename = input('Enter the file name (without extension): ') + '.txt'
    graph = np.loadtxt(filename)
    start_node = int(input('Enter starting node: '))
    while start_node >= len(graph) or start_node < 0:
        start_node = int(input('The value entered is out of bounds. Try again: '))
    end_node = int(input('Enter end node: '))
    while end_node >= len(graph) or end_node < 0:
        end_node = int(input('The value entered is out of bounds. Try again: '))
    target_node = end_node
    costs, previous = dijkstra(graph, start_node)
    print(f"The shortest path from the start node {start_node} to every other node in the graph is \n{costs}")
    SSSPath = []
    while True:
        SSSPath.append(end_node)
        if end_node == start_node:
            break
        end_node = previous[end_node]
    SSSPath.reverse()
    print(f"The shortest path from the start node {start_node} to the target node {target_node} is {SSSPath} with a distance of {dict(costs).get(target_node)}")
if __name__ == "__main__":
    main()