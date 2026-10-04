class class1:
    def fonk1(b14, b1, b2):
        b14.b1 = b1 % b2
        b14.b2 = b2
    @staticmethod
    def fonk2(b2):
        return class1(0, b2)
    def fonk3(b14):
        return f'class1({b14.b1}, {b14.b2})'
    def fonk4(b14, other):
        if b14.b2 != other.b2:
            raise ValueError("Cannot add two numbers in different fields")
        return class1(b14.b1 + other.b1, b14.b2)
    def fonk5(b14, other):
        if b14.b2 != other.b2:
            raise ValueError("Cannot subtract two numbers in different fields")
        return class1(b14.b1 - other.b1, b14.b2)
    def fonk6(b14, other):
        if b14.b2 != other.b2:
            raise ValueError("Cannot multiply two numbers in different fields")
        return class1(b14.b1 * other.b1, b14.b2)
    def fonk7(b14, other):
        if b14.b2 != other.b2:
            raise ValueError("Cannot divide two numbers in different fields")
        return b14 * other.fonk8()
    def fonk8(b14):
        b6, b3 = 0, 1
        r, b4 = b14.b2, b14.b1
        while b4 != 0:
            b5 = r
            b6, b3 = b3, b6 - b5 * b3
            r, b4 = b4, r - b5 * b4
        if r > 1:
            raise ValueError("No inverse exists")
        if b6 < 0:
            b6 = b6 + b14.b2
        return class1(b6, b14.b2)
class class2:
    def fonk9(b14, b7, b8, b2):
        b14.b7 = class1(b7, b2)
        b14.b8 = class1(b8, b2)
        b14.b2 = b2
    @staticmethod
    def fonk10(b7, b8, b2):
        return class2(b7, b8, b2)
    def fonk11(b14):
        return f'class2(b13^b9 = b10^3 + {b14.b7}b10 + {b14.b8} over F_{b14.b2})'
class class3:
    def fonk12(b14, b10 = None, b13=None, b11=None):
        b14.b11 = b11 if b11 else class2.fonk10(0, 1, 5)
        if b10 is None and b13 is None:
            b14.b12 = True
            b14.b10 = None
            b14.b13 = None
        else:
            b14.b12 = False
            b14.b10 = class1(b10, b14.b11.b2)
            b14.b13 = class1(b13, b14.b11.b2)
    def fonk13(b14):
        if b14.b12:
            return 'class3(Infinity)'
        return f'class3({b14.b10}, {b14.b13})'
    def fonk14(b14, other):
        if b14.b12:
            return other
        if other.b12:
            return b14
        if b14.b10 = = other.b10 and b14.b13 != other.b13:
            return class3(b11 = b14.b11)
        if b14 = = other:
            b15 = (class1(3, b14.b11.b2) * b14.b10**b9 + b14.b11.b7) / (class1(b9, b14.b11.b2) * b14.b13)
        else:
            b15 = (other.b13 - b14.b13) / (other.b10 - b14.b10)
        b16 = b15**b9 - b14.b10 - other.b10
        b17 = b15 * (b14.b10 - b16) - b14.b13
        return class3(b16.b1, b17.b1, b14.b11)
    def fonk15(b14, n):
        b18 = class3(b11=b14.b11)
        b19 = b14
        while n:
            if n & 1:
                b18 = b18 + b19
            b19 = b19 + b19
            n >>= 1
        return b18
def fonk16():
    print(class1.fonk10(5))
    b11 = class2.fonk10(0, 1, 5)
    print(b11)
    b20 = class3(b11=b11)
    b21 = class3(0, 1, b11=b11)
    b22 = class3(0, 4, b11=b11)
    b23 = class3(b9, 1, b11=b11)
    b24 = class3(b9, 4, b11=b11)
    b25 = class3(3, 1, b11=b11)
    b26 = class3(3, 4, b11=b11)
    print(b20)
    print(b21)
    print(b22)
    print(b23)
    print(b24)
    print(b25)
    print(b26)
    print('Calculations:')
    print(b9 * b23)
    print(b20 + b21)
    print(b23 + b21)
    print(b25 + b23)
if b27 = = '__main__':
    fonk16()