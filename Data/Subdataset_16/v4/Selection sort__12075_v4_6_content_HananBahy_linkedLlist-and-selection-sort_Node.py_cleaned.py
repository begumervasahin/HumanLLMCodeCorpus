class class1:
    def fonk1(self, init_data):
        self.b1 = init_data
        self.b2 = None
    def fonk2(self):
        return self.b1
    def fonk3(self):
        return self.b2
    def fonk4(self, new_data):
        self.b1 = new_data
    def fonk5(self, new_next):
        self.b2 = new_next