def shortest_path(graph, start, goal):
    explored = []
    queue = [[start]]
    if start == goal:
        return "Start and goal nodes are the same."
    while queue:
        current_path = queue.pop(0)
        current_node = current_path[-1]
        if current_node not in explored:
            neighbours = graph[current_node]
            for neighbour in neighbours:
                new_path = list(current_path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal:
                    return new_path
            explored.append(current_node)
    return "Sorry, the path from {} to {} does not exist.".format(start, goal)
graph = {
    'A': {'B'},
    'B': {'A', 'C'},
    'C': {'B', 'D', 'H', 'I'},
    'D': {'C', 'E', 'F', 'H'},
    'E': {'D'},
    'F': {'D', 'G'},
    'G': {'F', 'H'},
    'H': {'C', 'D', 'G', 'L'},
    'I': {'C', 'J', 'K'},
    'J': {'I'},
    'K': {'I', 'L'},
    'L': {'H', 'K'}
}
start_node = input("Enter the start node: ")
goal_node = input("Enter the goal node: ")
print(shortest_path(graph, start_node, goal_node))