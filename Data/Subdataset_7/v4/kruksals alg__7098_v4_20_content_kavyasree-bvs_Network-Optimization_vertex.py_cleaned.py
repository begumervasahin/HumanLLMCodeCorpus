class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = []
    def fonk2(self, neighbor):
        if isinstance(neighbor, class1):
            if neighbor.b1 not in self.b2:
                self.b2.append(neighbor.b1)
                neighbor.b2.append(self.b1)
                self.b2.sort()
                neighbor.b2.sort()
        else:
            return False
    def fonk3(self):
        return str(self.b2)