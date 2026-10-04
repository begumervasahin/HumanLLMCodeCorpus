from sklearn.linear_model import SGDClassifier
class class1:
    def fonk1(self, b1, b2, b3, b4, b5, b6):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.b6 = b6
        if self.b1 is not None and self.b3 is not None:
            self.b6.fit(self.b1, self.b3)
    def fonk2(self, data):
        return self.b6.fonk2(data)
    def fonk3(self):
        if self.b2 is not None and self.b4 is not None:
            return self.b6.fonk3(self.b2, self.b4)
        return None
class class2:
    def fonk4(self):
        self.b5 = None
        self.b4 = None
        self.b3 = None
        self.b2 = None
        self.b1 = None
        self.b6 = SGDClassifier()
    def fonk5(self, b1):
        self.b1 = b1
        return self
    def fonk6(self, b3):
        self.b3 = b3
        return self
    def fonk7(self, b2):
        self.b2 = b2
        return self
    def fonk8(self, b4):
        self.b4 = b4
        return self
    def fonk9(self, b5):
        self.b5 = b5
        return self
    def fonk10(self) -> class1:
        return class1(
            self.b1,
            self.b2,
            self.b3,
            self.b4,
            self.b5,
            self.b6
        )
def fonk11():
    b1 = [[0.1, 0.2], [0.2, 0.3], [0.3, 0.4]]
    b3 = [0, 1, 0]
    b2 = [[0.2, 0.1], [0.3, 0.2]]
    b4 = [0, 1]
    b7 = (class2()
                 .fonk5(b1)
                 .fonk6(b3)
                 .fonk7(b2)
                 .fonk8(b4)
                 .fonk9(None)
                 .fonk10())
    b8 = b7.fonk2(b2)
    b9 = b7.fonk3()
    print(f"Predictions: {b8}")
    print(f"Score: {b9}")
if b10 = = "__main__":
    fonk11()