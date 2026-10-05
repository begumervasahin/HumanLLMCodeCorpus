class class1:
    def fonk1(self, b4):
        self.b1 = None
        self.b2 = None
        self.b3 = None
        self.b4 = b4
    def fonk2(self, child_node):
        self.b1 = child_node
        child_node.b3 = self
    def fonk3(self, child_node):
        self.b2 = child_node
        child_node.b3 = self
    def fonk4(self):
        print(self.b1)
    def fonk5(self):
        print(self.b2)
    def fonk6(self):
        print(self.b4)
    def fonk7(self):
        print(self.b3)