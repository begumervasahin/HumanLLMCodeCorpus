
maps = {
    'ALASKA': set(['CALIFORNIA']),
    'CALIFORNIA': set(['CAROLINA', 'ALASKA']),
    'CAROLINA': set(['CALIFORNIA', 'INDIANA', 'HAWAII', 'DAREWALE']),
    'DAREWALE': set(['CAROLINA', 'EDINBURGH', 'HAWAII', 'FLORIDA']),
    'EDINBURGH': set(['DAREWALE']),
    'FLORIDA': set(['DAREWALE', 'GEORGIA']),
    'GEORGIA': set(['FLORIDA', 'HAWAII']),
    'HAWAII': set(['DAREWALE', 'CAROLINA', 'GEORGIA', 'LOUISIANA']),
    'INDIANA': set(['CAROLINA', 'IDAHO', 'KENTUCKY']),
    'IDAHO': set(['INDIANA']),
    'KENTUCKY': set(['LOUISIANA', 'INDIANA']),
    'LOUISIANA': set(['KENTUCKY', 'HAWAII'])
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
    print("Path not found")
    return None
if __name__ == "__main__":
    path = dfs(maps, 'ALASKA', 'INDIANA')
    if path:
        print(f"Path found: {' -> '.join(path)}")
    else:
        print("No path found")