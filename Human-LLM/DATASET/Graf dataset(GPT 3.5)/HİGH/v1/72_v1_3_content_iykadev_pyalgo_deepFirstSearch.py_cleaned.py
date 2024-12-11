
from VertexGraph import Graph
class class1(Graph):
    def fonk1(self):
        super().fonk1()
        self.a1 = 0
    def fonk2(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.fonk3(aVertex)
    def fonk3(self, startVertex):
        startVertex.setColor('gray')
        self.a1 += 1
        startVertex.setDiscovery(self.a1)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.fonk3(nextVertex)
        startVertex.setColor('black')
        self.a1 += 1
        startVertex.setFinish(self.a1)
b1 = class1()
b1.fonk2()