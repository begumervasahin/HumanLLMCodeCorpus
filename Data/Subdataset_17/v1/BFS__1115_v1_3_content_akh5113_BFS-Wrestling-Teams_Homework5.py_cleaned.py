
import collections
adjList = {}
fileName = "wrestler2.txt"
with open(fileName, "r") as f:
    lines = f.readlines()
    num = int(lines[0])
    numRivals = int(lines[num+1])
    count = 0
    innerCount = 1
    for x in lines:
        count += 1
        if count > num + 2 and innerCount <= numRivals:
            var = x.strip('\n')
            var = var.split(" ")
            adjList.setdefault(var[0], []).append(var[1])
            adjList.setdefault(var[1], []).append(var[0])
            innerCount += 1
babyFaces = []
heels = []
def BFS(graph, source):
    doneChecking = []
    queue = [source]
    depth = {}
    depth[source] = 0
    visited = [source]
    while queue:
        vertex = queue.pop(0)
        doneChecking.append(vertex)
        if depth[vertex] % 2 == 0:
            babyFaces.append(vertex)
        else:
            heels.append(vertex)
        neighbors = graph[vertex]
        for neighbor in neighbors:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)
                depth[neighbor] = depth[vertex] + 1
    return doneChecking
key = list(adjList.keys())[0]
checked = BFS(adjList, key)
i = 0
for keys in adjList:
    if keys in checked:
        i += 1
    else:
        key2 = list(adjList.keys())[i]
        checked2 = BFS(adjList, key2)
        for x in checked2:
            checked.append(x)
        i += 1
numBabyFaces = len(babyFaces)
numHeels = len(heels)
if numBabyFaces == numHeels:
    print("Yes, possible")
    print("Baby Faces: ", babyFaces)
    print("Heels: ", heels)
else:
    print("Not possible")
