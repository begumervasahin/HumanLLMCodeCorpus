import inspect
class class1:
    def fonk1(self, b4, b1 = False):
        self.b2 = {}
        def fonk2(*args):
            if args in self.b2:
                return self.b2[args]
            else:
                self.b2[args] = b4(b3)(*args)
                return self.b2[args]
        self.b3 = b3
        if b1:
            self.b4 = b4
        else:
            self.b4 = self.fonk4(b4)
    def fonk3(self, *args):
        return self.fonk2(*args)
    def fonk4(self, b4):
        b5 = b4.__name__
        b6 = inspect.getsource(b4)
        b6 = b6.replace(b5, 'h', 1)
        b6 = b6.replace(b5 + '(', 'abc' + '(')
        def fonk5(abc):
            exec(b6, {'abc': abc}, globals())
            return h
        return g
def fonk6(n):
    if n <= 1:
        return n
    else:
        return fonk6(n-1) + fonk6(n-2)
b7 = class1(fibonacci)
print(b7(10))
