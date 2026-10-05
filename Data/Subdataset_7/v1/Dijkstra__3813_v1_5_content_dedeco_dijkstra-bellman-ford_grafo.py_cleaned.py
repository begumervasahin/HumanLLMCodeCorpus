class class1:
    def fonk1(self, identifier):
        self.b1 = identifier
        self.b2 = {}
    def fonk2(self, b6, b3 = 0):
        self.b2[b6] = b3
    def fonk3(self):
        return self.b2.keys()
    def fonk4(self, b6):
        return self.b2[b6]
class class2:
    def fonk5(self, b4 = False):
        self.b5 = {}
        self.b4 = b4
    def fonk6(self, identifier):
        if identifier not in self.b5:
            b6 = class1(identifier)
            self.b5[identifier] = b6
            return b6
        else:
            return None
    def fonk7(self, source, destination, b3 = 0):
        if source not in self.b5:
            self.fonk6(source)
        if destination not in self.b5:
            self.fonk6(destination)
        self.b5[source].fonk2(self.b5[destination], b3)
        if not self.b4:
            self.b5[destination].fonk2(self.b5[source], b3)
    def fonk8(self):
        return list(self.b5.values())
    def fonk9(self, identifier):
        return self.b5.get(identifier, None)
    def fonk10(self):
        b7 = set()
        for b6 in self.b5.values():
            for adjacent_vertex, b3 in b6.b2.items():
                b7.add((b6.b1, adjacent_vertex.b1, b3))
        return b7
    def fonk11(self):
        return iter(self.b5.values())
