import matplotlib.pyplot as plt
import math
class class1:
    def fonk1(b14, prime_modulus, coefficient_a, coefficient_b, base_point, order, cofactor):
        b14.b1 = prime_modulus
        b14.b2 = coefficient_a
        b14.b3 = coefficient_b
        b14.b4 = base_point
        b14.b5 = order
        b14.b6 = cofactor
    def fonk2(b14, n_points):
        b7 = []
        b8 = []
        for i in range(n_points):
            b7.append(i)
            b8.append(math.sqrt(i**3 + b14.b2*i + b14.b3))
        plt.plot(b7, b8)
        plt.show()
class class2(class1):
    def fonk3(b14, x_coord, y_coord, b11):
        super().fonk3(b11.b1, b11.b2, b11.b3, b11.b4, b11.b5, b11.b6)
        b14.b9 = x_coord
        b14.b10 = y_coord
        b14.b11 = b11
    def fonk4(b14, other):
        if b14.b9 < other.b9:
            b2 = b14
            b3 = other
        else:
            b2 = other
            b3 = b14
        if b2.b9 = = 0 and b2.b10 == 0:
            return b3
        elif b3.b9 = = 0 and b3.b10 == 0:
            return b2
        elif b3 = = b2.fonk6():
            return class2(0, 0, b2.b11)
        else:
            if b2 = = b3:
                b12 = (3 * (b2.b9**2) + b2.b11.b2) * b2.fonk5(2*b2.b10)
            else:
                b12 = (b3.b10 - b2.b10) * b2.fonk5(b3.b9 - b2.b9)
        b13 = class2(0, 0, b2.b11)
        b13.b9 = ((b12**2 % b2.b11.b1) - b2.b9 - b3.b9) % b2.b11.b1
        b13.b10 = (b12 * (b2.b9 - b13.b9) - b2.b10) % b2.b11.b1
        return b13
    def fonk5(b14, b9):
        return pow(b9, b14.b11.b1-2, b14.b11.b1)
    def fonk6(b14):
        if b14.b9 = = 0 and b14.b10 == 0:
            return b14
        return class2(b14.b9, (-b14.b10) % b14.b11.b1, b14.b11)
    def fonk7(b14, other):
        return b14.b9 = = other.b9 and b14.b10 == other.b10 and b14.b11 == other.b11
    def fonk8(b14, other):
        return not b14 = = other
    def fonk9(b14, scalar):
        b15 = bin(scalar)[2:]
        b16 = class2(b14.b9, b14.b10, b14.b11)
        b17 = class2(b14.b9, b14.b10, b14.b11)
        b15.pop()
        b15.reverse()
        for b18 in b15:
            if b18 = = '0':
                b16 = b16 + b16
                b16.b9 %= b14.b11.b1
                b16.b10 %= b14.b11.b1
            else:
                b16 = b16 + b16
                b16.b9 %= b14.b11.b1
                b16.b10 %= b14.b11.b1
                b16 = b16 + b17
                b16.b9 %= b14.b11.b1
                b16.b10 %= b14.b11.b1
        return b16