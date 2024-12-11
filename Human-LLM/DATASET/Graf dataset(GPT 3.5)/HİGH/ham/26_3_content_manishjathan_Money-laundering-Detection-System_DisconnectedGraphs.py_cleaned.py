3. Repository: manishjathan/Money-laundering-Detection-System
   File: DisconnectedGraphs.py
   URL: https:
   Code Content:
import drawGraph as dG
def fonk1(edgeList,graph,sourceNode):
    b1 = []
    b2 = [sourceNode]
    while b2 != []:
        b3 = b2.pop()
        if b3 not in b1:
            try:
                b1.append(b3)
            except:
                b1 = [b3]
        if b3 in graph.keys():
                for val in graph[b3]:
                    try:
                        b2.append(val)
                    except:
                        b2 = [val]
    print("Vertices in Graph")
    b1.sort()
    print(b1)
    return b1
def fonk2(indegreeMap):
    print("Source Nodes")
    b4 = []
    for k,b5 in indegreeMap.items():
        if b5 = = 0:
            try:
                b4.append(k)
            except:
                b4 = [k]
    print(b4)
    return b4
def fonk3(outdegreeMap):
    print("Destination Nodes")
    b6 = []
    for k,b5 in outdegreeMap.items():
        if b5 = = 0:
            try:
                b6.append(k)
            except:
                b6 = [k]
    print(b6)
    return b6
def fonk4(edgeList,graph,b4):
    b7 = []
    for sourceNode in b4:
        b8 = fonk1(edgeList,graph,sourceNode)
        b9 = []
        for edge in edgeList:
            if edge[0] in b8 and edge[1] in b8:
                try:
                    b9.append(edge)
                except:
                    b9 = [edge]
        try:
            b7.append(b9)
        except:
            b7 = [b9]
    print("New Edge Lists after splitting")
    a1 = 0
    for b9 in b7:
        print(b9)
        dG.drawGraph(b9,"Graph"+str(a1)+".png")
        a1 += 1
    return b7
   README Content:
This project is built to identify money laundering cases in the layering stage. Basically there are two major techniques that have been applied to do this.First is identification of frequent transactions using Hash based Apriori Algorithm. Frequent transactions are identified by means of threshold values. Second is forming a connection between the involved customers and finding the amount of money laundered.
* run Graph Analysis UI.py
* run Transaction Analysis UI.py
* Download and install Python(b5>3).
* Download and install MongoDB and RoboMongo.
* Book1.xlsx contains all the banking transactions.
* Enter the number of records(in UI) you want to work on.(Those many number of record are inserted into MongoDB database)
![Money Laundering System UI](MoneyLaunderingSystemUI.png)
![Graph1](Pdf1.png)
![Graph2](Pdf2.png)
