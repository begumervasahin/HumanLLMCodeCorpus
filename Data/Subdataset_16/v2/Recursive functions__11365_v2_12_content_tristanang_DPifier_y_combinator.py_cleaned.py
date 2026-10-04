import inspect
class class1:
    def fonk1(self, b4, b1 = False):
        self.b2 = {}
        self.b3 = self.fonk3()
        self.b4 = b4 if b1 else self.fonk6(b4)
    def fonk2(self, *args):
        return self.b3(self.b4)(*args)
    def fonk3(self):
        def fonk4(b4):
            def fonk5(*args):
                if args in self.b2:
                    return self.b2[args]
                else:
                    b5 = b4(fonk4(b4))(*args)
                    self.b2[args] = b5
                    return b5
            return wrapper
        return memoizer
    def fonk6(self, b4):
        b6 = b4.__name__
        b7 = inspect.getsource(b4)
        b8 = b7.replace(b6, 'inner_func', 1).replace(b4"{b6}(", "wrapped_func(", 1)
        def fonk7(wrapped_func):
            exec(b8, {'wrapped_func': wrapped_func}, globals())
            return inner_func
        return wrapper_function
def fonk8(b4):
    def fonk9(b9):
        if b9 = = 0:
            return 1
        else:
            return b9 * b4(b9 - 1)
    return inner_func
b10 = class1(factorial)
print(b10(5))
