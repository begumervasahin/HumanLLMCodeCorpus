
import collections
adjList = {}
fileName = "wrestler2.txt"
with open(fileName, "r") as f:
    lines = f.readlines()
    num = int(lines[0])
    numRivals = int(lines[num + 1])
    for count, line in enumerate(lines):
        if count > num + 2 and count <= num + 2 + numRivals:
            wrestler1, wrestler2 = line.strip().split()
            adjList.setdefault(wrestler1, []).append(wrestler2)
            adjList.setdefault(wrestler2, []).append(wrestler1)
babyFaces = []
heels = []
def BFS(graph, source):
    doneChecking = []
    queue = collections.deque([source])
    depth = {source: 0}
    visited = {source}
    while queue:
        vertex = queue.popleft()
        doneChecking.append(vertex)
        if depth[vertex] % 2 == 0:
            babyFaces.append(vertex)
        else:
            heels.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                depth[neighbor] = depth[vertex] + 1
    return doneChecking
first_key = list(adjList.keys())[0]
checked = BFS(adjList, first_key)
for key in adjList:
    if key not in checked:
        checked += BFS(adjList, key)
numBabyFaces = len(babyFaces)
numHeels = len(heels)
if numBabyFaces == numHeels:
    print("Yes, possible")
    print("Baby Faces:", babyFaces)
    print("Heels:", heels)
else:
    print("Not possible")