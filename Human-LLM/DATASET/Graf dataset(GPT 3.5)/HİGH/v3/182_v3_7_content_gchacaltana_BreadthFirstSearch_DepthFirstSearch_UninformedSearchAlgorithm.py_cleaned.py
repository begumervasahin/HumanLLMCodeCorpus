from Node import Node
class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
        self.fonk2()
    def fonk2(self):
        self.b3 = [self.b1[0]]
    def fonk3(self):
        return self.b3.pop(0)
    def fonk4(self):
        return len(self.b3)
    def fonk5(self, b4):
        for node in self.b1:
            if node.b4 = = b4:
                return node
    def fonk6(self):
        if not self.b3:
            raise Exception("The b3 is empty")
    def fonk7(self, b5):
        if b5 = = self.b2:
            raise Exception("City found: %s" % b5)
    def fonk8(self):
        pass
    def fonk9(self, node):
        b6 = node.get_children_nodes()
        for child in b6:
            b7 = self.fonk5(child.b4)
            if isinstance(b7, Node):
                self.fonk10(b7)
    def fonk10(self, node):
        self.b3.append(node)
if b8 = = "__main__":
    b9 = {
        "Tumbes": Node("Tumbes"),
        "Trujillo": Node("Trujillo"),
        "Moyobamba": Node("Moyobamba"),
        "Iquitos": Node("Iquitos"),
        "Lima": Node("Lima"),
        "Huancayo": Node("Huancayo"),
        "Nazca": Node("Nazca"),
        "Puno": Node("Puno"),
        "Cusco": Node("Cusco"),
        "Arequipa": Node("Arequipa")
    }
    b9["Tumbes"].add_child(b9["Trujillo"])
    b9["Tumbes"].add_child(b9["Moyobamba"])
    b9["Tumbes"].add_child(b9["Iquitos"])
    b9["Trujillo"].add_child(b9["Lima"])
    b9["Trujillo"].add_child(b9["Huancayo"])
    b9["Moyobamba"].add_child(b9["Huancayo"])
    b9["Iquitos"].add_child(b9["Huancayo"])
    b9["Iquitos"].add_child(b9["Cusco"])
    b9["Lima"].add_child(b9["Nazca"])
    b9["Huancayo"].add_child(b9["Arequipa"])
    b9["Huancayo"].add_child(b9["Puno"])
    b9["Nazca"].add_child(b9["Arequipa"])
    b9["Puno"].add_child(b9["Arequipa"])
    b9["Cusco"].add_child(b9["Arequipa"])
    b10 = class1(b9.values(), "Arequipa")
    try:
        b10.fonk8()
    except Exception as e:
        print(e)