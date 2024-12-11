class class1:
    def fonk1(self, b2, b1 = None):
        self.b2 = b2
        self.b3 = b1 if b1 else {}
    def fonk2(self, other):
        return sum(self.b3[d] * other.b3[d] for d in self.b2)
    def fonk3(self, other):
        return class1(self.b2, {d: other * self.b3[d] for d in self.b2})
def fonk4(b6, v, b4 = 1E-20):
    b5 = ((b6 * v) / (v * v)) if v * v > b4 else 0
    return b5 * v
def fonk5(b6, vlist):
    for v in vlist:
        b6 = b6 - fonk4(b6, v)
    return b6
def fonk6(b6, vlist, b4 = 1E-20):
    b7 = {len(vlist): 1}
    for i, v in enumerate(vlist):
        b5 = (b6 * v) / (v * v) if v * v > b4 else 0
        b7[i] = b5
        b6 = b6 - b5 * v
    return b6, b7
def fonk7(vlist):
    assert isinstance(vlist, list)
    b8 = []
    for v in vlist:
        b8.append(fonk5(v, b8))
    return b8
def fonk8(vlist):
    assert isinstance(vlist, list)
    b8 = []
    b9 = []
    b2 = set(range(len(vlist)))
    for v in vlist:
        vstar, b10 = fonk6(v, b8)
        b8.append(vstar)
        b9.append(class1(b2, b10))
    return b8, b9