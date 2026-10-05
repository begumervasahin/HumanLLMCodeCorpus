import numpy as np
class class1:
    def fonk1(self, data):
        self.a1 = 0
        self.a2 = 0
        self.b1 = data
        self.b2 = data.shape[0]
    @property
    def fonk2(self):
        return self.b1
    def fonk3(self, batch_size, b3 = True):
        b4 = self.a1
        if b4 = = 0 and self.a2 == 0:
            self.fonk4()
        if b4 + batch_size > self.b2:
            self.a2 += 1
            b5 = self.b2 - b4
            b6 = self.b1[b4:self.b2]
            self.fonk4()
            b4 = 0
            self.a1 = batch_size - b5
            b7 = self.a1
            b8 = self.b1[b4:b7]
            return np.concatenate((b6, b8), b9 = 0)
        else:
            self.a1 += batch_size
            b7 = self.a1
            return self.b1[b4:b7]
    def fonk4(self):
        b10 = np.arange(0, self.b2)
        np.random.b3(b10)
        self.b1 = self.b1[b10]
def fonk5(dataset):
    return class1(dataset)