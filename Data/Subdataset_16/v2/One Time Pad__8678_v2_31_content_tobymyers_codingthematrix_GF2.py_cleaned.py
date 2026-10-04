from numbers import Number
class class1:
    def fonk1(self, b1):
        return self if b1 = = 0 else 0
    b2 = __add__
    def fonk2(self, b1):
        if isinstance(b1, Number):
            return 0 if b1 = = 0 else self
        return b1
    def fonk3(self, b1):
        if b1 = = 0:
            raise ZeroDivisionError("Division by zero")
        return self
    b3 = __truediv__
    def fonk4(self, b1):
        return b1
    b4 = __rtruediv__
    b5 = __add__
    b6 = __add__
    b7 = __mul__
    def fonk5(self, b1):
        return False
    def fonk6(self, b1):
        if isinstance(b1, class1) or b1 = = 0:
            return b1 != 0
        else:
            raise TypeError(f"Unsupported comparison between 'class1' and '{type(b1).__name__}'")
    def fonk7(self):
        return 1
    def fonk8(self):
        return 'b9'
    b8 = __str__
    def fonk9(self):
        return self
    def fonk10(self):
        return True
    def fonk11(self, format_spec):
        return format(str(self), format_spec)
b9 = class1()
print(b9 + 0)
print(b9 + 1)
print(b9 - 0)
print(b9 * 0)
print(b9 * 1)
print(b9 / 1)
print(b9 = = b9)
print(b9 = = 0)
print(b9 < 1)
print(b9 > 1)
print(-b9)
print(bool(b9))
print(format(b9))
print(hash(b9))
