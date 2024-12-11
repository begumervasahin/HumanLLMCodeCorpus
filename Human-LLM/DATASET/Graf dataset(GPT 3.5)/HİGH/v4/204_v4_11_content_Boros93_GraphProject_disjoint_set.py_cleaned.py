class class1:
    def fonk1(self, init_arr):
        self.b1 = []
        if init_arr:
            for item in list(set(init_arr)):
                self.b1.append([item])
    def fonk2(self, elem):
        for item in self.b1:
            if elem in item:
                return self.b1.index(item)
        return None
    def fonk3(self, elem):
        for item in self.b1:
            if elem in item:
                return self.b1[self.b1.index(item)]
        return None
    def fonk4(self, elem1, elem2):
        b2 = self.fonk2(elem1)
        b3 = self.fonk2(elem2)
        if b2 != b3 and b2 is not None and b3 is not None:
            self.b1[b3] = self.b1[b3] + self.b1[b2]
            del self.b1[b2]
        return self.b1
    def fonk5(self):
        return self.b1