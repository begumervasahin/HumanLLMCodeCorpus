a1 = 23
b1 = (a1, a1)
b2 = [(b3,b4) for b3 in range(a1) for b4 in range(a1) if (b3 ** 3 + b3 * 2 + 7) % a1 == b4 * b4 % a1]
def fonk1(b3):
    for i in range(a1):
        if i * b3 % a1 = = 1:
            return i
    raise Exception('Reciprocal not found')
class class1:
    def fonk2(b9, x_init, y_init):
        b9.b3 = x_init
        b9.b4 = y_init
        if b9.fonk3() not in b2 and b9.fonk3() != b1:
            raise Exception('Invalid initialization')
    def fonk3(b9):
        return (b9.b3, b9.b4)
    def fonk4(b9):
        print(b9.fonk3())
    def fonk5(b9, another):
        if b9.fonk3() == b1:
            return another
        if another.fonk3() == b1:
            return b9
        b5 = b9.b3
        b6 = b9.b4
        b7 = another.b3
        b8 = another.b4
        if b5 = = b7 and b6 == -b8:
            return class1(a1, a1)
        if b9 = = another:
            b10 = (3 * b5 * b5 + 2) * fonk1(2 * b8) % a1
        else:
            b10 = (b8 - b6) * fonk1(b7 - b5) % a1
        b11 = (b10 * b10 - b5 - b7) % a1
        b12 = (b10 * (b5 - b11) - b6) % a1
        return class1(b11, b12)
    def fonk6(b9, number):
        b13 = b9
        for i in range(number - 1):
            b13 = b13 + b9
        return b13