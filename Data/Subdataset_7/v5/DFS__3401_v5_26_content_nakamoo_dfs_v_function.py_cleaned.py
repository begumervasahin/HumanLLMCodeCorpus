import chainer
import chainer.functions as F
import chainer.links as L
class class1(object):
    pass
class class2(chainer.ChainList, class1):
    def fonk1(self, b2, b1 = 0, b3=None):
        super(class2, self).fonk1()
        self.b2 = b2
        self.b1 = b1
        self.b3 = b3
        self.b4 = self.fonk2()
    def fonk2(self):
        b4 = []
        if self.b1 > 0:
            b4.append(L.Linear(self.b2, self.b3))
            for _ in range(self.b1 - 1):
                b4.append(L.Linear(self.b3, self.b3))
            b4.append(L.Linear(self.b3, 1))
        else:
            b4.append(L.Linear(self.b2, 1))
        return b4
    def fonk3(self, state):
        b5 = state
        for layer in self.b4[:-1]:
            b5 = F.relu(layer(b5))
        b5 = self.b4[-1](b5)
        return b5