from Node import Node
class UninformedSearchAlgorithm(object):
    def __init__(self, listNodes, searched):
        self.listNodes = listNodes
        self.searched = searched
        self.createQueue()
    def createQueue(self):
        self.queue = []
        self.queue.append(self.listNodes[0])
    def addQueue(self, node):
        pass
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
            raise Exception("La cola esta vacia")
    def matchSearched(self, nodeName):
        if nodeName == self.searched:
            raise Exception("Ciudad encontrada: %s" % nodeName)
    def search(self):
        pass
    def insertNodeChildQueue(self, node):
        childrenNodes = node.getChildrenNodes()
        for child in childrenNodes:
            childNode = self.getNodeFromList(child.name)
            if (isinstance(childNode, Node)):
                self.addQueue(childNode)
Tumbes = Node("Tumbes")
Trujillo = Node("Trujillo")
Moyobamba = Node("Moyobamba")
Iquitos = Node("Iquitos")
Lima = Node("Lima")
Huancayo = Node("Huancayo")
Nazca = Node("Nazca")
Puno = Node("Puno")
Cusco = Node("Cusco")
Arequipa = Node("Arequipa")
Tumbes.addChild(Trujillo)
Tumbes.addChild(Moyobamba)
Tumbes.addChild(Iquitos)
Trujillo.addChild(Lima)
Trujillo.addChild(Huancayo)
Moyobamba.addChild(Huancayo)
Iquitos.addChild(Huancayo)
Iquitos.addChild(Cusco)
Lima.addChild(Nazca)
Huancayo.addChild(Arequipa)
Huancayo.addChild(Puno)
Nazca.addChild(Arequipa)
Puno.addChild(Arequipa)
Cusco.addChild(Arequipa)
search_algorithm = UninformedSearchAlgorithm([Tumbes, Trujillo, Moyobamba, Iquitos, Lima, Huancayo, Nazca, Puno, Cusco, Arequipa], "Arequipa")
try:
    search_algorithm.search()
except Exception as e:
    print(e)