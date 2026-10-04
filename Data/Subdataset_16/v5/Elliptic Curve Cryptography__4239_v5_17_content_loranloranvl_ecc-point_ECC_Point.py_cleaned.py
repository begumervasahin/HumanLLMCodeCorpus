a1 = 23
b1 = (a1, a1)
b2 = [(b3, b4) for b3 in range(a1) for b4 in range(a1) if (b3**3 + b3*2 + 7) % a1 == b4*b4 % a1]
def fonk1(b3):
    for i in range(a1):
        if i * b3 % a1 = = 1:
            return i
    raise Exception('Reciprocal not found')
class class1:
    def fonk2(b8, b3, b4):
        b8.b3 = b3
        b8.b4 = b4
        if b8.fonk3() not in b2 and b8.fonk3() != b1:
            raise Exception('Invalid initialization')
    def fonk3(b8):
        return (b8.b3, b8.b4)
    def fonk4(b8):
        print(b8.fonk3())
    def fonk5(b8, other):
        if b8.fonk3() == b1:
            return other
        if other.fonk3() == b1:
            return b8
        b7, b5 = b8.b3, b8.b4
        x2, b6 = other.b3, other.b4
        if b7 = = x2 and b5 == -b6:
            return class1(a1, a1)
        if b8 = = other:
            b9 = (3 * b7 * b7 + 2) * fonk1(2 * b5) % a1
        else:
            b9 = (b6 - b5) * fonk1(x2 - b7) % a1
        b10 = (b9 * b9 - b7 - x2) % a1
        b11 = (b9 * (b7 - b10) - b5) % a1
        return class1(b10, b11)
    def fonk6(b8, n):
        b12 = b8
        for _ in range(n - 1):
            b12 = b12 + b8
        return b12