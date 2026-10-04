
maps = {
    'ALASKA': {'CALIFORNIA'},
    'CALIFORNIA': {'CAROLINA', 'ALASKA'},
    'CAROLINA': {'CALIFORNIA', 'INDIANA', 'HAWAII', 'DAREWALE'},
    'DAREWALE': {'CAROLINA', 'EDINBURGH', 'HAWAII', 'FLORIDA'},
    'EDINBURGH': {'DAREWALE'},
    'FLORIDA': {'DAREWALE', 'GEORGIA'},
    'GEORGIA': {'FLORIDA', 'HAWAII'},
    'HAWAII': {'DAREWALE', 'CAROLINA', 'GEORGIA', 'LOUISIANA'},
    'INDIANA': {'CAROLINA', 'IDAHO', 'KENTUCKY'},
    'IDAHO': {'INDIANA'},
    'KENTUCKY': {'LOUISIANA', 'INDIANA'},
    'LOUISIANA': {'KENTUCKY', 'HAWAII'}
}
def dfs(graph, start, goal):
    stack = [[start]]
    visited = set()
    while stack:
        path = stack.pop()
        state = path[-1]
        if state == goal:
            return path
        if state not in visited:
            visited.add(state)
            for neighbor in graph.get(state, []):
                new_path = path + [neighbor]
                stack.append(new_path)
    return None
if __name__ == "__main__":
    start_node = 'ALASKA'
    goal_node = 'INDIANA'
    path = dfs(maps, start_node, goal_node)
    if path:
        print(f"Path found: {' -> '.join(path)}")
    else:
        print("No path found")