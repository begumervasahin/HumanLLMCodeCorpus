from Node import Node
class UninformedSearchAlgorithm:
    def __init__(self, listNodes, searched):
        self.listNodes = listNodes
        self.searched = searched
        self.createQueue()
    def createQueue(self):
        self.queue = []
        self.queue.append(self.listNodes[0])
    def readQueue(self):
        return self.queue.pop(0)
    def getQueueLen(self):
        return len(self.queue)
    def getNodeFromList(self, name):
        for node in self.listNodes:
            if node.name == name:
                return node
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