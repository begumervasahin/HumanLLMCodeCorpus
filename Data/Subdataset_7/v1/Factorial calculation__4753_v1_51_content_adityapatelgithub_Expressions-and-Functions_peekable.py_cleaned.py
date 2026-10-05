class class1():
    def fonk1(self, iterator):
        self.b1 = iterator
        self.b2 = None
    def fonk2(self):
        return self
    def fonk3(self):
        if self.b2 is None:
            self.b2 = next(self.b1)
        b3 = self.b2
        self.b2 = None
        return b3
    def fonk4(self):
        if self.b2 is None:
            self.b2 = next(self.b1)
        return self.b2
def fonk5(x):
    return x.fonk5()
if b4 = = "__main__":
    b5 = class1(iter([1, 2, 3, 4, 5]))
    print(fonk5(b5))
    print(fonk5(b5))
    print(next(b5))
    print(next(b5))
    print(next(b5))
    print(fonk5(b5))
    print(next(b5))
    print(list(class1(iter([1, 2, 3, 4, 5]))))
