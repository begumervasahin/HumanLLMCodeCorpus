3. Repository: akh5113/BFS-Wrestling-Teams
   File: Homework5.py
   URL: https:
   Code Content:
adjList = {}
fileName = "wrestler2.txt"
with open(fileName, "r") as f:
    lines = f.readlines()
    num = int(lines[0])
    numRivals = int(lines[num+1])
    count = 0
    innerCount = 1
    for x in lines:
        count +=1
        if count > num+2 and innerCount <= numRivals:
            var = x.strip('\n')
            var = var.split(" ")
            adjList.setdefault(var[0],[]).append(var[1])
            adjList.setdefault(var[1],[]).append(var[0])
            innerCount += 1
babyFaces = []
heel = []
def BFS(graph, source):
    doneChecking = []
    queue = [source]
    depth = {}
    depth[source] = 0
    visited = [source]
    while queue:
        vertex = queue.pop(0)
        doneChecking.append(vertex)
        if depth[vertex]%2 == 0:
            babyFaces.append(vertex)
        else:
            heel.append(vertex)
        neighbors = graph[vertex]
        for neighbor in neighbors:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)
                depth[neighbor] = depth[vertex]+1
    return doneChecking
key = list(adjList.keys())[0]
checked = BFS(adjList, key)
i = 0
for keys in adjList:
    if keys in checked:
        i += 1
    else:
        key2 = list(adjList.keys())[i]
        checked2 = BFS(adjList,key2)
        for x in checked2:
            checked.append(x)
        i += 1
numBabyFaces = len(babyFaces)
numHeels = len(heel)
if numBabyFaces == numHeels:
    print("Yes, possible")
    print("Baby Faces: ", babyFaces)
    print("Heels: ", heel)
else:
    print("Not possible")
   README Content:
Anne Harris
CS 325-400
Homework 5 - README
This program takes in a txt file of wrestlers, which lists their rivalries,
and uses a breadth-first search algorithm to determine if it's possible to
designate some as "baby faces" and some as "heels", such that each rivalry is
between a baby face and a heel.
This program reads in a text file in the format:
[number of players]
[player 1]
[player 2]
.
.
.
[player n]
[number of rivalries]
[rivalry 1]
[rivalry 2]
.
.
.
[rivalry n]
[comments]
This file will default to run with a text file called "wrestler.txt". To change
this, change the fileName variable in line 14
To run this program on flip, type: "python3 Homework5.py"
