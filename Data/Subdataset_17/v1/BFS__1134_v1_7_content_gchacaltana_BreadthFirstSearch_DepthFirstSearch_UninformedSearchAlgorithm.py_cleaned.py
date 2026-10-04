class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
    def addChild(self, childNode):
        self.children.append(childNode)
    def getChildrenNodes(self):
        return self.children
class UninformedSearchAlgorithm:
    def __init__(self, listNodes, searched):
        self.listNodes = listNodes
        self.searched = searched
        self.createQueue()
    def createQueue(self):
        self.queue = []
        self.queue.append(self.listNodes[0])
    def addQueue(self, node):
        self.queue.append(node)
    def readQueue(self):
        return self.queue.pop(0)
    def getQueueLen(self):
        return len(self.queue)
    def getNodeFromList(self, name):
        for node in self.listNodes:
            if node.name == name:
                return node
    def validateLenQueue(self):
        if self.getQueueLen() == 0:
            raise Exception("The queue is empty")
    def matchSearched(self, nodeName):
        if nodeName == self.searched:
            raise Exception("City found: %s" % nodeName)
    def search(self):
        pass
    def insertNodeChildQueue(self, node):
        childrenNodes = node.getChildrenNodes()
        for child in childrenNodes:
            childNode = self.getNodeFromList(child.name)
            if isinstance(childNode, Node):
                self.addQueue(childNode)
class BreadthFirstSearch(UninformedSearchAlgorithm):
    def addQueue(self, node):
        self.queue.append(node)
    def search(self):
        while True:
            self.validateLenQueue()
            node = self.readQueue()
            self.matchSearched(node.name)
            self.insertNodeChildQueue(node)
class DepthFirstSearch(UninformedSearchAlgorithm):
    def addQueue(self, node):
        self.queue.insert(0, node)
    def search(self):
        while True:
            self.validateLenQueue()
            node = self.readQueue()
            self.matchSearched(node.name)
            self.insertNodeChildQueue(node)
import json
from Node import Node
from UninformedSearchAlgorithm import BreadthFirstSearch, DepthFirstSearch
def createGraph(routes):
    nodes = {}
    for city, connections in routes.items():
        if city not in nodes:
            nodes[city] = Node(city)
        for connection in connections:
            if connection not in nodes:
                nodes[connection] = Node(connection)
            nodes[city].addChild(nodes[connection])
    return list(nodes.values())
def main():
    routes = {
        "Tumbes": {"Trujillo": None, "Moyobamba": None, "Iquitos": None},
        "Trujillo": {"Lima": None, "Huancayo": None},
        "Moyobamba": {"Huancayo": None},
        "Iquitos": {"Huancayo": None, "Cusco": None},
        "Lima": {"Nazca": None},
        "Huancayo": {"Arequipa": None, "Puno": None},
        "Nazca": {"Arequipa": None},
        "Puno": {"Arequipa": None},
        "Cusco": {"Arequipa": None},
        "Arequipa": {"Arequipa": None}
    }
    nodes = createGraph(routes)
    print("Breadth-First Search")
    bfs = BreadthFirstSearch(nodes, "Arequipa")
    try:
        bfs.search()
    except Exception as e:
        print(e)
    print("\nDepth-First Search")
    dfs = DepthFirstSearch(nodes, "Arequipa")
    try:
        dfs.search()
    except Exception as e:
        print(e)
if __name__ == "__main__":
    main()