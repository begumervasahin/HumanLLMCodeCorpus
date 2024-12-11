import basicfunc
class class1(object):
    def fonk1(self, b1, b2):
        assert b1.is_valid(b2)
        self.b1 = b1
        self.b2 = b2
        self.b3 = b1.order(b2)
        pass
    def fonk2(self, priv, b2):
        return self.b1.mul(b2, priv)
    def fonk3(self, plain, pub, b2, r):
        assert self.b1.is_valid(plain)
        assert self.b1.is_valid(pub)
        return (self.b1.mul(b2, r), self.b1.add(plain, self.b1.mul(pub, r)))
    def fonk4(self, cipher, priv, b1):
        c1, b4 = cipher
        assert self.b1.is_valid(c1) and b1.is_valid(b4)
        return self.b1.add(b4, self.b1.neg(self.b1.mul(c1, priv)))
    pass