51. Repository: rrraharja/Kecerdasan-Buatan-AI
   File: Project DFS.py
   URL: https:
   Code Content:
maps =  {'ALASKA':set(['CALIFORNIA']),
         'CALIFORNIA':set(['CAROLINA','ALASKA']),
         'CAROLINA':set(['CALIFORNIA','INDIANA','HAWAII','DAREWALE']),
         'DAREWALE':set(['CAROLINA','EDINBURH','HAWAII','FLORIDA']),
         'EDINBURGH':set(['DAREWALE']),
         'FLORIDA':set(['DAREWALE','GEORGIA']),
         'GEORGIA':set(['FLORIDA','HAWAII']),
         'HAWAII':set(['DARAWALE','CAROLINA','GEORGIA','LOUSIANA']),
         'INDIANA':set(['CAROLINA','IDAKO','KENTUCKY']),
         'IDAKO':set(['INDIANA']),
         'KENTUCKY':set(['LOUSIANA','INDIANA']),
         'LOUSIANA':set(['KENTUCKY','HAWAII'])}
def dfs(graf, start, finish):
    stack = [[start]]
    visited = set()
    while stack:
        longofstack = len(stack)-1
        path = stack.pop(longofstack)
        state = path[-1]
        if state == finish:
            return path
        elif state not in visited:
            for branch in graf.get(state, []):
                new_path = list(path)
                new_path.append(branch)
                stack.append(new_path)
            visited.add(state)
        content = len(stack)
        if content == 0:
            print("NOT FOUND 404")
print(dfs(maps,'ALASKA','INDIANA'))
   README Content:
BFS dan DFS
