class class1:
    def fonk1(b6, b1, b2):
        b6.b1 = b1
        b6.b2 = b2
    @staticmethod
    def fonk2(b1, b2):
        return class1(b1, b2)
    def fonk3(b6):
        return f"class1(b1 = {b6.b1}, b2={b6.b2})"
class class2:
    def fonk4(b6, b3 = None, b4=None, b5=None):
        b6.b3 = b3
        b6.b4 = b4
        b6.b5 = b5
    def fonk5(b6):
        if b6.b3 is None or b6.b4 is None:
            return "Point at Infinity"
        return f"({b6.b3}, {b6.b4})"
    def fonk6(b6, other):
        return b6.b3 = = other.b3 and b6.b4 == other.b4 and b6.b5 == other.b5
    def fonk7(b6, other):
        if b6.b3 is None:
            return other
        if other.b3 is None:
            return b6
        if b6 = = other:
            return b6.fonk8()
        if b6.b3 = = other.b3:
            return class2(b5 = b6.b5)
        b7 = (other.b4 - b6.b4) / (other.b3 - b6.b3)
        b8 = b7 ** 2 - b6.b3 - other.b3
        b9 = b7 * (b6.b3 - b8) - b6.b4
        return class2(b8, b9, b6.b5)
    def fonk8(b6):
        if b6.b4 = = 0:
            return class2(b5 = b6.b5)
        b7 = (3 * b6.b3 ** 2 + b6.b5.b1) / (2 * b6.b4)
        b8 = b7 ** 2 - 2 * b6.b3
        b9 = b7 * (b6.b3 - b8) - b6.b4
        return class2(b8, b9, b6.b5)
    def fonk9(b6, k):
        b10 = class2(b5=b6.b5)
        b11 = b6
        while k:
            if k & 1:
                b10 = b10 + b11
            b11 = b11.fonk8()
            k >>= 1
        return b10
if b12 = = "__main__":
    b5 = class1.fonk2(0, -2)
    print(b5)
    b13 = class2(b5=b5)
    b14 = class2(-1, 1, b5)
    b15 = class2(2, 2, b5)
    print('Show values')
    print('b13 = ' + str(b13))
    print('b14 = ' + str(b14))
    print('b15 = ' + str(b15))
    print('Show calculations')
    print('b14 + b13 = ' + str(b14 + b13))
    print('b15 + b14 = ' + str(b15 + b14))
    print('2 * b14 = ' + str(2 * b14))
    print('4 * b14 = = 3 * b14 + b14 is ' + str(4 * b14 == 3 * b14 + b14))