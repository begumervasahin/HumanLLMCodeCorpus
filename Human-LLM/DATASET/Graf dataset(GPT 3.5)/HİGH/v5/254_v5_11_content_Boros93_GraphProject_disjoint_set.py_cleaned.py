class class1:
    def fonk1(self, init_arr):
        self.b1 = []
        if init_arr:
            self.fonk2(init_arr)
    def fonk2(self, arr):
        b2 = set(arr)
        self.b1 = [[item] for item in b2]
    def fonk3(self, elem):
        for index, item in enumerate(self.b1):
            if elem in item:
                return index
        return None
    def fonk4(self, elem):
        for item in self.b1:
            if elem in item:
                return item
        return None
    def fonk5(self, elem1, elem2):
        b3 = self.fonk3(elem1)
        b4 = self.fonk3(elem2)
        if b3 is not None and b4 is not None and b3 != b4:
            self.b1[b4] += self.b1[b3]
            del self.b1[b3]
        return self.b1
    def fonk6(self):
        return self.b1