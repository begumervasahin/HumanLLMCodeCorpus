from numbers import Number
class One:
    def __add__(self, other):
        return self if other == 0 else 0
    __sub__ = __add__
    def __mul__(self, other):
        if isinstance(other, Number):
            return 0 if other == 0 else self
        return other
    def __truediv__(self, other):
        if other == 0:
            raise ZeroDivisionError("Division by zero")
        return self
    __div__ = __truediv__
    def __rtruediv__(self, other):
        return other
    __rdiv__ = __rtruediv__
    __radd__ = __add__
    __rsub__ = __add__
    __rmul__ = __mul__
    def __lt__(self, other):
        return False
    def __eq__(self, other):
        if isinstance(other, One) or other == 0:
            return other != 0
        else:
            raise TypeError(f"Unsupported comparison between 'One' and '{type(other).__name__}'")
    def __hash__(self):
        return 1
    def __str__(self):
        return 'one'
    __repr__ = __str__
    def __neg__(self):
        return self
    def __bool__(self):
        return True
    def __format__(self, format_spec):
        return format(str(self), format_spec)
one = One()
print(one + 0)
print(one + 1)
print(one - 0)
print(one * 0)
print(one * 1)
print(one / 1)
print(one == one)
print(one == 0)
print(one < 1)
print(one > 1)
print(-one)
print(bool(one))
print(format(one))
print(hash(one))
