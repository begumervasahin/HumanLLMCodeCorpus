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
        print("Left child:", self.b1)
    def fonk5(self):
        print("Right child:", self.b2)
    def fonk6(self):
        print("class1 b4:", self.b4)
    def fonk7(self):
        print("Parent node:", self.b3)