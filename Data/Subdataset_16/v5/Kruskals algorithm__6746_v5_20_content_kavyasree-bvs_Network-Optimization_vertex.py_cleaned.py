class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = []
    def fonk2(self, neighbor):
        if not isinstance(neighbor, class1):
            return False
        if neighbor.b1 not in self.b2:
            self.b2.append(neighbor.b1)
            neighbor.b2.append(self.b1)
            self.b2.sort()
            neighbor.b2.sort()
    def fonk3(self):
        return f"class1({self.b1}): Neighbors -> {self.b2}"