class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = {}
    def fonk2(self, *args):
        if args in self.b2:
            return self.b2[args]
        try:
            b3 = self.b1(*args)
            self.b2[args] = b3
            return b3
        except TypeError:
            return self.b1(*args)
    def fonk3(self):
        return self.b1.__doc__
b4 = memoised = class1
@b4
def fonk4(n):
    if n < 2:
        return n
    return fonk4(n - 1) + fonk4(n - 2)
def fonk5():
    for i in range(10, 21, 5):
        print(f"Fibonacci({i}): {fonk4(i)}")
if b5 = = "__main__":
    fonk5()