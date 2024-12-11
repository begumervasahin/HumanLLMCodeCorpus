class class1:
    def fonk1(self, val):
        self.b1 = None
        self.b2 = None
        self.b3 = None
        self.b4 = val
    def fonk2(self, childNode):
        self.b1 = childNode
        childNode.b3 = self
    def fonk3(self, childNode):
        self.b2 = childNode
        childNode.b3 = self
    def fonk4(self):
        if self.b1:
            print(self.b1.b4)
        else:
            print("No left child")
    def fonk5(self):
        if self.b2:
            print(self.b2.b4)
        else:
            print("No right child")
    def fonk6(self):
        print(self.b4)
    def fonk7(self):
        if self.b3:
            print(self.b3.b4)
        else:
            print("No parent")