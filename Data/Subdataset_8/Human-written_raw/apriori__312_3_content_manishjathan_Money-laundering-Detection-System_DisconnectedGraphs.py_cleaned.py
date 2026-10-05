3. Repository: manishjathan/Money-laundering-Detection-System
   File: DisconnectedGraphs.py
   URL: https:
   Code Content:
import drawGraph as dG
def depthFirstSearch(edgeList,graph,sourceNode):
    dfsStack = []
    exploredStack = [sourceNode]
    while exploredStack != []:
        visitedNode = exploredStack.pop()
        if visitedNode not in dfsStack:
            try:
                dfsStack.append(visitedNode)
            except:
                dfsStack = [visitedNode]
        if visitedNode in graph.keys():
                for val in graph[visitedNode]:
                    try:
                        exploredStack.append(val)
                    except:
                        exploredStack =[val]
    print("Vertices in Graph")
    dfsStack.sort()
    print(dfsStack)
    return dfsStack
def getSourceNodes(indegreeMap):
    print("Source Nodes")
    sourceNodes = []
    for k,v in indegreeMap.items():
        if v == 0:
            try:
                sourceNodes.append(k)
            except:
                sourceNodes = [k]
    print(sourceNodes)
    return sourceNodes
def getDestNodes(outdegreeMap):
    print("Destination Nodes")
    destNodes = []
    for k,v in outdegreeMap.items():
        if v == 0:
            try:
                destNodes.append(k)
            except:
                destNodes = [k]
    print(destNodes)
    return destNodes
def splitEdgeList(edgeList,graph,sourceNodes):
    newEdgeList = []
    for sourceNode in sourceNodes:
        vertexSet = depthFirstSearch(edgeList,graph,sourceNode)
        row = []
        for edge in edgeList:
            if edge[0] in vertexSet and edge[1] in vertexSet:
                try:
                    row.append(edge)
                except:
                    row = [edge]
        try:
            newEdgeList.append(row)
        except:
            newEdgeList =[row]
    print("New Edge Lists after splitting")
    i = 0
    for row in newEdgeList:
        print(row)
        dG.drawGraph(row,"Graph"+str(i)+".png")
        i += 1
    return newEdgeList
   README Content:
This project is built to identify money laundering cases in the layering stage. Basically there are two major techniques that have been applied to do this.First is identification of frequent transactions using Hash based Apriori Algorithm. Frequent transactions are identified by means of threshold values. Second is forming a connection between the involved customers and finding the amount of money laundered.
* run Graph Analysis UI.py
* run Transaction Analysis UI.py
* Download and install Python(v>3).
* Download and install MongoDB and RoboMongo.
* Book1.xlsx contains all the banking transactions.
* Enter the number of records(in UI) you want to work on.(Those many number of record are inserted into MongoDB database)
![Money Laundering System UI](MoneyLaunderingSystemUI.png)
![Graph1](Pdf1.png)
![Graph2](Pdf2.png)
