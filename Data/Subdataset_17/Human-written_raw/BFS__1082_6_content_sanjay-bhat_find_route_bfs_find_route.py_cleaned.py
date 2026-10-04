6. Repository: sanjay-bhat/find_route_bfs
   File: find_route.py
   URL: https:
   Code Content:
import romania
import sys
class find_route:
    def findRoute(self):
        fileInput = sys.argv[1]
        dest1 = sys.argv[2]
        dest2 = sys.argv[3]
        totalDistance = 0
        stack = []
        biDirGraph = romania.romania(0).getDataRomania(fileInput)
        graph = biDirGraph[0]
        vertices = biDirGraph[1]
        visited = [False] * vertices
        for i in range(vertices):
            if visited[i] == False:
                self.sort(graph, dest1, visited, stack)
        dist = [float("Inf")] * vertices
        dist[graph.keys().index(dest1)] = 0.0
        fromCity = [0] * vertices
        toCity = [0] * vertices
        toFroDist = [0] * vertices
        while stack:
            pos = stack.pop()
            for destination, distance in graph[pos]:
                cumilativeDistance = float(dist[graph.keys().index(pos)]) + float(distance)
                if float(dist[graph.keys().index(destination)]) > cumilativeDistance:
                    dist[graph.keys().index(destination)] = cumilativeDistance
                    fromCity[graph.keys().index(destination)] = pos
                    toCity[graph.keys().index(destination)] = destination
                    toFroDist[graph.keys().index(destination)] = float(distance)
                    if destination == dest2:
                        totalDistance = cumilativeDistance
        pos = 0
        returnStr = []
        finalDist = totalDistance
        while totalDistance != 0:
            if toCity[pos] == dest2:
                    returnStr.append(fromCity[pos])
                    returnStr.append(toCity[pos])
                    returnStr.append(str(toFroDist[pos]))
                    totalDistance = dist[pos] - toFroDist[pos]
                    dest2 = fromCity[pos]
                    pos = 0
            else:
                pos = pos + 1
        returnStr.reverse()
        if finalDist == 0:
            pathStr = "distance: infinity\nroute:\nnone\n"
        else:
            pathStr = "distance: " + str(finalDist) + " km\n" + "route:\n"
            pos = 0
            while pos < len(returnStr):
                pathStr += returnStr[pos + 2] + " to " + returnStr[pos + 1] + ", " + returnStr[pos] + " km\n"
                pos = pos + 3
        print pathStr
    def sort(self, graph, dest1, visited, stack):
        visited[graph.keys().index(dest1)] = True
        if dest1 in graph.keys():
            for d, distance in graph[dest1]:
                if visited[graph.keys().index(d)] == False:
                    self.sort(graph, d, visited, stack)
        stack.append(dest1)
def main():
    obj = find_route()
    obj.findRoute()
if __name__ == "__main__":
    main()
   README Content:
find_route_bfs
======
[![Build Status](https:
find-route calculates optimal distance between two vertices by also taking into accont thier weights. In this case the vertices are cities and weights are distances between them and we use BSF in an attempt to find shortest route between any 2 given cities provided a path exists.
Files included
--------------
1. romania.py - Contains the details on converting the text containing vertices and their respective distances into graph.
2. find_route.py - Find the optimal path between destination 1 and destination 2, i.e: source and destination, using BSF
3. input1.txt - File containing vertices and their respective distances
Steps to run the code
---------------------
1. Place the files [1], [2] and [3] in desired directory and change permissions of all the 3 files from existing (0644) permissions to -rwxrwxrwx, i.e: 0777.
2. Open terminal.
3. Traverse to the directory where the files are held using 'cd'.
4. Invoke the code using the following command, '[san @ubuntu]$ python find_route.py input1.txt Berlin Munich' and hit enter to find the BFS shortest path between Berlin and Munich.
5. Change input1.txt file and cities following it as per need.
