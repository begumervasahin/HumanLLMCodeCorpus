
maps = {
    'ALASKA': set(['CALIFORNIA']),
    'CALIFORNIA': set(['CAROLINA', 'ALASKA']),
    'CAROLINA': set(['CALIFORNIA', 'INDIANA', 'HAWAII', 'DAREWALE']),
    'DAREWALE': set(['CAROLINA', 'EDINBURGH', 'HAWAII', 'FLORIDA']),
    'EDINBURGH': set(['DAREWALE']),
    'FLORIDA': set(['DAREWALE', 'GEORGIA']),
    'GEORGIA': set(['FLORIDA', 'HAWAII']),
    'HAWAII': set(['DAREWALE', 'CAROLINA', 'GEORGIA', 'LOUSIANA']),
    'INDIANA': set(['CAROLINA', 'IDAKO', 'KENTUCKY']),
    'IDAKO': set(['INDIANA']),
    'KENTUCKY': set(['LOUSIANA', 'INDIANA']),
    'LOUSIANA': set(['KENTUCKY', 'HAWAII'])
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
            for branch in graph.get(state, []):
                new_path = list(path)
                new_path.append(branch)
                stack.append(new_path)
            visited.add(state)
    return "NOT FOUND 404"
print(dfs(maps, 'ALASKA', 'INDIANA'))