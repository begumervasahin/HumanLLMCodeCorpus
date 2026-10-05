class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
        self.b4 = None
    def fonk2(self, child_node):
        self.b2 = child_node
        child_node.b4 = self
    def fonk3(self, child_node):
        self.b3 = child_node
        child_node.b4 = self
    def fonk4(self):
        if self.b2:
            print("Left Child:", self.b2.b1)
        else:
            print("No b2 child")
    def fonk5(self):
        if self.b3:
            print("Right Child:", self.b3.b1)
        else:
            print("No b3 child")
    def fonk6(self):
        print("class1 Value:", self.b1)
    def fonk7(self):
        if self.b4:
            print("Parent class1:", self.b4.b1)
        else:
            print("No b4 node")