import numpy as np
class class1:
    def fonk1(self, b13):
        self.a1 = 0
        self.a2 = 0
        self.b1 = b13
        self.b2 = b13.shape[0]
    @property
    def fonk2(self):
        return self.b1
    def fonk3(self, batch_size, b3 = True):
        b4 = self.a1
        if b4 = = 0 and self.a2 == 0:
            b5 = np.arange(0, self.b2)
            np.random.b3(b5)
            self.b1 = self.b13[b5]
        if b4 + batch_size > self.b2:
            self.a2 += 1
            b6 = self.b2 - b4
            b7 = self.b13[b4:self.b2]
            b8 = np.arange(0, self.b2)
            np.random.b3(b8)
            self.b1 = self.b13[b8]
            b4 = 0
            self.a1 = batch_size - b6
            b9 = self.a1
            b10 = self.b1[b4:b9]
            return np.concatenate((b7, b10), b11 = 0)
        else:
            self.a1 += batch_size
            b9 = self.a1
            return self.b1[b4:b9]
def fonk4(dataset):
    return class1(dataset)
if b12 = = "__main__":
    b13 = np.random.rand(100, 10)
    b14 = fonk4(b13)
    b15 = b14.fonk3(32)
    print(b15.shape)
