
maps = {
    'ALASKA': {'CALIFORNIA'},
    'CALIFORNIA': {'CAROLINA', 'ALASKA'},
    'CAROLINA': {'CALIFORNIA', 'INDIANA', 'HAWAII', 'DAREWALE'},
    'DAREWALE': {'CAROLINA', 'EDINBURGH', 'HAWAII', 'FLORIDA'},
    'EDINBURGH': {'DAREWALE'},
    'FLORIDA': {'DAREWALE', 'GEORGIA'},
    'GEORGIA': {'FLORIDA', 'HAWAII'},
    'HAWAII': {'DAREWALE', 'CAROLINA', 'GEORGIA', 'LOUSIANA'},
    'INDIANA': {'CAROLINA', 'IDAKO', 'KENTUCKY'},
    'IDAKO': {'INDIANA'},
    'KENTUCKY': {'LOUSIANA', 'INDIANA'},
    'LOUSIANA': {'KENTUCKY', 'HAWAII'}
}
def dfs(graph, start, goal):
    stack = [[start]]
    visited = set()
    while stack:
        path = stack.pop()
        state = path[-1]
        if state == goal:
            return path
        elif state not in visited:
            for neighbor in graph.get(state, []):
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)
            visited.add(state)
    return "NOT FOUND 404"
if __name__ == "__main__":
    start_node = 'ALASKA'
    goal_node = 'INDIANA'
    path = dfs(maps, start_node, goal_node)
    print(f"Path from {start_node} to {goal_node}: {path}")