class class1:
    '''A decorator that caches a function's return b3 each time it is called.
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
        '''Return the function's docstring.'''
        return self.b1.__doc__
b4 = memoised = class1