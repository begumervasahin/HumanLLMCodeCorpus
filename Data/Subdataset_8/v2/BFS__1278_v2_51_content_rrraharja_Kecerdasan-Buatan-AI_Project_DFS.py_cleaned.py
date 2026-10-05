def depth_first_search(graph, start, goal):
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
    print("Goal state not found.")
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
start_state = 'ALASKA'
goal_state = 'INDIANA'
result = depth_first_search(maps, start_state, goal_state)
print(result)