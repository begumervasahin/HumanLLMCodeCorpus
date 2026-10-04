import inspect
class class1:
    def fonk1(self, b4, b1 = False):
        self.b2 = {}
        def fonk2(b4):
            def fonk3(*args):
                if args in self.b2:
                    return self.b2[args]
                else:
                    self.b2[args] = b4(fonk2(b4))(*args)
                    return self.b2[args]
            return g
        self.b3 = b3
        if b1:
            self.b4 = b4
        else:
            self.b4 = self.fonk5(b4)
    def fonk4(self, *args):
        return self.fonk2(self.b4)(*args)
    def fonk5(self, b4):
        b5 = b4.__name__
        b6 = inspect.getsource(b4)
        b6 = b6.replace(b5, 'h', 1)
        b6 = b6.replace(b5 + '(', 'abc(', 1)
        def fonk6(abc):
            exec(b6, {'abc': abc}, globals())
            return h
        return g