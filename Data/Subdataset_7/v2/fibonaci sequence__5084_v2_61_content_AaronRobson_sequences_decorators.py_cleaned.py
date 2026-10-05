class class1(object):
    '''
    Decorator that caches a function's return b3 each time it is called.
    If called later with the same arguments, the cached b3 is returned, and
    not re-evaluated.
    See: http:
    '''
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = {}
    def fonk2(self, *args):
        try:
            return self.b2[args]
        except KeyError:
            b3 = self.b1(*args)
            self.b2[args] = b3
            return b3
        except TypeError:
            return self.b1(*args)
    def fonk3(self):
        '''
        Return the function's docstring.
        '''
        return self.b1.__doc__
b4 = memoised = class1
@b4
def fonk4(n):
    if n <= 1:
        return n
    else:
        return fonk4(n-1) + fonk4(n-2)
if b5 = = "__main__":
    print(fonk4(10))
    print(fonk4(20))