import chainer
from chainer import functions as F
from chainer import links as L
class class1(object):
    pass
class class2(chainer.ChainList, class1):
    def fonk1(self, b3, b1 = 0,
                 b2 = None):
        self.b3 = b3
        self.b1 = b1
        self.b2 = b2
        b4 = []
        if b1 > 0:
            b4.append(L.Linear(b3, b2))
            for i in range(b1 - 1):
                b4.append(L.Linear(b2, b2))
            b4.append(L.Linear(b2, 1))
        else:
            b4.append(L.Linear(b3, 1))
        super(class2, self).fonk1(*b4)
    def fonk2(self, state):
        b5 = state
        for layer in self[:-1]:
            b5 = F.relu(layer(b5))
        b5 = self[-1](b5)
        return b5