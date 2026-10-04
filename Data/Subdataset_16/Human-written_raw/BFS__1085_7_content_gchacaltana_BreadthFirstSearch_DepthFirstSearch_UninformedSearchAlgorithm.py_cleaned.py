7. Repository: gchacaltana/BreadthFirstSearch_DepthFirstSearch
   File: UninformedSearchAlgorithm.py
   URL: https:
   Code Content:
b1 = "Gonzalo Chacaltana Buleje"
b2 = "gchacaltanab@gmail.com"
from Node import Node
class class1(object):
    def fonk1(self, b3, b4):
        self.b3 = b3
        self.b4 = b4
        self.fonk2()
    def fonk2(self):
        self.b5 = []
        self.b5.append(self.b3[0])
    def fonk3(self, node):
        pass
    def fonk4(self):
        return self.b5.pop(0)
    def fonk5(self):
        return len(self.b5)
    def fonk6(self, b6):
        for node in self.b3:
            if node.b6 = = b6:
                return node
    def fonk7(self):
        if self.fonk5() == 0:
            raise Exception("La cola esta vacia")
    def fonk8(self, b7):
        if b7 = = self.b4:
            raise Exception("Ciudad encontrada: %s" % b7)
    def fonk9(self):
        pass
    def fonk10(self, node):
        b8 = node.getChildrenNodes()
        for child in b8:
            b9 = self.fonk6(child.b6)
            if (isinstance(b9, Node)):
                self.fonk3(b9)
   README Content:
**BFS** = BreadthFirstSearch
**DFS** = DepthFirstSearch
        python App.py
Implementar los algoritmos DFS y BFS para encontrar el camino del viajero de la ciudad de Tumbes hacia la ciudad de Arequipa segÃºn el mapa.
![Ruta de un viajero](http:
*CrÃ©ditos: Mirko Rodriguez.*
        {
            "Tumbes": {
                "Trujillo": null,
                "Moyobamba": null,
                "Iquitos": null
            },
            "Trujillo": {
                "Lima": null,
                "Huancayo": null
            },
            "Moyobamba": {
                "Huancayo": null
            },
            "Iquitos": {
                "Huancayo": null,
                "Cusco": null
            },
            "Lima": {
                "Nazca": null
            },
            "Huancayo": {
                "Arequipa": null,
                "Puno": null
            },
            "Nazca": {
                "Arequipa": null
            },
            "Puno": {
                "Arequipa": null
            },
            "Cusco": {
                "Arequipa": null
            },
            "Arequipa": {
                "Arequipa":null
            }
        }
