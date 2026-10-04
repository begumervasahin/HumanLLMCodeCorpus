class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = {}
    def fonk2(self, vertex, weight):
        if not isinstance(vertex, class1):
            raise ValueError("The vertex must be an instance of the class1 class.")
        if not isinstance(weight, (int, float)):
            raise ValueError("The weight must be a numeric value.")
        self.b2[vertex] = weight
    def fonk3(self):
        return f"class1(b1 = {self.b1})"
    def fonk4(self):
        return self.b2