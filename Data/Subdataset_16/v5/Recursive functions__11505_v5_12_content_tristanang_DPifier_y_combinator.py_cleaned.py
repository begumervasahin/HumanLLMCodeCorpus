import inspect
class class1:
    def fonk1(self, b4, b1 = False):
        self.b2 = {}
        self.b3 = self.fonk3()
        self.b4 = b4 if b1 else self.fonk6(b4)
    def fonk2(self, *args):
        return self.fonk4(self.b4)(*args)
    def fonk3(self):
        def fonk4(b4):
            def fonk5(*args):
                if args in self.b2:
                    return self.b2[args]
                else:
                    b5 = b4(fonk4(b4))(*args)
                    self.b2[args] = b5
                    return b5
            return g
        return b3
    def fonk6(self, b4):
        b6 = b4.__name__
        b7 = inspect.getsource(b4)
        b8 = b7.replace(b6, 'h', 1).replace(b6 + '(', 'abc(', 1)
        def fonk7(abc):
            exec(b8, {'abc': abc}, globals())
            return h
        return g