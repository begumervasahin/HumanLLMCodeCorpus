import romania
import sys
class FindRoute:
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
            if not visited[i]:
                self.sort(graph, dest1, visited, stack)
        dist = [float("Inf")] * vertices
        dist[list(graph.keys()).index(dest1)] = 0.0
        fromCity = [0] * vertices
        toCity = [0] * vertices
        toFroDist = [0] * vertices
        while stack:
            pos = stack.pop()
            for destination, distance in graph[pos]:
                cumulativeDistance = float(dist[list(graph.keys()).index(pos)]) + float(distance)
                if float(dist[list(graph.keys()).index(destination)]) > cumulativeDistance:
                    dist[list(graph.keys()).index(destination)] = cumulativeDistance
                    fromCity[list(graph.keys()).index(destination)] = pos
                    toCity[list(graph.keys()).index(destination)] = destination
                    toFroDist[list(graph.keys()).index(destination)] = float(distance)
                    if destination == dest2:
                        totalDistance = cumulativeDistance
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
                pos += 1
        returnStr.reverse()
        if finalDist == 0:
            pathStr = "distance: infinity\nroute:\nnone\n"
        else:
            pathStr = "distance: " + str(finalDist) + " km\n" + "route:\n"
            pos = 0
            while pos < len(returnStr):
                pathStr += returnStr[pos + 2] + " to " + returnStr[pos + 1] + ", " + returnStr[pos] + " km\n"
                pos += 3
        print(pathStr)
    def sort(self, graph, dest1, visited, stack):
        visited[list(graph.keys()).index(dest1)] = True
        if dest1 in graph.keys():
            for d, distance in graph[dest1]:
                if not visited[list(graph.keys()).index(d)]:
                    self.sort(graph, d, visited, stack)
        stack.append(dest1)
def main():
    obj = FindRoute()
    obj.findRoute()
if __name__ == "__main__":
    main()